from django import forms
from .models import UserProfile, User
#from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper

class UserForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_show_labels = False


    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password')

class UserProfileForm(forms.ModelForm):
     class Meta():
         model = UserProfile
         fields = ('full_name', 'department', 'employee_id', 'app_user_id', 'role', 'is_admin',)
