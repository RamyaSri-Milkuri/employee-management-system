from django.contrib import admin
from app.models import Employee,News,Holiday

# Register your models here.

admin.site.register(Employee)
admin.site.register(News)
admin.site.register(Holiday)