# Form to accept file upload

from django import forms

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    pic = forms.FileField(label='Select a file')

