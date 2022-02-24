from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    names = ["Cherish", "Adams", "Owen", "Sean", "Paris", "Walter"]
    context = {
        'names': names,
    }



    return render(request, "home.html", context)