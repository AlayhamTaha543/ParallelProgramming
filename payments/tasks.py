from celery import shared_task
import time 

@shared_task
def generate_and_send_invoice(order_id, user_email):
    print(f"Starting to generate invoice for Order {order_id}...")
    time.sleep(5) 
    print(f"Success! Invoice sent to {user_email}")
    
    return "Task completed"