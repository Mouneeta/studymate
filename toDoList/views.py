from django.shortcuts import render, HttpResponse


def home(request):
   return render(request,'index.html') 
   #  return HttpResponse('works')

def about(request):
   return render(request,'about.html') 
   #  return HttpResponse('works')

