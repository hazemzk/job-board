from django.db import models

# Create your models here.

JOB_TYPE={
    ('Full time','Full time'),
    ('Part time','Part time'),
}

class Job(models.Model):
    title=models.CharField(max_length=100)
    # location=models.CharField(max_length=50)
    job_type=models.CharField(max_length=15, choices=JOB_TYPE)
    description=models.TextField(max_length=1000)
    published_at=models.DateTimeField(auto_now=True)
    Vacancy=models.IntegerField(default=1)
    salary=models.IntegerField(default=0)
    category=models.ForeignKey("Category", on_delete=models.CASCADE)
    experience =models.IntegerField()
    
    def __str__(self):
        return self.title
    
    
class Category(models.Model):
    name=models.CharField(max_length=25)
    
    def __str__(self):
        return self.name