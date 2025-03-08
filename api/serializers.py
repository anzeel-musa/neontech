from rest_framework import serializers
from.models import *

class TechncianSerializers(serializers.ModelSerializer):
    class Meta:
        model=Technician
        fields=['id','first_name','last_name','profile_pic','address','mobile','status']

class CustomerSerializers(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields=['id',
                'image',
                'first_name',
                'last_name',
                'address',
                'mobile',
                'status']
        
class AppointmentSerializers(serializers.ModelSerializer):
    class Meta:
        model=Appointment
        fields=['customerId',
                'assignedTechnicianId',
                'customerName',
                'appointmentDate',
                'imei',
                'device',
                'symptoms',
                'status']
        
class DeviceDischargeDetailsSerializers(serializers.ModelSerializer):
    class Meta:
        model=DeviceDischargeDetails
        fields=['customerId',
                'assignedTechnicianId',
                'appointmentId',
                'releaseDate',
                'daySpent',
                'storageCharge',
                'repairCost','technicianFee','OtherCharge','total']
        
        
        
        
