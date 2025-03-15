import datetime
from django.http import HttpResponseRedirect,HttpResponse
from django.utils import timezone
from django.conf import settings
from django.shortcuts import redirect, render
from rest_framework.generics import GenericAPIView

from django.core.mail import send_mail
from accounts.models import OneTimePassword, User
from accounts.signals import create_token
#from.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from django.contrib import messages      
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

#@action(detail=True, methods=["PATCH"])
def verify_email(request, email):
    user = User.objects.get(email=email)
    otp = OneTimePassword.objects.filter(user=user).last()
    if request.method == 'POST':
        if otp.otp_code == request.POST["otp_code"]:
           
            #valid token
            if not user.is_active and otp.otp_expires_at and timezone.now() < otp.otp_expires_at:
                user.is_active = True
                user.is_verified = True
                user.otp_expires_at = None
                user.max_otp_try = settings.MAX_OTP_TRY
                user.otp_max_out = None
                user.save()
                messages.success(request, "Email verified successfully")
                return redirect('home')
            elif user.is_active and user.is_verified and timezone.now() > otp.otp_expires_at:
                messages.error(request, "OTP has expired")
                return redirect('verify-email', email=user.email)
            else:
                messages.error(request, "Invalid OTP")
                return HttpResponse('your otp has been verified')
        #invalid otp code
        else:
           messages.error(request, "Invalid OTP")
           return redirect('verify-email', email=user.email)
    context = {}
    return render(request, 'otp/verify_token.html', context)



#@action(detail=True, methods=["PATCH"])
def resend_otp(request):
    if request.method == 'POST':
        user_email = request.POST["otp_email"]
        if User.objects.filter(email=user_email).exists():
              
            instance = OneTimePassword.objects.filter(user__email=user_email).last()
            max_otp_try = instance.max_otp_try
            otp_max_out = instance.otp_max_out

            if int(max_otp_try) == 0 and timezone.now() < otp_max_out:
                messages.warning(request, "You have reached the maximum number of attempts for OTP verification. Please try again after an hour.")
                return redirect("resend-otp")
            else:
                user = User.objects.get(email=user_email)
                otp = OneTimePassword.objects.create(user=user, otp_expires_at=timezone.now() + timezone.timedelta(minutes=5), max_otp_try = int(max_otp_try) - 1, otp_max_out=timezone.now() + timezone.timedelta(hours=1))

                if max_otp_try == 0:
                # Set cool down time
                    otp_max_out = timezone.now() + datetime.timedelta(hours=1)
                    instance.otp_max_out = otp_max_out
                elif max_otp_try == -1:
                    otp_max_out = timezone.now() + datetime.timedelta(hours=1)
                    instance.otp_max_out = otp_max_out
                    # instance.max_otp_try = settings.MAX_OTP_TRY
                else:
                    instance.otp_max_out = None
                    instance.max_otp_try = max_otp_try
                instance.save()

                context = {
                    'user': user,
                    'otp': otp,
                    'expiry': otp.otp_expires_at.strftime("%d-%m-%Y %H:%M:%S"),
                    'url': f"http://127.0.0.1:8000/verify-email/{user.email}",
                }

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
                        recipient_list = [user.email, ],
                        html_message=convert_to_html_content,
                        fail_silently=False,
                    )
                messages.success(request, "A new OTP has been sent to your email-address")
                return redirect("verify-email", email=user.email)
        else:
            messages.warning(request, f'This email, {user_email} does not exist')
            return render(request, "otp/resend_otp.html")      
 
    return render(request, "otp/resend_otp.html")