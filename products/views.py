import logging
from django.core.cache import cache
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework.decorators import action

from products.permission import IsProductStoreOwner

from .models import Product
from .serializers import ProductSerializer

from store.models import Store

logger = logging.getLogger(__name__)

class ProductViewSet(ModelViewSet):

    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsProductStoreOwner]
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    def get_queryset(self):
        store_id = self.kwargs['store_pk']
        return Product.objects.filter(store_id=store_id)

    def perform_create(self, serializer):
        store_id = self.kwargs['store_pk']
        store = Store.objects.get(id=store_id)
        
        if store.owner != self.request.user:
            raise PermissionDenied('This store does not belong to you')

        serializer.save(store=store)

    def list(self, request, *args, **kwargs):
        store_id = kwargs.get('store_pk')
        cache_key = f"product_list:store:{store_id}:url:{request.get_full_path()}"
        
        try:
            cached_data = cache.get(cache_key)
            if cached_data:
                # Update with fresh price and stock from individual keys
                items = cached_data['results'] if isinstance(cached_data, dict) and 'results' in cached_data else cached_data
                
                missing_ids = []
                for item in items:
                    pid = item['id']
                    price = cache.get(f"product:{pid}:price")
                    stock = cache.get(f"product:{pid}:stock")
                    if price is not None and stock is not None:
                        item['price'] = price
                        item['stock'] = stock
                    else:
                        missing_ids.append(pid)
                
                if missing_ids:
                    fresh_products = {p.id: p for p in Product.objects.filter(id__in=missing_ids).only('id', 'price', 'stock')}
                    for item in items:
                        if item['id'] in missing_ids:
                            p = fresh_products.get(item['id'])
                            if p:
                                item['price'] = str(p.price)
                                item['stock'] = p.stock
                                cache.set(f"product:{p.id}:price", str(p.price), timeout=None)
                                cache.set(f"product:{p.id}:stock", p.stock, timeout=None)
                                
                return Response(cached_data)
        except Exception as e:
            logger.error(f"Redis cache error: {e}")
            cached_data = None

        response = super().list(request, *args, **kwargs)
        
        try:
            cache.set(cache_key, response.data, timeout=300)
            items = response.data['results'] if isinstance(response.data, dict) and 'results' in response.data else response.data
            for item in items:
                cache.set(f"product:{item['id']}:price", item['price'], timeout=None)
                cache.set(f"product:{item['id']}:stock", item['stock'], timeout=None)
        except Exception as e:
            logger.error(f"Redis cache error: {e}")
            
        return response

    def retrieve(self, request, *args, **kwargs):
        # cache per product ID, TTL 10 minutes.
        instance_id = kwargs.get('pk')
        cache_key = f"product:{instance_id}"
        
        try:
            cached_data = cache.get(cache_key)
            if cached_data:
                # Fetch price and stock from cache or DB
                price_key = f"product:{instance_id}:price"
                stock_key = f"product:{instance_id}:stock"
                
                price = cache.get(price_key)
                stock = cache.get(stock_key)
                
                if price is None or stock is None:
                    try:
                        fresh_obj = Product.objects.only('price', 'stock').get(pk=instance_id)
                        price = str(fresh_obj.price)
                        stock = fresh_obj.stock
                        cache.set(price_key, price, timeout=None)
                        cache.set(stock_key, stock, timeout=None)
                    except Product.DoesNotExist:
                        pass
                
                cached_data['price'] = price
                cached_data['stock'] = stock
                return Response(cached_data)
        except Exception as e:
            logger.error(f"Redis cache error: {e}")
            cached_data = None

        response = super().retrieve(request, *args, **kwargs)
        
        try:
            cache.set(cache_key, response.data, timeout=600) # 10 minutes
            # Also cache price and stock
            cache.set(f"product:{instance_id}:price", response.data['price'], timeout=None)
            cache.set(f"product:{instance_id}:stock", response.data['stock'], timeout=None)
        except Exception as e:
            logger.error(f"Redis cache error: {e}")
            
        return response

    @action(detail=True, methods=['post'])
    def increment_view(self, request, store_pk=None, pk=None):
        cache_key = f"product:{pk}:views"
        try:
            views = cache.incr(cache_key)
        except ValueError:
            # key doesn't exist
            try:
                product = Product.objects.get(pk=pk)
                cache.set(cache_key, product.views + 1, timeout=None)
                views = product.views + 1
            except Exception:
                pass
        except Exception as e:
            logger.error(f"Redis cache error: {e}")
            
        return Response({"status": "view incremented"})

    @action(detail=True, methods=['post'])
    def increment_like(self, request, store_pk=None, pk=None):
        cache_key = f"product:{pk}:likes"
        try:
            likes = cache.incr(cache_key)
        except ValueError:
            try:
                product = Product.objects.get(pk=pk)
                cache.set(cache_key, product.likes + 1, timeout=None)
                likes = product.likes + 1
            except Exception:
                pass
        except Exception as e:
            logger.error(f"Redis cache error: {e}")
            
        return Response({"status": "like incremented"})
