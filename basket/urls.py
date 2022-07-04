from django.urls import path
from . import views
import basket

app_name = 'basket'

urlpatterns = [
    path('basket/', views.view_basket, name='basket'),
]
