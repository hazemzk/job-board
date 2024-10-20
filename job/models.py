from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
# Create your models here.

JOB_TYPE={
    ('Full time','Full time'),
    ('Part time','Part time'),
}
class Job(models.Model):
    owner=models.ForeignKey(User, related_name='job_owner', on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    location=models.CharField(max_length=50)
    job_type=models.CharField(max_length=15, choices=JOB_TYPE)
    description=models.TextField(max_length=1000)
    published_at=models.DateTimeField(auto_now=True)
    Vacancy=models.IntegerField(default=1)
    salary=models.IntegerField(default=0)
    category=models.ForeignKey("Category", on_delete=models.CASCADE)
    experience =models.IntegerField()
    image = models.ImageField(upload_to='jobs/' , blank=True, null=True) 

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Job, self).save(*args, **kwargs)
    
    slug=models.SlugField(null=True, blank=True )

    
    def __str__(self):
        return self.title
    
    
class Category(models.Model):
    name=models.CharField(max_length=25)
    
    def __str__(self):
        return self.name
    
    
    
class Apply(models.Model):
    job = models.ForeignKey(Job, related_name='apply_job', on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=254)
    link=models.URLField()
    cv=models.FileField(upload_to=None, max_length=100)
    cover_letter = models.TextField(max_length=1500)
    applied_at=models.DateTimeField(auto_now=True)
   
    def __str__(self):
        return self.name