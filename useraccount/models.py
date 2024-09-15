from django.db import models
from django.contrib.auth.models import User
# Create your models here.
GENDER_TYPE =(
    ("MALE","MALE"),
    ("FEMALE","FEMALE"),
)
class user_account(models.Model):
    user = models.OneToOneField(User, related_name="account", on_delete=models.CASCADE)
    birth_date = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_TYPE)
    balance = models.DecimalField(default=0, max_digits=12, decimal_places=2)

    def __str__(self):
        return self.user.username

class user_address(models.Model):
    user = models.OneToOneField(User, related_name="addresses", on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    postal_code = models.IntegerField()
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username} - {self.user.email}"

