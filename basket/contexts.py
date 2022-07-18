from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from sweets.models import Sweet

def basket_items(request):
    """
    Shows the basket items available to all templates
    """

    sweet_calculated_price = []
    basket_selection = []
    basket_sum = 0
    sweet_count = 0
    basket = request.session.get('basket', {})

    for item_id, item_data in basket.items():
        if isinstance(item_data, int):
            sweet = get_object_or_404(Sweet, pk=item_id)
            basket_sum += item_data * sweet.price
            sweet_count += item_data
            basket_selection.append({
                'item_id': item_id,
                'quantity': item_data,
                'sweet': sweet,
            })
        else:
            for size, quantity in item_data['items_by_size'].items():
                sweet = get_object_or_404(Sweet, pk=item_id)
                basket_sum += quantity * sweet.price
                sweet_count += quantity
                print(sweet_count)
                print(quantity)
                basket_selection.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'sweet': sweet,
                    'size': size,
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
        'quantity': quantity,
        'free_postage_mark': free_postage_mark,
        'free_postage_price': settings.FREE_POSTAGE_PRICE,
        'grand_total': grand_total,
    }
    return context
