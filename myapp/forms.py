from django import forms

class ContactForm(forms.Form):
    name=forms.CharField(label='Enter Name')
    email=forms.EmailField(label='Enter Email')
    subject=forms.CharField(required=False)
    body=forms.CharField(widget=forms.Textarea)

