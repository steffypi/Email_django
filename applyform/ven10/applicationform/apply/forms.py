from django import forms
from apply.models import application

class applyform(forms.ModelForm):
    class Meta:
        model=application
        fields='__all__'