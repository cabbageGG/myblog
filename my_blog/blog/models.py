from django.db import models

# Create your models here.

class Blog(models.Model):
    titile = models.CharField(max_length=32, default="Title")
    content = models.TextField(null=True)
    create_time = models.DateTimeField(null=True)


