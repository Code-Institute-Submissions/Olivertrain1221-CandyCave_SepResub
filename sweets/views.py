from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Sweet, Category

def all_sweets(request):
    """
    View that the main sweet page
    """
    sweets = Sweet.objects.all()
    query = None
    sweet_type = None
    sort = None
    direction = None
    sort_type = None

    if request.GET:

        if 'sort' in request.GET:
            sort_type = request.GET['sort']
            sort = sort_type
            if sort_type == 'name':
                sort_type == 'lowername'
                products = products.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sort_type = f'-{sort_type}'
            sweets = sweets.order_by(sort_type)

        if 'category' in request.GET:
            sweet_type = request.GET['category']
            print(sweet_type)
            sweets = sweets.filter(category__name=sweet_type)
            sweet_type = Category.objects.filter(name__in=sweet_type)
            print(sweet_type)

        if 'search' in request.GET:
            query = request.GET['search']
            if not query:
                messages.error(request, "Please enter something to search")
                return redirect(reverse('sweets:sweets'))

            queries = Q(name__icontains=query) | Q(detail__icontains=query)
            sweets = sweets.filter(queries)

    sorting_method = f'-{sort}_{direction}'

    context = {
        'sweets': sweets,
        'search_term': query,
        'sweet_type': sweet_type,
        'sorting_method': sorting_method,
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
