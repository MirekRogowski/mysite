from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import reverse_lazy

from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


# class UserRegisterView(generic.CreateView):
#     form_class = UserCreationForm
#     template_name = 'users/register.html'
#     success_url = reverse_lazy('login')


class BlogLoginView(LoginView):
    template_name = 'users/login.html'
    success_url = reverse_lazy('login')


class BlogLogoutView(LogoutView):
    template_name = 'users/logout.html'
    success_url = reverse_lazy('logout')


class BlogResetPasswordsView(PasswordResetView):
    template_name = 'users/password_reset.html'
    success_url = reverse_lazy('password_reset')
    success_message = "Email został wysłany na podany email"


class BlogPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'users/password_reset_done.html'
    success_url = reverse_lazy('password_reset')


class BlogPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'users/reset.html'
    success_url = reverse_lazy('password_reset_confirm')


class BlogPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'password_reset_complete.html'
    success_url = reverse_lazy('password_reset_complete')


class UserRegister(generic.CreateView):
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')
    success_message = "Utworzyłeś nowe konto"


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account is updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'f_form': p_form
    }

    return render(request, 'users/profile.html', context)

