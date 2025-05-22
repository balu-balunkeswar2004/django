from django.db import models

# Create your models here.
class Employee(models.Model):
  empid = models.IntegerField(primary_key = True)
  ename = models.CharField(max_length=50)
  password = models.CharField(max_length=50)
  pno = models.CharField(max_length=50)
  email = models.CharField(max_length=50)
  add = models.TextField(max_length=100)
  gender = models.CharField(max_length=10)
  
  def __str__(self):
    return self.ename