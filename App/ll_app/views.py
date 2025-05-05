# ll_app/views.py
from django.conf import settings
from django.http import Http404, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt  # TEMPORARY, REMOVE LATER
from .models import BusinessSignup, ConsumerSignup
from django.contrib import messages
import logging
from django.contrib.auth import logout
from bson import ObjectId 

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
    products = Product.objects.all() 
    for p in products:
        p.id = str(p._id)
    return render(request, 'home.html', {'products': products})

def home2(request):
    return render(request, 'home2.html')

def product_page(request, product_id):
    product = get_object_or_404(Product, _id=ObjectId(product_id))
    return render(request, 'product_page.html', {'product': product})


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

        return redirect('home')

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

    return render(request, "home2.html")

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

def add_product(request):
    return render(request, 'add_product.html')

from .models import Product
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.conf import settings

def add_product(request):
    if request.method == 'POST':
        # Get the POST data from the form
        product_name = request.POST.get('productname')
        cost = request.POST.get('cost')
        length = request.POST.get('length')
        width = request.POST.get('width')
        height = request.POST.get('height')
        weight = request.POST.get('weight')
        feature = request.POST.get('feature')  # Assuming features will be added manually
        state = request.POST.get('state')
        region = request.POST.get('region')
        description = request.POST.get('description')
        details = request.POST.get('details')

        # Handle the image upload
        product_image = request.FILES.get('productimage')
        image_url = None
        if product_image:
            fs = FileSystemStorage(location=settings.MEDIA_ROOT)  # Ensure saving to media folder
            filename = fs.save(product_image.name, product_image)
            image_url = fs.url(filename)  # This will give the correct URL to access the image

        # Saving the product to the database
        try:
            product = Product(
                product_name=product_name,
                cost=cost,
                image_url=image_url,
                length=length,
                width=width,
                height=height,
                weight=weight,
                features=[feature],  # Assuming single feature for simplicity
                state=state,
                region=region,
                description=description,
                details=details
            )
            product.save()

            # Return a success response
            response_data = {
                'success': True,
                'message': 'Product added successfully',
            }
        except Exception as e:
            # If there's an error saving the product
            response_data = {
                'success': False,
                'message': f'Failed to add product. Error: {str(e)}',
            }

        return JsonResponse(response_data)

    return render(request, 'add_product.html')


from django.http import JsonResponse
from django.shortcuts import render
from .models import Product

def dashboard_view(request):
    products = Product.objects.all()
    
    if request.headers.get('x-requested-with') == 'XMLHttpRequest' or request.GET.get('format') == 'json':
        try:
            data = [
                {'id': str(product._id), 'name': product.product_name}
                for product in products
            ]
            return JsonResponse({'products': data})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return render(request, 'dashboard.html', {'products': products})

from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Order
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def place_order(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, _id=product_id)
        user = request.user  # or get ConsumerSignup object if different

        address = request.POST.get('address')
        quantity = int(request.POST.get('quantity', 1))
        payment_mode = request.POST.get('payment_mode')
        cost = product.price * quantity  # assuming 'price' field exists

        Order.objects.create(
            user=user,
            product=product,
            address=address,
            cost=cost,
            quantity=quantity,
            payment_mode=payment_mode
        )

        messages.success(request, "Order placed successfully!")
        return redirect('order_success_page')

    return redirect('product_detail', product_id=product_id)  # fallback for GET

def order_success(request):
    return render(request, 'order_success.html')  # make this template



