from django.urls import path
from . import views

app_name = 'sweets'

urlpatterns = [
    path('', views.all_sweets, name='sweets'),
    path('<product_id>', views.individual_sweet, name='sweet_individual'),
]
