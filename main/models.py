from django.db import models

# Create your models here.

class InputImage(models.Model):
    style_image=models.ImageField(upload_to='main/files/style')
    source_image=models.ImageField(upload_to='main/files/source')

class TestImage(models.Model):
    images=models.ImageField(upload_to='orpage/test')
    
class TestOutput(models.Model):
    out_images=models.ImageField(upload_to='orpage/result')
class OutputImage(models.Model):
    result_image=models.ImageField(upload_to='main/files/result',blank=True,null=True)
   