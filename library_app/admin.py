from django.contrib import admin
from .models import Category, Book, Order, Delivery, Notification, ReturnBook

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'publication_date', 'isbn', 'quantity', 'available')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'order_date')


@admin.register(Delivery)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order', 'tracking_number', 'courier', 'delivery_date')

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'is_read')

@admin.register(ReturnBook)
class ReturnBookAdmin(admin.ModelAdmin):
    list_display = ('delivery', 'fine', 'fine_reason')


# You can register other models here if needed

# Optionally, you can customize the admin site header and title
admin.site.site_header = 'Library Management System Admin'
admin.site.site_title = 'Library Management System Admin'
