from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.db import models


# Create your models here.



class Setting(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    phone = models.CharField(max_length=255)
    skills = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(Setting, self).save(*args, **kwargs)

class Projects(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    author = models.ForeignKey(Setting, on_delete=models.CASCADE)
    url = models.URLField(max_length=255, blank=True)
    created_at = models.DateField(auto_now_add=False)


    def __str__(self):
        return self.title



class AdminProject(models.Model):
    admin = models.ForeignKey(Setting, on_delete=models.CASCADE)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('admin', 'project')



class Comments(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=255)
    comment = models.TextField()