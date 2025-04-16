from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('home2/', views.home2, name='home2'),
    path('product_page/', views.product_page, name='product_page'),

    path('sign_in/', views.sign_in, name='sign_in'),
    path('sign_up1/', views.sign_up1, name='sign_up1'),
    path('sign_up2/', views.sign_up2, name='sign_up2'),
    path('sign_up3/', views.sign_up3, name='sign_up3'),
    path('sign_up4/', views.sign_up4, name='sign_up4'),

    # Handle consumer signup
    path('consumer_signup/', views.consumer_signup, name='consumer_signup'),

    # Handle business signup in two steps
    path('business_signup_step1/', views.business_signup_step1, name='business_signup_step1'),
    path('business_signup_step2/', views.business_signup_step2, name='business_signup_step2'),
    
    path('add_product/', views.add_product, name='add_product'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
