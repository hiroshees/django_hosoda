from django import forms
from django.forms import ModelForm
from django.contrib.auth import grt_user_model

class UserUpdateForm(ModelForm):
    class Meta:
        model=get_user_model()
        fields=['last_name','firstname']
        lables={
            'last_name':'姓',
            'firstname':'名',
        }
