from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=32, default="Title")
    content = models.TextField(null=True)
    summary = models.TextField(null=True)
    create_time = models.DateTimeField(null=True)
    def __unicode__(self):
        return self.title

class User(models.Model):
    name = models.CharField(max_length=32)
    head_img = models.ImageField(upload_to='head_img', null=True)
    account = models.CharField(max_length=32, null=True)
    passwd = models.CharField(max_length=32, null=True)
    def __unicode__(self):
        return self.name




