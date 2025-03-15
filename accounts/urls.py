from django.urls import path
from accounts.views import *
urlpatterns = [
    
    path("verify-email/<email>", verify_email, name="verify-email"),
    path("resend-otp", resend_otp, name="resend-otp"),

]