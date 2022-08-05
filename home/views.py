from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from urllib3 import HTTPResponse
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from home.forms import ContactFormForm

# Create your views here.


def index(request):
    """
    View that returns index page
    """
    return render(request, 'home/index.html')


def about(request):
    """
    View that returns index page
    """
    return render(request, 'home/about.html')


def contact(request):
    """
    View used for the contact form
    """
    form = ContactFormForm()
    context = {
        'form': form
    }
    return render(request, 'home/contact-us.html', context)


def contactForm(request):
    """
    Handles the form
    """
    if request.method == "POST":
        form = ContactFormForm(request.POST)
        if form.is_valid():
            contact = form.save()
            contact_fname = contact.firstname
            contact_email = contact.useremail
            contact_message = contact.message
            response_subject = render_to_string(
                'home/emails/contact_email_subject.txt',
            )
            response_body = render_to_string(
                'home/emails/contact_email_body.txt',
                {'contact_fname': contact_fname,
                 'message': contact_message
                 }
            )
            send_mail(
                response_subject,
                response_body,
                settings.DEFAULT_FROM_EMAIL,
                [settings.DEFAULT_FROM_EMAIL]
            )
            messages.success(request, "Your Message has been sent!")
            return redirect('home:contact-us')
        else:
            messages.error(request,
                           "Sorry please check the form again!")
