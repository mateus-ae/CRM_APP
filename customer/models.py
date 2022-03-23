from django.db import models
from django.urls import reverse

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    birth_date = models.DateField()
    area_code = models.CharField(max_length=3)
    phone_number = models.CharField(max_length=9)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_full_phone_number(self):
        return f"({self.area_code}) {self.phone_number[:5]}-{self.phone_number[5:]}"

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_city_and_state(self):
        return f"{self.city} - {self.state}"

    def get_absolute_url(self):
        return reverse("customer:customer-update", kwargs={"id": self.id})

    def get_delete_url(self):
        return reverse("customer:customer-delete", kwargs={"id": self.id})

    class Meta:
        # If this class is not used, the created table on the database would be stored as nameOfApp_nameOfTable,
        # in this case customer_customer. But By using it, I can specify the name of the table, in this case customer
        db_table = "customer"

    # Now run "python manage.py makemigrations customer" to create a migration file (0001_initial) and the run
    # "python manage.py migrate" to create the table in the database.
