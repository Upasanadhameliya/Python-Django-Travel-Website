from django.db import models

# Create your models here.
class Destination(models.Model):
     name = models.CharField(max_length = 100,default='')
     img = models.ImageField(upload_to = 'pics',default='')
     desc = models.TextField(default='This place is gorgeous')
     price = models.IntegerField(default=100)
     offer = models.BooleanField(default=False)
     
     def __str__(self):
          return self.name