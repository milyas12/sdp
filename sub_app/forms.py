from django import forms
from .models import SkinModel
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SkinForm(forms.ModelForm):
	class Meta:
		model=SkinModel
		fields = "__all__"
  

#Sign-up form.
class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]