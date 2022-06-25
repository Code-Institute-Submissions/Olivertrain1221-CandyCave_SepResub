from django.shortcuts import render, get_object_or_404
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


def individual_sweet(request, product_id):
    """
    Shows the individual sweet
    """
    sweet = get_object_or_404(Sweet, pk=product_id)

    context = {
        'sweet': sweet,
    }
    return render(request, 'sweets/individual_sweet.html', context)
