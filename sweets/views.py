from django.shortcuts import render
from.models import Sweet

def all_sweets(request):
    """
    View that the main sweet page
    """
    sweets = Sweet.objects.all()

    context = {
        'sweets': sweets,
    }
    return render(request, 'sweets/sweets.html', context)