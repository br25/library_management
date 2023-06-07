from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Delivery, Notification

@receiver(post_save, sender=Delivery)
def send_delivery_notification(sender, instance, created, **kwargs):
    if created:
        user = instance.order.user
        notification = Notification.objects.create(
            user=user,
            message=f'The book has been delivered. Order ID: {instance.order.id}. Book return Date is: {instance.order.return_date}'
        )