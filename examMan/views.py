from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from examMan.models import examMan
from .serializers import examManSerializer

@api_view(['GET'])
def getData(request):
    examMans = examMan.objects.all()
    serializer = examManSerializer(examMans, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def addData(request):
    serializer = examManSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
