from django import forms
from .models import *


class CommentForm(forms.ModelForm):
    class Meta:
        model = comment
        fields = ('Name', 'Email', 'Body')
