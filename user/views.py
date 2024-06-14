from django.shortcuts import render, redirect

from company.models import Jobs
from .form import *
from .models import *
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login,logout

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(username, password)
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                # Redirect to user dashboard or any other page after successful login
                return redirect('jlist')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})



def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Create a new User instance
            user = User.objects.create_user(username=form.cleaned_data['name'],
                                            email=form.cleaned_data['email'],
                                            password=form.cleaned_data['password'])

            # Create a new UserProfile instance associated with the created User instance
            profile = UserProfile.objects.create(user=user,
                                                 name=form.cleaned_data['name'],
                                                 qualification=form.cleaned_data['qualification'],
                                                 gender=form.cleaned_data['gender'],
                                                 phone=form.cleaned_data['phone'])
            messages.success(request, 'Registration successful. Please log in.')
            return redirect('user_login')  
    else:
        form = UserRegistrationForm()
    return render(request, 'reg.html', {'form': form})

def job_list(req):
    jobs = Jobs.objects.all()
    return render(req, "publicList.html", {'jobs': jobs, })

def apply_job(request, job_id):
    print(job_id)
    job = Jobs.objects.get(pk=job_id)
    user = request.user.email
    print(user)
    if not user in job.applied_users:
        job.applied_users.append(user)
    job.save()
    return redirect("jlist")


# def user_login(request):
#         if request.method == 'POST':
#             form = LoginForm(request.POST)
#             if form.is_valid():
#                 email = form.cleaned_data['email']
#                 password = form.cleaned_data['password']
#                 # Check if user with given email exists in the database
#                 try:
#                     user = User.objects.get(email=email)
#                 except User.DoesNotExist:
#                     user = None
#                 # If company exists and password matches, log in the company
#                 if user is not None and user.password == password:
#                     # Redirect to dashboard or another page
#                     return redirect('jlist')
#                 else:
#                     error_msg = "Invalid email or password."
#                     return render(request, 'login.html', {'form': form, 'error_msg': error_msg})
#         else:
#             form = LoginForm()
#         return render(request, 'login.html', {'form': form})


def user_profile(request):
    print("-----------------")
    user = request.user  # Assuming user is logged in and request.user contains the logged-in user object
    print("-----------------",user)
    return render(request, 'profile.html', {'user': user})

def user_logout(request):
    logout(request)
    return redirect('user_login')