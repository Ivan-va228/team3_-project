from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, nickname, password=None, first_name=None, last_name=None):
        if not email:
            raise ValueError("Користувач повинен мати email")
        if not nickname:
            raise ValueError("Користувач повинен мати нікнейм")

        email = self.normalize_email(email)
        user = self.model(email=email, nickname=nickname, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nickname, password, first_name=None, last_name=None):
        user = self.create_user(email, nickname, password, first_name, last_name)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """Кастомна модель користувача"""
    
    nickname = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    nickname = models.CharField(max_length=30, unique=True)  
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    
    
    USERNAME_FIELD = 'nickname'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager() 

    def __str__(self):
        return self.nickname
