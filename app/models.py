from django.db import models

# Create your models here.
class Employee(models.Model):
    Emp_Name=models.CharField(max_length=20)
    Emp_Id=models.IntegerField()
    Designation=models.CharField(max_length=20)
    Date_of_Joining=models.DateField()
    Department=models.CharField(max_length=25)
    Salary_Package=models.DecimalField(max_digits=10, decimal_places=2)
    Experience=models.FloatField()

class News(models.Model):
    Occation = models.TextField(max_length=100)

class Holiday(models.Model):
    Date=models.DateField()
    Occation=models.TextField(max_length=100)
