

from pdb import post_mortem
from decimal import Decimal
from django.conf import settings

from candy_cave.settings import FREE_POSTAGE_PRICE

def basket_items(request):
    """
    Shows the basket items available to all templates
    """

    basket_selection = []
    basket_sum = 0
    sweet_count = 0

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
        'free_postage_mark': free_postage_mark,
        'free_postage_price': settings.FREE_POSTAGE_PRICE,
        'grand_total': grand_total,
    }

    return context