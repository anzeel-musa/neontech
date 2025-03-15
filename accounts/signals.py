from django.contrib.auth.models import User
#from .models import Profile

from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from django.core.mail import send_mail
from django.utils import timezone
from django.core.mail import EmailMessage
from TECH_SOLUTIONS import settings
from accounts.models import  User, OneTimePassword
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


@receiver(post_save, sender=settings.AUTH_USER_MODEL) 
def create_token(sender, instance, created, *args,**kwargs):
    if created:
        if instance.is_superuser:
            pass
        
        else:
            otp = OneTimePassword.objects.create(user=instance, max_otp_try=settings.MAX_OTP_TRY, otp_expires_at=timezone.now() + timezone.timedelta(minutes=5),
                                                 otp_max_out=timezone.now() + timezone.timedelta(hours=1))
            instance.is_active=False 
            instance.is_email_verified=False
            instance.is_verified=False
            instance.email
            instance.save()
        context = {
                'otp': otp,
                'url': f"http://127.0.0.1:8000/verify-email/{instance.email}", }
               
        # email variables
        template_name = "otp/receiver_otp.html"
        convert_to_html_content =  render_to_string(
        template_name=template_name,
        context=context
        )
        plain_message = strip_tags(convert_to_html_content)
        
        yo_send_it = send_mail(
                subject="Email Verification",
                message=plain_message,
                from_email = settings.DEFAULT_FROM_EMAIL,
                recipient_list = [instance.email, ],
                html_message=convert_to_html_content,
                fail_silently=False,
            )