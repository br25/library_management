from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order, Delivery, Notification

def send_notification(subject, message, recipient):
    send_mail(subject, message, 'no-reply@gmail.com', [recipient])

@receiver(post_save, sender=Delivery)
def notify_delivery_created(sender, instance, created, **kwargs):
    if created:
        order = instance.order
        user = order.user
        message = f'Your order for "{order.book.title}" has been shipped. Tracking number: {instance.tracking_number}'
        Notification.objects.create(user=user, message=message)

def get_unread_notifications(user):
    return Notification.objects.filter(user=user, is_read=False)

def mark_notification_as_read(notification):
    notification.is_read = True
    notification.save()
