from django.shortcuts import render
from django.core.paginator import Paginator
from job.models import Job
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    jobs = Job.objects.all()
    
    # Paginate jobs with 12 jobs per page
    paginator = Paginator(jobs, 12)  
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    users = User.objects.all()  # Fetch all users
    
    context = {
        "jobs": page_obj, 
        'users': users, 
    }
    
    return render(request, 'home/home.html', context)
