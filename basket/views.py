from django.shortcuts import (
        render,
        redirect,
        reverse,
        HttpResponse,
        get_object_or_404
)

from django.contrib import messages
from sweets.models import Sweet


def view_basket(request):
    """
    Shows the basket and whats in it
    """
    return render(request, 'basket/basket.html')


def add_items_to_basket(request, item_id):
    """
    Adds a users item to there basket
    """
    sweet = get_object_or_404(Sweet, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})
    size = None
    if 'sweet_measurement' in request.POST:
        size = request.POST['sweet_measurement']

    if size:
        if item_id in list(basket.keys()):
            if size in basket[item_id]['items_by_size'].keys():
                basket[item_id]['items_by_size'][size] += quantity
                messages.success(request, f'Updated size {size.upper()}{sweet.name} quantity to {basket[item_id]["items_by_size"][size]}')
            else:
                basket[item_id]['items_by_size'][size] = quantity
                messages.success(request, f'Added size{size.upper()} {sweet.name} to your basket')
        else:
            basket[item_id] = {'items_by_size': {size: quantity}}
            messages.success(request, f'Added size{size.upper()} {sweet.name} to your basket')
    else:
        if item_id in list(basket.keys()):
            basket[item_id] += quantity
            messages.success(request, f'Updated{sweet.name} quantity to {basket[item_id]}')
        else:
            basket[item_id] = quantity
            messages.success(request, f'Added{sweet.name} to your basket')

    request.session['basket'] = basket
    return redirect(redirect_url)


def adjust_basket(request, item_id):
    """Adjust the quantity of the specified sweet to the specified amount"""
    sweet = get_object_or_404(Sweet, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'sweet_measurement' in request.POST:
        size = request.POST['sweet_measurement']
    basket = request.session.get('basket', {})
    if size:
        if quantity > 0:
            basket[item_id]['items_by_size'][size] = quantity
            messages.success(request, f'Updated size {size.upper()}{sweet.name} quantity to{basket[item_id]["items_by_size"][size]}')
        else:
            del basket[item_id]['items_by_size'][size]
            if not basket[item_id]['items_by_size']:
                basket.pop(item_id)
                messages.success(request, f'Removed size{size.upper()} {sweet.name} from your bag')
    else:
        if quantity > 0:
            basket[item_id] = quantity
            messages.success(request, f'Updated{sweet.name} quantity to {basket[item_id]}')
        else:
            basket.pop(item_id)
            messages.success(request, f'Removed {sweet.name} from your bag')

    request.session['basket'] = basket
    return redirect(reverse('basket:view_basket'))


def remove_from_basket(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        sweet = get_object_or_404(Sweet, pk=item_id)
        size = None
        if 'sweet_measurement' in request.POST:
            size = request.POST['sweet_measurement']
        basket = request.session.get('basket', {})

        if size:
            del basket[item_id]['items_by_size'][size]
            if not basket[item_id]['items_by_size']:
                basket.pop(item_id)
                messages.success(request, f'Removed size {size.upper()}{sweet.name} from your bag')
        else:
            basket.pop(item_id)
            messages.success(request, f'Removed {sweet.name} from your bag')

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
