from django.shortcuts import render
from .serializers import RoomSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from django.http import HttpResponse

# Create your views here.
@api_view(['GET','PUT','POST','DELETE'])
def view_rooms(request):
    if request.method == 'GET':
        roomdata = Room.objects.all()
        data = {
            'roomdata':list(roomdata.values())
        }
        return Response(data, status=status.HTTP_200_OK)
    elif request.method =='POST':
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','PUT','DELETE'])
def view_rooms_by_id(request, id):
        try:
            room = Room.objects.get(pk=id)
        except Room.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        if request.method == 'GET':
            serializer = RoomSerializer(room)
            return Response(serializer.data)
        elif request.method =='PUT':
            serializer = RoomSerializer(room, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        elif request == 'DELETE':
            room.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)