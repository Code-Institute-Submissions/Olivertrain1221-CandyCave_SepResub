from django.shortcuts import render


def view_basket(request):
    """
    Shows the basket and whats in it
    """
    
    return render(request, 'basket/basket.html')