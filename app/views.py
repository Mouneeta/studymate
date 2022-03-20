from django.shortcuts import render, HttpResponse
from app.models import Task
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import TaskSerializer


def home(request):
    context = {'success': False, 'name': '  Mouneeta'}
    if request.method == "POST":
        title = request.POST['title']
        desc = request.POST['desc']
        print(title, desc)
        ins = Task(taskTitle=title, taskDesc=desc)
        ins.save()
        context = {'success': True}
    return render(request, 'index.html', context)
    #  return HttpResponse('works')


def about(request):
    allTask = Task.objects.all()
    context = {'tasks': allTask}
    print(allTask)
    return render(request, 'about.html', context)
    #  return HttpResponse('works')


@api_view(['GET'])
def getData(request):
    Tasks = Task.objects.all()
    serializer = TaskSerializer(Tasks, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addData(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
