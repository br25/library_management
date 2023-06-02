from django.contrib import admin
from .models import Category, Book, IssuedBook, Order

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'publication_date', 'isbn', 'quantity', 'available')

@admin.register(IssuedBook)
class IssuedBookAdmin(admin.ModelAdmin):
    list_display = ('book', 'issued_date', 'return_date', 'fine', 'fine_reason')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'order_date', 'is_completed')

# You can register other models here if needed

# Optionally, you can customize the admin site header and title
admin.site.site_header = 'Library Management System Admin'
admin.site.site_title = 'Library Management System Admin'
