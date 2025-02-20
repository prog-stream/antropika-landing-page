from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager
from django.db import models
from rest_framework.fields import Field


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=128, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    language = models.CharField(max_length=255, null=True, blank=True)
    status = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_login = None
    username = None

    objects = UserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ()

    @staticmethod
    def convertNone(value):
        if value is None:
            return ''
        else:
            return value

    class Meta:
        db_table = 'users'