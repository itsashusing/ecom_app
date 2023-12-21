from django.shortcuts import render,redirect
from .form import SignUpUserForm
from django.contrib import messages
# Create your views here.


def SignUpUserView(request):
    if request.method == 'POST':
        form=SignUpUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
            messages.success(request,f'Account created successfully. log-in now.')
            return redirect('login')
    else:
        form=SignUpUserForm

    context={
        'form':form
    }
    return render(request,'user/singup.html',context)