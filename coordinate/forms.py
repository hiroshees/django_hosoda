from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model=Item
        fields=['name','category','season','image']
        error_massages = {
            'name':{
                'required':'必須入力です'
            },
        }
        help_texts = {
            'name':'名前は必須です'
        }
        widgets = {
            'name':forms.TextInput(attrs={'autofocus':True}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
