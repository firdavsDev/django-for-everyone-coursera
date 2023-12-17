from django.shortcuts import render
from django.http import HttpResponse

def my_view(request):
    return HttpResponse("Hello, world. ccf086b6 is the polls index.")


def index(request):
    return render(request, 'task_2.html')
