from django import forms
from .models import *


# class AddPostForm(forms.Form):
#     title = forms.CharField(max_length=255)


class AddPostForm(forms.ModelForm):
    class Meta:
        model = BaseImages
        fields = '__all__'
