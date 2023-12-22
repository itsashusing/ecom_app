from django.shortcuts import render, redirect
from .form import SignUpUserForm, CheckOutForm
from django.contrib import messages
from django.views import View
from .models import BillingAddress
from django.core.exceptions import ObjectDoesNotExist
from mainapp.models import Order
from mainapp import views
# Create your views here.


def SignUpUserView(request):
    if request.method == 'POST':
        form = SignUpUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            messages.success(
                request, f'Account created successfully. log-in now.')
            return redirect('login')
    else:
        form = SignUpUserForm

    context = {
        'form': form
    }
    return render(request, 'user/singup.html', context)


class CheckoutView(View):
    def get(self, request, *args, **kwargs):
        form = CheckOutForm()

        context = {
            'form': form
        }
        return render(self.request, 'user/checkout.html', context)

    def post(self, request, *args, **kwargs):
        form = CheckOutForm(self.request.POST)
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            if form.is_valid():
                address = form.cleaned_data.get('address')
                phonenumber = form.cleaned_data.get('phonenumber')
                city = form.cleaned_data.get('city')
                user = self.request.user
                billingaddress = BillingAddress(
                    user=user,
                    address=address,
                    city=city,
                    phonenumber=phonenumber
                )
                billingaddress.save()
                order.billing_address = billingaddress
                order.save()
                summery=True
                messages.success(
                    self.request, f'Your order is confirm.  {self.request.user}')
                return redirect('ordersummery')

        except ObjectDoesNotExist:
            messages.info(self.request, f'You have not any order.')
            return redirect('/')

        else:
            messages.error(
                self.request, f'Your order is not confirm.  {self.request.user}')
            return redirect('checkout')
