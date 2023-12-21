from django.shortcuts import render, get_object_or_404, redirect
from .models import Item, Order, OrderItem
from django.views.generic import ListView, DetailView
from django.utils import timezone
from django.contrib import messages
from django.views import View
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class HomeView(ListView):
    model = Item
    template_name = 'mainapp/home.html'


class ItemDetailsView(DetailView):
    model = Item
    template_name = 'mainapp/itemdetails.html'


class OrderSummeryView(LoginRequiredMixin, View):
    def get(self, request, *arg, **kwargs):

        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                'object': order
            }
            return render(self.request, 'mainapp/order_summery.html', context)
        except ObjectDoesNotExist:
            messages.info(self.request, f'You have not any order.')
            return redirect('/')


@login_required
def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item, user=request.user, ordered=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, f'This item quantity updated successfully')
            return redirect('ordersummery')
        else:
            messages.success(request, f'This item add to your cart.')
            order.items.add(order_item)
            return redirect('ordersummery')
    else:
        order_date = timezone.now()
        order = Order.objects.create(user=request.user, order_date=order_date)
        order.items.add(order_item)
        messages.success(request, f'This item add to your cart.')
        return redirect('ordersummery')


@login_required
def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the the order
        if order.items.filter(item__slug=item.slug).exists():

            order_item = OrderItem.objects.filter(
                item=item, user=request.user, ordered=False)[0]

            order.items.remove(order_item)
            messages.info(request, f'This item was removed from your cart')
            return redirect('itemdetailsview', slug=slug)
        else:
            messages.info(request, f'This item is not in your cart.')
            return redirect('itemdetailsview', slug=slug)
    else:
        messages.info(request, f'You have not an active order.')
        return redirect('itemdetailsview', slug=slug)


@login_required
def remove_single_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the the order
        if order.items.filter(item__slug=item.slug).exists():

            order_item = OrderItem.objects.filter(
                item=item, user=request.user, ordered=False)[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
                messages.info(request, f'The item quantity was updated.')
                return redirect('ordersummery')
            else:
                order.items.remove(order_item)
            messages.info(request, f'The item quantity was updated.')
            return redirect('ordersummery')
        else:
            messages.info(request, f'This item is not in your cart.')
            return redirect('itemdetailsview', slug=slug)
    else:
        messages.info(request, f'You have not an active order.')
        return redirect('itemdetailsview', slug=slug)
