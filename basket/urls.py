from django.urls import path
from . import views


app_name = 'basket'

urlpatterns = [
    path('basket/', views.view_basket, name='basket'),
    path('add/<item_id>/', views.add_items_to_basket, name='add_items_to_basket'),
]
