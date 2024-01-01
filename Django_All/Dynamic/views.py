from django.shortcuts import render


# Create your views here.

def Dynamic(request):
    return render(request, "Dynamic.html")
