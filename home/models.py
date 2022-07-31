from django.db import models

# Create your models here.
class ContactForm(models.Model):
    """
    Contact Form model
    """
    firstname = models.CharField(blank=False, max_length=15)
    lastname = models.CharField(blank=False, max_length=15)
    useremail = models.EmailField(blank=False)
    message = models.CharField(blank=False, max_length=1000)

    def __str__(self):
        return self.name
