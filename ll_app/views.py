# ll_app/views.py
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt  # TEMPORARY, REMOVE LATER
from .models import BusinessSignup, ConsumerSignup
from django.contrib import messages
import logging

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

def home(request):
    return render(request, 'home.html') 

def home2(request):
    return render(request, 'home2.html')

def product_page(request):
    return render(request, 'product_page.html')


logger = logging.getLogger(__name__)

@csrf_exempt  # REMOVE THIS IN PRODUCTION!
def consumer_signup(request):
    if request.method == "POST":
        logger.info("Received POST request: %s", request.POST)

        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('sign_up2')

        try:
            ConsumerSignup.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                mobile=mobile,
                password=password
            )
            logger.info("Consumer saved to database: %s", email)
        except Exception as e:
            logger.error("Database error: %s", e)
            messages.error(request, "Error saving data. Try again.")

        return redirect('sign_in')

    return render(request, "sign_up2.html")


logger = logging.getLogger(__name__)

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import BusinessSignup  # Ensure you have imported the correct model
from django.contrib.auth.hashers import make_password

from django.shortcuts import render, redirect
from .models import ConsumerSignup, BusinessSignup
from django.contrib import messages

def business_signup_step1(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect("sign_up3")

        # Store in session temporarily
        request.session["email"] = email
        request.session["password"] = password

        return redirect("sign_up4")  # Redirect to Step 2

    return render(request, "sign_up3.html")



def business_signup_step2(request):
    if request.method == "POST":
        business_name = request.POST.get("business_name")
        region = request.POST.get("region")
        business_id = request.POST.get("business_id")
        mobile = request.POST.get("mobile")

        # Retrieve session data
        email = request.session.get("email")
        password = request.session.get("password")

        # Check if session data exists
        if not email or not password:
            messages.error(request, "Session expired. Please start over.")
            return redirect("sign_up3")

        # Save to database
        business = BusinessSignup(
            business_name=business_name,
            region=region,
            business_id=business_id,
            email=email,
            mobile=mobile,
            password=password  # Store hashed passwords in production
        )
        business.save()

        # Clear session data
        del request.session["email"]
        del request.session["password"]

        messages.success(request, "Business registered successfully!")
        return redirect("sign_in")  # Redirect to home or login

    return render(request, "sign_up4.html")

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ConsumerSignup, BusinessSignup
from django.contrib.auth.hashers import check_password

def sign_in(request):
    if request.method == "POST":
        email_or_mobile = request.POST.get("email")
        password = request.POST.get("password")

        # Check if user is a Consumer
        consumer = ConsumerSignup.objects.filter(email=email_or_mobile).first() or \
                   ConsumerSignup.objects.filter(mobile=email_or_mobile).first()

        if consumer and consumer.password == password:  # Replace with hashed password check in production
            request.session["user_type"] = "consumer"
            request.session["user_id"] = consumer.id
            request.session["user_name"] = consumer.first_name
            messages.success(request, "Consumer signed in successfully!")
            return redirect("home")  # Redirect to consumer dashboard

        # Check if user is a Business
        business = BusinessSignup.objects.filter(email=email_or_mobile).first() or \
                   BusinessSignup.objects.filter(mobile=email_or_mobile).first()

        if business and business.password == password:  # Replace with hashed password check in production
            request.session["user_type"] = "business"
            request.session["user_id"] = business.id
            request.session["user_name"] = business.business_name
            messages.success(request, "Business signed in successfully!")
            return redirect("home2")  # Redirect to business dashboard

        # If credentials don't match
        messages.error(request, "Invalid email/mobile or password.")
        return redirect("sign_in")

    return render(request, "sign_in.html")

def sign_out(request):
    request.session.flush()  # Clear all session data
    messages.success(request, "You have signed out successfully!")
    return redirect("sign_in")
