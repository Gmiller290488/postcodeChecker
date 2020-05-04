from django.shortcuts import render
from .forms import UserForm

def register_user(request):
    form = UserForm(request.POST)
    if form.is_valid():
        user = form.save(commit=True)
        user.save()
    return render(request, 'postcodeApp/register_user.html', {'form': form})