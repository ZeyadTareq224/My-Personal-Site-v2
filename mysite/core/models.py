from django.db import models

# Create your models here.
class Resume(models.Model):
    resume = models.FileField(upload_to ='uploads/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    @property
    def get_resume_path(self):
        return self.resume.url



class Project(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='uploads/project_images/')
    github_link = models.URLField(max_length=255)
    demo_link = models.URLField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']

class Achievment(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='achievments')
    created_at = models.DateTimeField(auto_now_add=False)
    
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']


class Skill(models.Model):
    image = models.ImageField(upload_to='skills')
    name = models.CharField(max_length=50)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"

    ordering = ['-updated_at']