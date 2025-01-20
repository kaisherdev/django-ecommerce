from django.forms import ModelForm
from .models import Account

# create the form class.
class RegistrationForm(ModelForm):
    class Meta:
        model = Account
        fields = ['first_name','last_name','phone_number','email','password']