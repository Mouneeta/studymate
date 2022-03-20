from django.urls import path
from . import views 

urlpatterns = [
    path('see/',views.getData),
    path('add/', views.addData),
]