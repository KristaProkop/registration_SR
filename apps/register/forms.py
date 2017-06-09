from django import forms

from .models import User, CreditCard


DATE_INPUT_FORMATS = ['%d/%m/%Y']

class Name_Email_Form(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name','email')

class Name_Email_Password_Form(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('first_name', 'last_name','email', 'password')


class Credit_Card_Form(forms.ModelForm):
    class Meta:
        model = CreditCard
        fields = ('card_num', 'expiry','cvv')