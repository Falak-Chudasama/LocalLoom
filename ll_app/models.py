from djongo import models

class ConsumerSignup(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=100)  # Store hashed passwords in production

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class BusinessSignup(models.Model):
    business_name = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    business_id = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=100)  # Store hashed passwords in production

    def __str__(self):
        return self.business_name

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField(blank=True)  # This will store the image URL
    length = models.CharField(max_length=100)
    width = models.CharField(max_length=100)
    height = models.CharField(max_length=100)
    weight = models.CharField(max_length=100)
    features = models.JSONField(default=list)  # Storing features as a list
    state = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    description = models.TextField()
    details = models.TextField()

    def __str__(self):
        return self.product_name