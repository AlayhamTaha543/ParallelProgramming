from django.core.management.base import BaseCommand
from django.core.cache import cache
from products.models import Product

class Command(BaseCommand):
    help = 'Flushes views and likes from Redis cache to DB'

    def handle(self, *args, **options):
        # We can iterate through product IDs or keys
        products = Product.objects.all()
        for product in products:
            views_key = f"product:{product.id}:views"
            likes_key = f"product:{product.id}:likes"
            
            views = cache.get(views_key)
            likes = cache.get(likes_key)
            
            updated = False
            if views is not None and views > product.views:
                product.views = views
                updated = True
            
            if likes is not None and likes > product.likes:
                product.likes = likes
                updated = True
                
            if updated:
                product.save(update_fields=['views', 'likes'])
                self.stdout.write(self.style.SUCCESS(f'Updated Product {product.id} (views: {product.views}, likes: {product.likes})'))
        self.stdout.write(self.style.SUCCESS('Successfully flushed all counters'))