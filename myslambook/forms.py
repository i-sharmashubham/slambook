from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserModel
from .models import Slam

class SlamBook(forms.ModelForm):
    photo = forms.ImageField()
    user = forms.CharField(widget=forms.HiddenInput(attrs={'value':''}),required=False)
    dob = forms.DateField(widget=forms.DateInput(attrs={'type':'date','placeholder':'Date of Birth'}))
    gender = forms.ChoiceField(choices=(('MALE', 'Male'),('FEMALE', 'Female'),('OTHER', 'Other')),widget=forms.Select())
    phone = forms.CharField(max_length=15)
    desc = forms.CharField(widget=forms.Textarea,max_length=500,required=False)
    class Meta:
        model = Slam
        fields = ['user','photo','name','dob','gender','zodic','phone','email','facebook','instagram','twitter','address','nick1','nick2','skils','occupation','food','color','music','movie','actor','actress','sport','person','place','desc']

class Register(UserCreationForm):    
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']

class Login(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    