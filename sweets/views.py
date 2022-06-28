from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from.models import Sweet

def all_sweets(request):
    """
    View that the main sweet page
    """
    sweets = Sweet.objects.all()
    query = None
    
    if request.GET:
        if 'search' in request.GET:
            query = request.GET['search']
            if not query:
                messages.error(request, "Please enter something to search")
                return redirect(reverse('sweets'))

            queries = Q(name__icontains=query) | Q(detail__icontains=query)
            sweets = sweets.filter(queries)

    context = {
        'sweets': sweets,
        'search_term': query,
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
