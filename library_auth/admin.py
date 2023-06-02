from django.contrib import admin
from .models import User, Student, Librarian, Teacher

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone', 'address', 'user_role')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'roll_number', 'batch')

@admin.register(Librarian)
class LibrarianAdmin(admin.ModelAdmin):
    list_display = ('user', 'employee_ID', 'employee_role')

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('user', 'employee_id', 'department')

# Optionally, you can customize the admin site header and title
admin.site.site_header = 'Library Management System Admin'
admin.site.site_title = 'Library Management System Admin'
