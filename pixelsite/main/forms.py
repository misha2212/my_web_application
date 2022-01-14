from django import forms
from .models import *


class AddPostForm(forms.ModelForm):
    class Meta:
        model = BaseImages
        fields = '__all__'
