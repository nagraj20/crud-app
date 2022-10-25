from django import forms
from .models import users
from django.forms import fields

class user_forms(forms.ModelForm):
    class Meta:
        model = users
        fields ="__all__"