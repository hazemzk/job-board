from django import forms
from .models import *

class ApplyForm(forms.ModelForm):
    class Meta:
        model=Apply
        fields = ['name', 'email', 'link', 'cv', 'cover_letter']
        
        
        
class AddJob(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'location', 'salary', 'job_type', 'category', 'experience', 'Vacancy', 'image', 'description']
        