from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, Role, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, Role=Role, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, Role, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, Role, password, **extra_fields)


class User(AbstractBaseUser,PermissionsMixin):
    username = None
    email = models.EmailField(unique=True)
    user_type = (
        ("Org","organization"),
        ("Vol","volunteer")
    )
    Role = models.CharField(choices = user_type, max_length=50)
    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['Role']
    is_staff = models.BooleanField(default = False)
    is_active = models.BooleanField(default = True)
    
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        
    def __str__(self):
        return self.email
    