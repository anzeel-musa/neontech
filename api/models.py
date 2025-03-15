from django.db import models

# Create your models here.
from django.db import models
from accounts.models import User


DEVICE_TYPE = [
    ('Phone', 'Phone'),
    ('Laptop', 'Laptop'),
    ('Desktop', 'Desktop'),    
]

class Technician(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    profile_pic= models.ImageField(upload_to='profile_pic/TechProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.IntegerField()
    is_free=models.BooleanField(default=False)
    status=models.BooleanField(default=False)
    
    

    @property
    def get_name(self):
        return self.user.first_name + ''+ self.user.first_name
    @property
    def get_id(self):
        return self.user.id
    def _str_(self):
        return self.user.first_name + ' ' + self.user.last_name + ' location:'+ ' ' + self.address



class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE, null=True, blank=True)
    assignedTechnicianId=models.ForeignKey(Technician, verbose_name='Technician name', on_delete=models.CASCADE)
    image= models.ImageField(upload_to='images/',null=True,blank=True)
    first_name= models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    status=models.BooleanField(default=False)
    
    @property
    def get_name(self):
        return self.first_name+" "+self.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.first_name + " " +self.last_name


class Appointment(models.Model):
    customerId=models.ForeignKey(Customer, verbose_name='Customer name', on_delete=models.DO_NOTHING)
    assignedTechnicianId = models.ForeignKey(Technician, verbose_name='Technician name', on_delete=models.CASCADE)
    appointmentDate=models.DateTimeField(auto_now_add=True)
    imei = models.CharField(max_length=200,null=False)
    device = models.CharField(max_length=200,null=False, choices=DEVICE_TYPE)
    symptoms = models.CharField(max_length=100)
    description = models.TextField(max_length=500,null=True,blank=True)
    status=models.BooleanField(default=False)
    
    @property
    def get_id(self):
        return self.user.id




class DeviceDischargeDetails(models.Model):
    customerId=models.ForeignKey(Customer, verbose_name="Customer name", on_delete=models.DO_NOTHING)
    assignedTechnicianName=models.ForeignKey(Technician, verbose_name="Technician name", on_delete=models.DO_NOTHING)
    appointmentId=models.ForeignKey(Appointment,on_delete=models.DO_NOTHING)
    
    releaseDate=models.DateField(null=False)
    daySpent=models.PositiveIntegerField(null=False)

    storageCharge=models.PositiveIntegerField(null=False)
    repairCost=models.PositiveIntegerField(null=False)
    technicianFee=models.PositiveIntegerField(null=False)
    OtherCharge=models.PositiveIntegerField(null=False)
    total=models.PositiveIntegerField(null=False)
   
    
    class Meta:
        verbose_name_plural = "Device Discharge Details"
        ordering = ['-releaseDate']
    def _str_(self):
        return self.customerId + ": " + self.total
    
    
    

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)