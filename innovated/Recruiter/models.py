from pydoc import describe
from django.db import models

class ServiceCategory(models.Model):
    name=models.CharField(max_length=200)
    icon=models.ImageField(upload_to='category_icons/',blank=True,null=True)
    banner_image=models.ImageField(upload_to='category_banners/',blank=True,null=True)
    description=models.TextField(blank=True,null=True)
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class JobRole(models.Model):
    category=models.ForeignKey(ServiceCategory, on_delete=models.CASCADE ,related_name='roles') 
    
    role_name=models.CharField(max_length=200)
    image=models.ImageField(upload_to='job_roles/',blank=True,null=True)
    description=models.TextField(blank=True,null=True)
    hiring_type=models.CharField(max_length=200,choices=(('full_time','Full Time'),('part_time','Part Time'),('contract','Contract'),('internship','Internship')))
    experience=models.CharField(max_length=200,blank=True,help_text="0-1 years /2-5 years /5+ years")
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.role_name
    


   