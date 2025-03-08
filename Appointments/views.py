from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect,reverse
#from . import forms
from api.models import Technician
from django.db.models import Sum
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required,user_passes_test
from api.models import Message
from django.contrib.auth.models import User
from datetime import datetime,timedelta,date
from django.contrib import messages
from django.conf import settings
from django.db.models import Q

# Create your views here.
def home_view(request):
        
    return render(request,'commons/index.html')



from api import models
import requests
#admin dashboard
# @login_required(login_url='adminlogin')
# @user_passes_test(is_admin)
def admin_dashboard_view(request):
    #for both table in admin dashboard
    Technician = f'http://127.0.0.1:8000/api/technicians/'
    
    response = requests.get(Technician)
    
    data = response.json()
    TotalTechnicians = data['TotalTechnicians']
    print(TotalTechnicians)
    #Technician=models.Technician.objects.all().order_by('-id')
    Customer=models.Customer.objects.all().order_by('-id')
    #for three cards
    techniciancount=models.Technician.objects.all().filter(status=True).count()
    pendingtechniciancount=models.Technician.objects.all().filter(status=False).count()

    customercount=models.Customer.objects.all().filter(status=True).count()
    pendingcustomercount=models.Customer.objects.all().filter(status=False).count()

    appointmentcount=models.Appointment.objects.all().filter(status=True).count()
    pendingappointmentcount=models.Appointment.objects.all().filter(status=False).count()
    mydict={
    #'Technician':Technician,
    'TotalTechnicians':TotalTechnicians,
    'Customer':Customer,
    'techniciancount':techniciancount,
    'pendingtechniciancount':pendingtechniciancount,
    'customercount':customercount,
    'pendingcustomercount':pendingcustomercount,
    'appointmentcount':appointmentcount,
    'pendingappointmentcount':pendingappointmentcount,
    }
    return render(request,'adminn/dashboard.html',context=mydict)


# @login_required(login_url='technicianlogin')
# @user_passes_test(is_technician)
def technician_dashboard_view(request):
    #for three cards
    customercount=models.Customer.objects.all().filter(status=True,assignedTechnicianId=request.user.id).count()
    appointmentcount=models.Appointment.objects.all().filter(status=True,assignedTechnicianId=request.user.id).count()
    customerdischarged=models.DeviceDischargeDetails.objects.all().distinct().filter(assignedTechnicianName=request.user.id).count()

    #for  table in technician dashboard
    appointments=models.Appointment.objects.all().filter(status=True,assignedTechnicianId=request.user.id).order_by('-id')
    customers=models.Customer.objects.all().filter(status=True,assignedTechnicianId=request.user.id).order_by('-id')
    mydict={
    'customers':customers,
    'customercount':customercount,
    'appointmentcount':appointmentcount,
    'customerdischarged':customerdischarged,
    'appointments':appointments,
    'technician':models.Technician.objects.get(user_id=request.user.id), #for profile picture of doctor in sidebar
    }
    return render(request,'technician/dashboard.html',context=mydict)


#@login_required(login_url='customerlogin')
#@user_passes_test(is_customer)
def customer_dashboard_view(request):
    customer=models.Customer.objects.get(user_id=request.user.id)
    appointment=models.Appointment.objects.get(customerId=customer)
    print(appointment.symptoms)
    technician=models.Technician.objects.get(user_id=customer.assignedTechnicianId.user)
    mydict={
    'customer':customer,
    'technicianName':technician.get_name,
    'technicianMobile':technician.mobile,
    'technicanaddress':technician.address,
    'symptoms':appointment.symptoms,
    'admitDate':appointment.appointmentDate,
    }
    return render(request,'customer/dashboard.html',context=mydict)



#inquiry section
def aboutus_view(request):
    return render(request,'commons/aboutus.html')


#chat
@login_required
def send_message(request, username):
    if request.method == 'POST':
        recipient = User.objects.get(username=username)
        content = request.POST.get('content')
        message = Message.objects.create(sender=request.user, recipient=recipient, content=content)
        messages.success(request, "Your inquiry was sent successfully, You will receive a response soon")
        return redirect('conversation', username=username)
    messages.error(request, "Something Went Wrong")
    return render(request, 'commons/send_message.html')


@login_required
def view_conversation(request, username):
    recipient = User.objects.get(username=username)
    messages = Message.objects.filter(sender=request.user, recipient=recipient) | Message.objects.filter(sender=recipient, recipient=request.user).order_by('-timestamp')
    return render(request, 'commons/view_conversation.html', {'recipient': recipient, 'messages': messages})



def delete_message(request, message_id):
    message = Message.objects.get(id=message_id)
    message.delete()
    return redirect('conversation', username=message.recipient.username)