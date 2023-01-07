from django import forms
from django.contrib.auth.forms import UserCreationForm


from demo_app.models import Login, Trainer


class LoginForm(UserCreationForm):
    class Meta:
        model= Login
        fields=('username','password1','password2')

class TrainerForm(forms.ModelForm):
    class Meta:
        model=Trainer
        fields=('name', 'age', 'address', 'qualification', 'achievement', 'contact_no', 'image')