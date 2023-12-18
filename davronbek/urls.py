import os

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', include('ads.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # Keep
    #logout
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
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
