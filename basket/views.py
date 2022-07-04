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
    quantity_of_product = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        # if already in basket will add whatevery value quantity plus current basket
        basket[item_id] += quantity_of_product
    else:
        # otherwise just adds to basket (what user selects on first add)
        basket[item_id] = quantity_of_product

    request.session['basket'] = basket
    print(request.session['basket'])
    return redirect(redirect_url)
