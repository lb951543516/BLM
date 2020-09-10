from django.shortcuts import render

# Create your views here.
from HomeApp.models import BlmWheel


def home(request):
    wheels = BlmWheel.objects.all()
    context = {
        'wheels': wheels
    }
    return render(request, 'blm/main/home/home.html', context=context)
