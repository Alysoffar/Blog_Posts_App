
from django.shortcuts import render , redirect# type: ignore
from django.contrib.auth.forms import UserCreationForm # type: ignore
from django.contrib import messages # type: ignore
from .forms import UserRegesiterForm , UserUpdateForm ,ProfileUpdateForm
from django.contrib.auth.decorators import login_required # type: ignore
# Create your views here.
from django.contrib.auth import logout # type: ignore

def register(request):
    if request.method == "POST":
        form = UserRegesiterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request , f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegesiterForm()
    return render(request, 'users/register.html',{'form':form})


def logout_view(request):
    logout(request)
    messages.success(request , f'You are logged out!')
    return redirect('login')

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    
    return render(request, 'users/profile.html', context)
