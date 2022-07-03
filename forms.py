from django import forms
from django.forms.widgets import DateInput
from .models import users
class usersform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = users
        fields = "__all__"