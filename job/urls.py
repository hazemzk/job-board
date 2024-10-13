from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('<int:title>', views.job_ditail, name='job ditail'),
    
]
