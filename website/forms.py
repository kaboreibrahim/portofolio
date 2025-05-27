from django import forms

class ContactForm(forms.Form):
    contactName = forms.CharField()
    contactEmail = forms.EmailField()
    contactNumber = forms.CharField()
    contactSubject = forms.CharField()
    contactMessage = forms.CharField(widget=forms.Textarea)