from django import forms
from app.models import Employee,News,Holiday

class EmployeeForm(forms.ModelForm):
	class Meta:
		model=Employee
		fields='__all__'

class NewsForm(forms.ModelForm):
	class Meta:
		model=News
		fields='__all__'

class HolidayForm(forms.ModelForm):
	class Meta:
		model=Holiday
		fields='__all__'

