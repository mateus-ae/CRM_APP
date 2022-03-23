from django import forms
from .models import Customer

class DateInput(forms.DateInput):
    input_type = "date"


class CustomerForm(forms.ModelForm):
    first_name = forms.CharField(label="Name", error_messages={"max_length": "Name can't have more than 30 characters"})
    last_name = forms.CharField()
    email = forms.EmailField(label="E-mail")
    birth_date = forms.DateField(widget=DateInput())
    area_code = forms.RegexField(regex=r"^[0-9]{2}$", error_messages={"invalid": "Invalid Area Code"})
    phone_number = forms.RegexField(regex=r"^[0-9]{9,15}$", error_messages={"invalid": "Invalid Phone Number"})
    country = forms.CharField()
    state = forms.CharField()
    city = forms.CharField()

    class Meta:
        model = Customer
        fields = (
            "first_name",
            "last_name",
            "email",
            "birth_date",
            "area_code",
            "phone_number",
            "country",
            "state",
            "city"
        )