@register.filter(name='products_total')
def products_total(price, quantity):
    return price * quantity

    <p class="my-0">${{ item.sweet.price | products_total:item.quantity }}</p>