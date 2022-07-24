from django.urls import path
from . import views

app_name = 'sweets'

urlpatterns = [
    path('', views.all_sweets, name='sweets'),
    path('<int:product_id>/', views.individual_sweet, name='sweet_individual'),
    path('amend/', views.user_add_sweets, name='amend_sweets'),
]
