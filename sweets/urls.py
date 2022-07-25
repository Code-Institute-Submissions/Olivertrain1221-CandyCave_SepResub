from django.urls import path
from . import views

app_name = 'sweets'

urlpatterns = [
    path('', views.all_sweets, name='sweets'),
    path('<int:product_id>/', views.individual_sweet, name='sweet_individual'),
    path('amend/', views.user_add_sweets, name='amend_sweets'),
    path('edit/<int:product_id>/', views.edit_sweet, name='edit_sweet'),
    path('delete/<int:product_id>/', views.delete_sweet, name='delete_sweet'),
]
