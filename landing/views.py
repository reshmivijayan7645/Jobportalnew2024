from django.shortcuts import render, redirect

def landingPage(req):
    return render(req, 'home.html')
