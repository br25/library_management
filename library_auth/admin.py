from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone', 'address', 'user_role')

# Optionally, you can customize the admin site header and title
admin.site.site_header = 'Library Management System Admin'
admin.site.site_title = 'Library Management System Admin'
