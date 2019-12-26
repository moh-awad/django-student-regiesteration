from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import Regiest_Form, Transaction
from django.contrib.auth.models import User
from django import forms
from django.utils import timezone

class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ("username", "email", "password1", "password2")
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super(UserCreateForm,self).__init__(*args, **kwargs)
        self.fields["username"].label = "Display name"
        self.fields["email"].label = "Email address"


class RegiestForm(forms.ModelForm):
    class Meta:
        model = Regiest_Form
        fields = ('std_name',)

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ["customer","register","sender_account_number","reciver_account_number","transaction_amount"]

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
