from django.shortcuts import render
from .models import Order, Customer, OrderItem, ShippingAddress
# Create your views here.


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
    context = {
        "items": items,
    }
    return render(request, "shopping/cart.html", context=context)
