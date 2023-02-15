from django.urls import path
from .views import buy_item, show_item, all_items

urlpatterns = [
    path('buy/<int:id>/', buy_item, name='buy_item'),
    path('item/<int:id>/', show_item, name='show_item'),
    path('', all_items, name='all_items')
]
