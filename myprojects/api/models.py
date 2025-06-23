
from django.db import models

class Student(models.Model):
    StudentID = models.AutoField(primary_key=True)
    StudentName = models.CharField(max_length=100)
    Gender = models.CharField(max_length=10)
    DoB = models.DateField()
    PhoneNumber = models.CharField(max_length=15)
    Email = models.EmailField()

    def __str__(self):
        return self.StudentName
