from django.shortcuts import render
from django.http import HttpResponse
####
from .models import *
from django.http import JsonResponse
from rest_framework.response import Response
from customer.serializers import *
#from serializers import *
from .serializers import CustomerSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
# Create your views here.

@api_view(['GET','POST'])
def welcome_customer(request):
    return render(request, 'welcome.html', {'name':'Maria'})
@api_view(['GET', 'POST'])
def CustomerDataJsonFun(request, format=None):
    if request.method =='GET':
        # customer = Customer.objects.all()
        # serializer = CustomerSerializer(customer, many = True)
        # return Response(serializer.data, status=status.HTTP_200_OK)
        alldata = Customer.objects.all()
        data = {
            'alldata':list(alldata.values())
        }        
        return Response(data,status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = CustomerSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET','PUT','DELETE'])
def customer_by_id(request, id,format=None):
    
    try:
        customer = Customer.objects.get(pk=id)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CustomerSerializer(customer, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
 
    elif request.method == 'DELETE':
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)