from django.http.response import HttpResponseBadRequest
from django.shortcuts import redirect, render
from accounts.forms import EmployeeForm
from accounts.admin import UserCreationForm
from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


User = get_user_model()


@login_required(login_url='employee-login')
def home_view(request):
    return render(request, 'home.html', context=None)


def create_user(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        employee_form = EmployeeForm(request.POST)
        if user_form.is_valid() and employee_form.is_valid():
            user = user_form.save()
            employee = employee_form.save(commit=False)
            employee.user = user
            employee.save()
            login(request, user)
            return redirect(login_user)
    else:
        user_form = UserCreationForm()
        employee_form = EmployeeForm()
    context = {
        'user_form': user_form,
        'employee_form': employee_form
    }

    return render(request, 'emp_signup.html', context=context)


# login function
def login_user(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(home_view)
    else:
        HttpResponseBadRequest()
        print('Not allowed')
    return render(request, 'login.html', context=None)


def logout_user(request):
    logout(request)
    return redirect(login_user)
