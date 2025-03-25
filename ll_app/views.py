# ll_app/views.py
from django.shortcuts import render

def sign_in(request):
    return render(request, 'sign_in.html')

def sign_up1(request):
    return render(request, 'sign_up1.html')

def sign_up2(request):
    return render(request, 'sign_up2.html')

def sign_up3(request):
    return render(request, 'sign_up3.html')

def sign_up4(request):
    return render(request, 'sign_up4.html')