from typing import Any
from django.db import models

# Create your models here.
class school(models.Model):
    schoolName=models.CharField(max_length=100,primary_key=True)
    principal=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    def __str__(self):
        return self.schoolName

class student(models.Model):
    schoolName=models.ForeignKey(school,on_delete=models.CASCADE)
    studentName=models.CharField(max_length=100)
    studentID=models.IntegerField(primary_key=True)
    def __str__(self) :
        return self.studentName