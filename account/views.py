from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import UserForm

# Create your views here.
def index(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserForm()
    return render(request, 'index.html', {'form': form})
