from django.shortcuts import render

from HomeApp.models import BlmWheel
from HomeApp.models import BlmChoice
from HomeApp.models import BlmDiscount
from HomeApp.models import BlmBrand
from HomeApp.models import BlmActivity
from HomeApp.models import BlmRecommend


def home(request):
    wheels = BlmWheel.objects.all()
    choices = BlmChoice.objects.all()
    discounts = BlmDiscount.objects.all()
    brands = BlmBrand.objects.all()
    activities = BlmActivity.objects.all()
    recommends = BlmRecommend.objects.all()

    context = {
        'wheels': wheels,
        'choices': choices,
        'discounts': discounts,
        'brands': brands,
        'activities': activities,
        'recommends': recommends,
    }
    return render(request, 'blm/main/home/home.html', context=context)
