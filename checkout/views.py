from django.shortcuts import render, redirect, reverse
from django.contrib import messages

def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "There is nothing in your Basket!")
        return redirect(reverse('sweets'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }
    
    return render(request, template, context)