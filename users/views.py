from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from todo.models import TodoList, Todo


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,
                             f'Konto zostało utworzozne dla {username}! \
                             Możesz się teraz zalogować !')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        print(request.user)
        u_form = UserUpdateForm(request.POST, instance=request.user)
        print(u_form)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,
                             f'Konto zostało zaaktualizowane !')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    todo_list = TodoList.objects.filter(author=request.user) \
        .order_by('-created')

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'todo_list': todo_list
    }

    return render(request, 'users/profile.html', context)
