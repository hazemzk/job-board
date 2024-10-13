from django.shortcuts import render

# Create your views here.
def job_list(request):
    render(request, render(request, 'jobs.html'))

def job_ditail(request):
    render(request, render(request, 'job_ditails.html'))