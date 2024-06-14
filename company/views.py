from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import *
from .models import Company
from .models import Jobs

def list_company(req):
    return render(req, 'index.html')

def company_job_view(request):
    company = request.user.company  # Assuming request.user.company gives the company associated with the current user
    jobs = Jobs.objects.filter(company=company)
    return render(request, "job.html", {'jobs': jobs})


def view_application(req):
    company = req.user.company
    jobs = Jobs.objects.filter(company=company)
    return render(req, "publicList_with_applications.html", {'jobs': jobs})

    
    

def remove_job(request, job_id):
    try:
        job = Jobs.objects.get(pk=job_id)
        job.delete()
        return redirect('job')
    except Jobs.DoesNotExist:
        pass
    return redirect('job')


def add_job(request):
    if request.method == 'POST':
        print(request.POST)
        form = JobForm(request.POST)
        print(form)
        if form.is_valid():
            job = form.save(commit=False)
            job.company = request.user.company
            form.save()
            # Redirect to the jobs page or another appropriate page
            return redirect('job')
    else:
        form = JobForm()
    return render(request, 'add_job.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(username, password)
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                # Redirect to a success page or the desired URL
                return redirect('job')
            else:
                # Invalid login
                return render(request, 'index.html', {'form': form, 'error': 'Invalid username or password.'})
    else:
        form = LoginForm()
    return render(request, 'index.html', {'form': form})
   


