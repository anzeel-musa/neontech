from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

def technician_list(request, format=None):
    if request.method == 'GET':
        tech = Technician.objects.all()
        serializer = TechncianSerializers(tech, many=True)
        return JsonResponse({"status": "success", "TotalTechnicians": serializer.data}, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        serializer = TechncianSerializers (data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return JsonResponse({"error": serializer.errors}, status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PUT','DELETE','PATCH', 'HEAD', 'OPTIONS'])    
def technician_detail(request, pk, format=None):    
    if request.method == 'GET':
        try:
            tech = Technician.objects.get(pk=pk)
            serializer = TechncianSerializers(tech)
            return JsonResponse({"Technician": serializer.data})
        except Technician.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)
    
@api_view(['GET','PUT','DELETE'])  
def technician_detail(request, pk, format=None):    
    if request.method == 'GET':
        try:
            tech = Technician.objects.get(pk=pk)
            serializer = TechncianSerializers(tech)
            return JsonResponse({"Technician": serializer.data})
        except Technician.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)
        
    if request.method == 'PUT':
        try:
            tech = Technician.objects.get(pk=pk)
            serializer = TechncianSerializers(tech, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response({"error": serializer.errors}, status.HTTP_400_BAD_REQUEST)
        except Technician.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)
        
    if request.method == 'DELETE':
        try:
            tech = Technician.objects.get(pk=pk)
            tech.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Technician.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)

@api_view(['GET','POST'])
def customer_list(request, format=None):
    if request.method == 'GET':
        cust = Customer.objects.all()
        serializer = CustomerSerializers(cust, many=True)
        return JsonResponse({"status": "success", "TotalCustomers": serializer.data}, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        serializer = CustomerSerializers (data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response({"error": serializer.errors}, status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PUT','DELETE'])        
def customer_detail(request, pk, format=None):    
    if request.method == 'GET':
        try:
            cust = Customer.objects.get(pk=pk)
            serializer = CustomerSerializers(cust)
            return JsonResponse({"Customer": serializer.data})
        except Customer.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)
        
    if request.method == 'PUT':
        try:
            cust = Customer.objects.get(pk=pk)
            serializer = CustomerSerializers(cust, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response({"error": serializer.errors}, status.HTTP_400_BAD_REQUEST)
        except Customer.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)
        
    if request.method == 'DELETE':
        try:
            cust = Customer.objects.get(pk=pk)
            cust.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Customer.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)
        
def appointment_list(request, format=None):
    if request.method == 'GET':
        appoint = Appointment.objects.all()
        serializer = AppointmentSerializers(appoint, many=True)
        return JsonResponse({"status": "success", "TotalAppointments": serializer.data}, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        serializer = AppointmentSerializers (data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return JsonResponse({"error": serializer.errors}, status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET','PUT','DELETE'])        
def appointment_details(request, pk, format=None):    
    if request.method == 'GET':
        try:
            appoint = Appointment.objects.get(pk=pk)
            serializer = AppointmentSerializers(appoint)
            return JsonResponse({"Appointment": serializer.data})
        except Appointment.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)
        
    if request.method == 'PUT':
        try:
            appoint = Appointment.objects.get(pk=pk)
            serializer = AppointmentSerializers(appoint, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response({"error": serializer.errors}, status.HTTP_400_BAD_REQUEST)
        except Appointment.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)
        
    if request.method == 'DELETE':
        try:
            appoint = Appointment.objects.get(pk=pk)
            appoint.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Appointment.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)
        
def devicedischarge_list(request, format=None):
    if request.method == 'GET':
        ddd = DeviceDischargeDetails.objects.all()
        serializer = DeviceDischargeDetailsSerializers(ddd, many=True)
        return JsonResponse({"status": "success", "Totaldevices": serializer.data}, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        serializer = DeviceDischargeDetailsSerializers (data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return JsonResponse({"error": serializer.errors}, status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET','PUT','DELETE'])        
def devicedischarge_details(request, pk, format=None):    
    if request.method == 'GET':
        try:
            ddd = DeviceDischargeDetails.objects.get(pk=pk)
            serializer = DeviceDischargeDetailsSerializers(ddd)
            return JsonResponse({"DeviceDischargeDetails": serializer.data})
        except DeviceDischargeDetails.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)
        
    if request.method == 'PUT':
        try:
            ddd = DeviceDischargeDetails.objects.get(pk=pk)
            serializer = DeviceDischargeDetailsSerializers(ddd, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response({"error": serializer.errors}, status.HTTP_400_BAD_REQUEST)
        except DeviceDischargeDetails.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)
        
    if request.method == 'DELETE':
        try:
            ddd = DeviceDischargeDetails.objects.get(pk=pk)
            ddd.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except DeviceDischargeDetails.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)

