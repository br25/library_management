from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)

        if kwargs.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if kwargs.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **kwargs)


class User(AbstractUser):
    USER_ROLES = (
        ('student', 'Student'),
        ('librarian', 'Librarian'),
        ('teacher', 'Teacher'),
    )

    username = models.CharField(max_length=50, null=True, default=None)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    user_role = models.CharField(max_length=20, choices=USER_ROLES)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

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
