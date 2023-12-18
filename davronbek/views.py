from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_user(request):
    next_page = request.GET.get('next')
    logout(request)
    return redirect(next_page)
    

def my_view(request):
    return HttpResponse("Hello, world. ccf086b6 is the polls index.")


def index(request):
    return render(request, 'task_2.html')
