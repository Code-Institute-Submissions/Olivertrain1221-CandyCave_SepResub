from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from sweets.models import Sweet

def basket_items(request):
    """
    Shows the basket items available to all templates
    """

    basket_selection = []
    basket_sum = 0
    sweet_count = 0
    basket = request.session.get('basket', {})

    for item_id, quantity in basket.items():
        sweet = get_object_or_404(Sweet, pk=item_id)
        basket_sum += quantity * sweet.price
        sweet_count += quantity
        basket_selection.append({
            'item_id': item_id,
            'quantity': quantity,
            'sweet': sweet,
        })


    if basket_sum < settings.FREE_POSTAGE_PRICE:
        post = basket_sum * Decimal(settings.DELIVERY_PERCENTAGE / 100)
        free_postage_mark = settings.FREE_POSTAGE_PRICE - basket_sum
    else:
        post = 0
        free_postage_mark = 0

    grand_total = post + basket_sum

    context = {
        'basket_selection': basket_selection,
        'basket_sum': basket_sum,
        'sweet_count': sweet_count,
        'post': post,
        'free_postage_mark': free_postage_mark,
        'free_postage_price': settings.FREE_POSTAGE_PRICE,
        'grand_total': grand_total,
    }

    return context