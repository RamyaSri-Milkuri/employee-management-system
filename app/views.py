from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from app.form import EmployeeForm,NewsForm,HolidayForm
from app.models import Employee,News,Holiday
import csv
from django.http import HttpResponse

# Create your views here.

def home(request):
	return render(request,'app/home.html')

@login_required
def manager(request):
	return render(request,'app/manager.html')

def employee(request):
	return render(request,'app/employee.html')

def addemp(request):
	form=EmployeeForm()
	if request.method=='POST':
		form=EmployeeForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/empdata')
	return render(request,'app/addemp.html',{'form':form})

def empdata(request):
	e=Employee.objects.all()
	return render(request,'app/empdata.html',{'e':e})

def select(request):
	return render(request,'app/select.html')

def delete(request,id):
	e=Employee.objects.get(id=id)
	e.delete()
	return redirect('/empdata')

def update(request,id):
	e=Employee.objects.get(id=id)
	if request.method=='POST':
		form=EmployeeForm(request.POST, instance=e)
		if form.is_valid():
			form.save()
			return redirect('/empdata')
	return render(request,'app/select.html',{'e':e})


def getfile(request):
	response = HttpResponse(content_type='text/csv')
	response['Content-Desposition'] = 'attachment; filename="edata.csv"'
	employee = Employee.objects.all()
	writer = csv.writer(response)
	writer.writerow(['EMP_NAME','EMP_ID','DESIGNATION','DATE_OF_JOINING','DEPARTMENT','SALARY_PACKAGE','EXPERIENCE'])
	for i in employee:
		writer.writerow([i.Emp_Name,i.Emp_Id,i.Designation,i.Date_of_Joining,i.Department,i.Salary_Package,i.Experience])
	return response

def addnews(request):
	form=NewsForm()
	if request.method=="POST":
		form=NewsForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/latestnews')
	return render(request,'app/addnews.html',{'form':form})

def latestnews(request):
	n=News.objects.all()
	return render(request,'app/latestnews.html',{'n':n})

def addholiday(request):
	form=HolidayForm()
	if request.method=="POST":
		form=HolidayForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/holycalender')
	return render(request,'app/addholiday.html',{'form':form})

def holycalender(request):
	h=Holiday.objects.all()
	return render(request,'app/holycalender.html',{'h':h})