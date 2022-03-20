from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from studyMat.models import studyMat
from .serializers import studyMatSerializer

@api_view(['GET'])
def getData(request):
    studyMats = studyMat.objects.all()
    serializer = studyMatSerializer(studyMats, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def addData(request):
    serializer = studyMatSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

