from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):

    class Role(models.TextChoices):
        ADMIN = "ADMIN" , "admin"
        SELLER = "SELLER" , "seller"
        CUSTOMER = "CUSTOMER" , "customer"

    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20 , choices=Role.choices , default=Role.CUSTOMER)


    def save(self, *args, **kwargs):
        """
        submit user role as ADMIN if the user is a staff type
        """
        if self.is_staff:
            self.role = self.Role.ADMIN
        elif self.role == self.Role.ADMIN and not self.is_staff :
            self.role = self.Role.CUSTOMER

        super().save(*args, **kwargs)


class UserProfile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE , related_name="profile")
    bio = models.TextField(blank=True , null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_seller_applicant = models.BooleanField(default=False) # reminder : apply Automated Process


    def __str__(self):
        return f"{self.user.username}'s Profile"
