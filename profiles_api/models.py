from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


"""To make django understand the custom use model"""
class UserProfileManager(BaseUserManager):
    def create_user(self,email, name, password = None):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have email address')

        """Normalize email"""
        email = self.normalize_email(email)
        user = self.model(email = email, name = name)

        user.set_password(password)

        """To save into data base"""
        user.save(using = self._db)
        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email,name,password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using = self._db)
        return user


class UserProfile(AbstractBaseUser,PermissionsMixin):
    """Database model for users in system"""
    email = models.EmailField(max_length = 255, unique = True)
    name = models.CharField(max_length = 255)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)

    """Custom model manager"""
    objects = UserProfileManager()

    """Add fields to the class"""

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
         """Retreive full name of user"""
         return self.name
    def get_short_name(self):
        return self.name

    """String representation of user"""
    def __str__(self):
        return self.email

    """Create Super User"""
