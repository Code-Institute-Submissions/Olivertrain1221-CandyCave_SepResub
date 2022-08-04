from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from sweets.models import Sweet


def basket_items(request):
    """
    Shows the basket items available to all templates
    """
    sweet_total_price = 0
    quantity = 0
    basket_selection = []
    basket_sum = 0
    sweet_count = 0
    size = 0
    sweet_total_price = 0
    basket = request.session.get('basket', {})

    for item_id, item_data in basket.items():
        if isinstance(item_data, int):
            print("SWEET WITH NO SIZE")
            sweet = get_object_or_404(Sweet, pk=item_id)
            print(sweet, "sweet")
            basket_sum += item_data * sweet.price
            print(sweet.price)
            print(item_data, "item_data")
            sweet_count += item_data
            print(sweet_count, "sweet_count")
            basket_selection.append({
                'item_id': item_id,
                'quantity': item_data,
                'sweet': sweet,
            })
            print("END OF SWEET WITH NO SIZE")
        else:
            for size, quantity in item_data['items_by_size'].items():
                print("START SWEET WITH SIZE")
                sweet = get_object_or_404(Sweet, pk=item_id)
                sweet_total_price = int(size) * sweet.price
                print(sweet_total_price, "sweet_total_price")
                print(size, "size")
                print(sweet.price, "sweet.price")
                basket_sum += quantity * sweet_total_price
                sweet_count += quantity
                print(size)
                basket_selection.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'sweet': sweet,
                    'size': size,
                    'sweet_total_price': sweet_total_price
                })
                print("END OF SWEET WITH SIZE")

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
        'sweet_total_price': sweet_total_price,
        'free_postage_mark': free_postage_mark,
        'free_postage_price': settings.FREE_POSTAGE_PRICE,
        'grand_total': grand_total,
    }
    return context
