import os

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView

from .views import logout_user

urlpatterns = [
    path('', include('ads.urls')),
    path('admin/', admin.site.urls),
    path('accounts/logout/', logout_user, name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),  # Keep
    #logout
    path('oauth/', include('social_django.urls', namespace='social')),  # Keep

    # Sample applications
    path('autos/', include('autos.urls')),
    path('cats/', include('cats.urls')),
    path('polls/', include('quiz.urls', namespace='quiz')),

    # path('', include('hello.urls', namespace='hello')),
    # path('', include('home.urls')),  # Change to ads.urls

]

# References

# https://docs.djangoproject.com/en/3.0/ref/urls/#include
