from django.db import models
#
# # Create your models here.
from django.db import models
class Task(models.Model):
    name=models.CharField(max_length=250)
    dob=models.DateField()
    age=models.CharField(max_length=100)
    gender=models.CharField(max_length=30)
    phonenumber=models.IntegerField()
    email=models.EmailField(max_length=250)
    address=models.CharField(max_length=500)
    district=models.CharField(max_length=250)
    branch=models.CharField(max_length=250)
    acc_type=models.CharField(max_length=250)
    material=models.CharField(max_length=250)
    def __str__(self):
        return self.name

# Create your models here.


