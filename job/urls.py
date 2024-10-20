from django.urls import path
from . import views
from . import api

app_name = 'job'

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('add_job', views.add_job, name='add_job'),
    path('<str:slug>', views.job_ditail, name='job_ditail'),

    #api
    path('api/jobs', api.job_list, name='job_list_api'),
    path('api/jobs/<str:slug>', api.job_ditail_api, name='job_ditail_api'),
    #class based views
    path('api/v2/jobs', api.JobListApi.as_view(), name='job_list_api'),
    path('api/v2/jobs/<str:slug>', api.JobDitail.as_view(), name='jobditail'),


]
