from django.shortcuts import render, redirect


def view_basket(request):
    """
    Shows the basket and whats in it
    """

    return render(request, 'basket/basket.html')


def add_items_to_basket(request, item_id):
    """
    Adds a users item to there basket
    """
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
                # messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {basket[item_id]["sweets_by_size"][size]}')
            else:
                basket[item_id]['items_by_size'][size] = quantity
                # messages.success(request, f'Added size {size.upper()} {product.name} to your basket')
        else:
            basket[item_id] = {'items_by_size': {size: quantity}}
            # messages.success(request, f'Added size {size.upper()} {product.name} to your basket')
    else:
        if item_id in list(basket.keys()):
            basket[item_id] += quantity
            # messages.success(request, f'Updated {product.name} quantity to {basket[item_id]}')
        else:
            basket[item_id] = quantity
            # messages.success(request, f'Added {product.name} to your basket')

    request.session['basket'] = basket
    return redirect(redirect_url)
