from django.db import models

# Create your models here.
class ContactForm(models.Model):
    """
    Contact Form model
    """
    firstname = models.CharField(max_length=15)
    lastname = models.CharField(max_length=15)
    usermessage = models.CharField(max_length=1000)
    useremail = models.EmailField(blank=False)
