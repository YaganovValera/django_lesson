from django import forms


class PhotoUploadForm(forms.Form):
    img_product = forms.ImageField()





