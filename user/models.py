from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinLengthValidator

class CustomAccountManager(BaseUserManager):

    def create_user(self,phone_number, email, password, **other_fields):
        if not phone_number:
            raise ValueError(_('You must provide an phone number'))

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(mobile=mobile, email=email, **other_fields)
        user.set_password(password)
        user.save()
        return user



class User(AbstractBaseUser):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    country_code = models.CharField(max_length = 100)
    gender = models.CharField(max_length = 6)
    birthdate = models.DateField()
    avatar = models.FileField()
    email = models.EmailField(max_length = 80, null = True, unique = True)
    phone_number = PhoneNumberField( max_length = 15, unique = True,  validators=[MinLengthValidator(10)])
    objects = CustomAccountManager()
    USERNAME_FIELD = 'phone_number'
