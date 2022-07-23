from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import Profile
from .forms import ProfileForm


# Create your views here.
def profile(request):
    profile = get_object_or_404(Profile, user=request.user)

    if request == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated succesfully')

    orders = profile.orders.all()
    form = ProfileForm(instance=profile)
    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
    }
    return render(request, template, context)
