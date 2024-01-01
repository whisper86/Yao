from django.shortcuts import render


# Create your views here.
def Try(requests):
    return render(requests, "try.html")


def Design(requests):
    return render(requests, "Design.html")


def Description(requests):
    return render(requests, "description.html")


def Ark_Login(requests):
    return render(requests, "ark_login.html")


def Frame(requests):
    return render(requests, 'frame.html')
