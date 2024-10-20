from django.shortcuts import render , redirect
from django.urls import reverse
from .models import *
from django.core.paginator import Paginator
from .forms import ApplyForm , AddJob
from django.contrib.auth.decorators import login_required
from .filters import JobFilter
# Create your views here.


def job_list(request):
    jobs=Job.objects.all()
    # filters
    myfilter=JobFilter(request.GET,  queryset=jobs)
    jobs = myfilter.qs
    
    
    paginator = Paginator(jobs, 12)  
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    context={"jobs":page_obj, 'filter':myfilter}
    
    
    return render(request, 'job/job_list.html', context)

def job_ditail(request, slug):
    ditail=Job.objects.get(slug=slug)
    
    if request.method=='POST':
       
        form= ApplyForm(request.POST , request.FILES)
       
        if form.is_valid():
            myform=form.save(commit=False)
            myform.job=ditail
            myform.save()
            
    
    
    else:
        form=ApplyForm()
    context={"job":ditail, 'form':form}
    return render(request, 'job/job_ditail.html', context)

@login_required
def add_job(request):
    
    if request.method=='POST':
       
        form= AddJob(request.POST , request.FILES)
       
        if form.is_valid():
            myform=form.save(commit=False)
            myform.owner= request.user
            myform.save()
            return redirect(reverse('jobs:job_list'))
            
    else:
        form=AddJob()
    
    context={"form":form}
    return render(request,  'job/add_job.html', context)
