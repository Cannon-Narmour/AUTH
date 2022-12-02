from django import forms 
from .models import *

class AmbassadorForm(forms.ModelForm):
    class Meta:
        model = Ambassador
        fields = "__all__"