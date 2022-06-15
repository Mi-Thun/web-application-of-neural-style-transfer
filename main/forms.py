from django import forms
from .models import InputImage,TestImage


class ImageForm(forms.ModelForm):
    style_image=forms.FileField(widget=forms.FileInput(attrs={'onchange':'preview1()','class':'form-control','id':'formFile'}))
    source_image=forms.FileField(widget=forms.FileInput(attrs={'onchange':'preview()','class':'form-control','id':'formFile'}))
    class Meta:
        model=InputImage
        fields=['style_image','source_image']
        
    