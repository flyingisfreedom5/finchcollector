from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

class Finch:
    def __init__(self, name, breed, description, age):
      self.name = name
      self.breed = breed
      self.description = description
      self.age = age

finches = [
    Finch('Charlie', 'Zebra', 'Grey Shape', 0),
    Finch('Mike', 'Gouldian', 'Blue and Yellow Shape', 3),
    Finch('Peter', 'European', 'Black and Yellow Shape', 5),
    Finch('Sophia', 'Java Sparrow', 'Blue Shape', 2)
]

def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>' )


def about(request):
    return render(request, 'about.html' )

def finches_index(request):
    return render(request, 'finches/index.html', { 'finches': finches })
    