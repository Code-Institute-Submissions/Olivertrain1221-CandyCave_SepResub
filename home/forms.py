from django import forms
from .models import ContactForm

class ContactFormForm(forms.ModelForm):
    """
    Creates the Form for Contacting the site
    """
    class Meta:
        model = ContactForm
        fields = (
            'firstname',
            'lastname',
            'useremail',
            'message'
        )
