from django import forms
from .models import Empolyee

# class EmployeeForm

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Empolyee
        fields = '__all__'