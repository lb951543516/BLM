from django.shortcuts import render


# Create your views here.
def market(request):
    return render(request, 'blm/main/market/market.html')
