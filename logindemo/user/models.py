from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.validators import RegexValidator
from django.dispatch import receiver

from .managers import CustomUserManager
from phonenumber_field.modelfields import PhoneNumberField
import random


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(_('username'), max_length=50, null=True, blank=True, unique=True)
    first_name = models.CharField(_('first name'),max_length=100, null=True, blank=True)
    last_name = models.CharField(_('last name'),max_length=100, null=True, blank=True)
    mobile_number = PhoneNumberField(unique=True,blank=True)
    otp = models.CharField(max_length=20, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['mobile_number']

    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        # if self.mobile_number:
        #     self.otp = str(random.randint(100000, 999999))
        super(CustomUser, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.email

@receiver(post_save, sender=CustomUser)
def send_otp(sender, instance, created, **kwargs):
    if created:
        print(instance.mobile_number, instance.otp)
# @receiver(post_save, sender=Client)
# def createSuperUser(sender, instance, created, *args, **kwargs):
#     if created:
#         invalidInputs = ["", None]

#         user = CustomUser(
#             username = "",
#             email = "user1@mail.com",
#             first_name = "",
#             last_name = "",
#         )

#         user.set_password("helloworld")
#         user.is_superuser = True
#         user.is_staff = True
#         user.save()
#         return user