<<<<<<< HEAD
from django.shortcuts import render, get_object_or_404
=======
<<<<<<< HEAD
from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
>>>>>>> 3a0c8c0d6cbc06323f0e3e51cd019aa092a0da78
from django.contrib import messages

<<<<<<< HEAD
from .models import UserProfile
from .forms import UserProfileForm
=======
from .forms import OrderForm
from .models import Order, OrderLineItem
=======
from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm
>>>>>>> 384bd3250c81a51072fc19b48f90df312af56a99
>>>>>>> 3a0c8c0d6cbc06323f0e3e51cd019aa092a0da78


<<<<<<< HEAD
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)
=======
import stripe
import json

<<<<<<< HEAD

@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
>>>>>>> 3a0c8c0d6cbc06323f0e3e51cd019aa092a0da78

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
<<<<<<< HEAD
        'form': form,
        'orders': orders,
        'on_profile_page': True
=======
        'order': order,
=======
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
>>>>>>> 384bd3250c81a51072fc19b48f90df312af56a99
>>>>>>> 3a0c8c0d6cbc06323f0e3e51cd019aa092a0da78
    }

    return render(request, template, context)