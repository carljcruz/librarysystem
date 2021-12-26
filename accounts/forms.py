from django.contrib.auth.forms import UserCreationForm
from django.forms.models import ModelForm

from accounts.models import Employee, MyUser

class UserCreateForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = [
            "email", "password1", "password2"
        ]

class EmployeeForm(ModelForm):  # Employee form for registration
    """ Added an extra field for department for employee registration"""
    class Meta:
        model = Employee
        fields = ('department',)

