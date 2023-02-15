from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
import stripe
from .models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY

def buy_item(request, id):
    item = Item.objects.get(id=id)
    price = int(item.price * 100)  # convert to cents
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'unit_amount': price,
                'product_data': {
                    'name': item.name,
                    'description': item.description,
                },
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri('/success/'),
        cancel_url=request.build_absolute_uri('/cancel/'),
    )
    return JsonResponse({'session_id': session.id, 'stripe_public_key': settings.STRIPE_PUBLIC_KEY})


def show_item(request, id):
    item = Item.objects.get(id=id)
    context = {'item': item}
    return render(request, 'app/item_detail.html', context)


def all_items(request):
    items = Item.objects.all()
    context = {'items': items}
    return render(request, 'app/all_items.html', context)