from django.shortcuts import render
import random

# Create your views here.

def home(request):
    return render(request, 'home.htm')

def result(request):
    input = request.GET["input"]
    computer = random.randint(1,3)
    if computer==1:
        computer = "✌"
    elif computer==2:
        computer = "✊"
    else:
        computer = "✋"
    return render(request, 'result.htm', {'user':input, 'com':computer})