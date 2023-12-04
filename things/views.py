from django.shortcuts import render, redirect
from .forms import ThingForm
from .models import Thing

def home(request):
    if request.method == 'POST':
        form = ThingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ThingForm()

    things = Thing.objects.all()
    return render(request, 'home.html', {'form': form, 'things': things})
