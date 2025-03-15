import importlib
import secrets
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .manager import UserManager
from django.core.validators import RegexValidator, validate_email

GENDER= (
    ("Male","Male"),
    ("Female","Female"),
)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True, validators=[validate_email])
    first_name = models.CharField(_('first name'), max_length=30)
    last_name = models.CharField(_('last name'), max_length=30)
    image = models.ImageField(default="default.png", blank=True, upload_to="images")
    gender = models.CharField(max_length=50, choices=GENDER)
    
    
    is_staff = models.BooleanField(_('staff status'), default=False)
    is_superuser = models.BooleanField(_('superuser status'), default=False)
    is_verified = models.BooleanField(_('verified status'), default=False)
    is_active = models.BooleanField(_('active status'), default=False)
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'gender']
    

    objects = UserManager()
    
    
    def __str__(self):
        return self.email
    
class OneTimePassword(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    otp_code = models.CharField(max_length=6, default=secrets.token_hex(3))
    max_otp_try = models.CharField(max_length=2, default=settings.MAX_OTP_TRY)
    otp_max_out = models.DateTimeField(blank=True, null=True)
    otp_expires_at = models.DateTimeField(blank=True, null=True)
    otp_created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user.first_name}-passcode"
    
    db_name = 'OTP_table'