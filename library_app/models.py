from django.db import models
from library_auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    description = models.TextField()
    quantity = models.PositiveIntegerField(default=0)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)
    is_delivered = models.BooleanField(default=False)

    def __str__(self):
        return f"Order {self.id}"

class Delivery(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, unique=True)
    tracking_number = models.CharField(max_length=100)
    courier = models.CharField(max_length=100)
    delivery_date = models.DateField()
    is_delivered = models.BooleanField(default=False)

    def __str__(self):
        return f"Delivery for Order {self.order.id}"

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

class ReturnBook(models.Model):
    delivery = models.OneToOneField(Delivery, on_delete=models.CASCADE, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fine = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    fine_reason = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"Issued Book: {self.delivery.order.book.title}"