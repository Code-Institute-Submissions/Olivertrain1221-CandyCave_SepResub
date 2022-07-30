from django.http import HttpResponseRedirect
from django.shortcuts import render
from urllib3 import HTTPResponse

from home.models import ContactForm

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
    submitted = False
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            return HttpResponseRedirect()