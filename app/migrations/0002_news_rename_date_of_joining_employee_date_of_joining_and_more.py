# Generated by Django 5.0.2 on 2024-03-19 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Occation', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='Date_of_joining',
            new_name='Date_of_Joining',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='Emp_id',
            new_name='Emp_Id',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='Emp_name',
            new_name='Emp_Name',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='Salary_package',
            new_name='Salary_Package',
        ),
    ]
