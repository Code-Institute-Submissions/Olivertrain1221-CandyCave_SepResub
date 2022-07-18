@register.filter(name='products_total')
def products_total(price, quantity):
    return price * quantity
