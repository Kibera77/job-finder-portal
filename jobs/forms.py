from django import forms
from django.forms import ModelForm
from .models import Employees


class EmployeeForm(ModelForm):
    class Meta:
        model = Employees
        fields = '__all__'


