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
