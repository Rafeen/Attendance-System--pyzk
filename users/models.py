from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return "{}".format(self.username)

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    full_name = models.CharField(max_length=30)
    department = models.CharField(max_length=30)
    employee_id = models.CharField(max_length=30, unique=True)
    app_user_id = models.IntegerField()
    # User Roles Choices
    Admin = 'A'
    Employee = 'E'
    ROLE_CHOICES = (
        (Admin, 'Admin'), #First element is value, Second element is human readable representation of the value
        (Employee, 'Employee'),

    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=Employee)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name