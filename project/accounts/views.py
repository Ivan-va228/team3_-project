# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend') # Додано backend для автентифікації
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})