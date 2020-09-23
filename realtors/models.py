from django.db import models
from datetime import datetime

class Realtor(models.Model):
    id = models.AutoField(primary_key=True, )
    name = models.CharField(max_length=200)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(blank=True)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=20)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateField(default=datetime.now, blank=True)
    def __str__(self):
        return self.name
