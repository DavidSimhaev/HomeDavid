from django import forms

from .models import PROFILE_IMG


class IMG_PROFILE_FORM(forms.ModelForm):
    class Meta:
        model = PROFILE_IMG
        fields = ["image", "post"]
        labels = {"image": " "}
        
        widgets = {'post': forms.HiddenInput()}
        
