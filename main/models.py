from django.db import models

# Create your models here.
class websites(models.Model):
    website_address = models.CharField(max_length=255)
    time_interval = models.IntegerField()
    verify_string = models.CharField(max_length=1000)

class connection_log(models.Model):
    website_address = models.CharField(max_length=255)
    status = models.CharField(max_length=150)
    response_Time = models.CharField(max_length=50)
    checked = models.BooleanField(default=True)
    datetime_check = models.DateTimeField(auto_now_add=True)
