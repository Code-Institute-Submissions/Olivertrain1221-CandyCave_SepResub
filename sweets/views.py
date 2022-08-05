from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower

from sweets.forms import SweetForm
from .models import Sweet, Category
from .forms import SweetForm


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
        # Not creditable to myself (Code Institute LMS for below lines 19-30)
        if 'sort' in request.GET:
            sort_type = request.GET['sort']
            sort = sort_type
            if sort_type == 'name':
                sort_type == 'lowername'
                sweets = sweets.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sort_type = f'-{sort_type}'
            sweets = sweets.order_by(sort_type)

        if 'category' in request.GET:
            sweet_type = request.GET['category']
            sweets = sweets.filter(category__name=sweet_type)
            sweet_type = Category.objects.filter(name__in=sweet_type)

        if 'search' in request.GET:
            query = request.GET['search']
            if not query:
                messages.error(request, "Please enter something to search")
                return redirect(reverse('sweets:sweets'))

            queries = Q(name__icontains=query) | Q(detail__icontains=query)
            sweets = sweets.filter(queries)

    sorting_method = f'{sort}_{direction}'

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


@login_required
def user_add_sweets(request):
    if request.method == 'POST':
        form = SweetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added sweet to shop')
            return redirect(reverse('sweets:amend_sweets'))
        else:
            messages.error(request, 'failed to add product!')
    else:
        form = SweetForm()

    template = 'sweets/amend_sweets.html'
    context = {
        'form': form
    }
    return render(request, template, context)


@login_required
def edit_sweet(request, product_id):
    """
    Edit existing product
    """
    sweet = get_object_or_404(Sweet, pk=product_id)
    if request.method == 'POST':
        form = SweetForm(request.POST, request.FILES, instance=sweet)
        if form.is_valid():
            form.save()
            messages.success(request, "Great changes have been made")
            return redirect(reverse('sweets:sweet_individual',
                                    args=[sweet.id]))
        else:
            messages.error(request, 'Please check the form again!')
    else:
        form = SweetForm(instance=sweet)
        messages.info(request, f'Your about to edit {sweet.name}')

    template = 'sweets/edit_sweets.html'
    context = {
        'form': form,
        'sweet': sweet
    }
    return render(request, template, context)


@login_required
def delete_sweet(request, product_id):
    """
    Edit existing product
    """
    sweet = get_object_or_404(Sweet, pk=product_id)
    sweet.delete()
    messages.success(request, 'Thats that in the bin!')
    return redirect(reverse('sweets:sweets'))
