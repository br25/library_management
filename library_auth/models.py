from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    USER_ROLES = (
        ('student', 'Student'),
        ('librarian', 'Librarian'),
        ('teacher', 'Teacher'),
    )

    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    user_role = models.CharField(max_length=20, choices=USER_ROLES)


    def __str__(self):
        return self.username


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll_number = models.CharField(max_length=20)
    batch = models.CharField(max_length=20)

    def __str__(self):
        return f"Student: {self.user.username}"

class Librarian(models.Model):
    EMPLOYEE_ROLES = (
        ('manager', 'Manager'),
        ('staff', 'Staff'),
        ('accounts', 'Accounts'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_ID = models.CharField(max_length=20)
    employee_role = models.CharField(max_length=20, choices=EMPLOYEE_ROLES)

    def __str__(self):
        return self.user.username

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=20)
    department = models.CharField(max_length=50)

    def __str__(self):
        return f"Teacher: {self.user.username}"
