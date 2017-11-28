from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
#from .tasks import order_created
from cart.cart import Cart
from django.core.mail import send_mail
from .models import Order
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse



def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # clear the cart
            cart.clear()
            # launch asynchronous task
            order_created(order.id)
            request.session['order_id'] = order.id
            return redirect(reverse('payment:process'))
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'cart': cart,
                                                        'form': form})


def order_created(order_id):
    """
    Task to send an e-mail notification when an order is successfully created.
    """
    order = Order.objects.get(id=order_id)
    subject = 'Order nr. {}'.format(order.id)
    message = 'Dear {},\n\nYou have successfully placed an order. Your order id is {}.'.format(order.first_name,
                                                                             order.id)
    mail_sent = send_mail(subject, message, 'elearningsteam2@gmail.com', [order.email])
    return mail_sent