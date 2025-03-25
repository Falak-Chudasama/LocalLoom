# ll_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('sign_in/', views.sign_in, name='sign_in'),
    path('sign_up1/', views.sign_up1, name='sign_up1'),
    path('sign_up2/', views.sign_up2, name='sign_up2'),
    path('sign_up3/', views.sign_up3, name='sign_up3'),
    path('sign_up4/', views.sign_up4, name='sign_up4'),
    
]