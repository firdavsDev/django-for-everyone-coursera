from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    # path('', include('hello.urls', namespace='hello')),
    path('', include('home.urls')),  # Change to ads.urls
    path('admin/', admin.site.urls),
    path('polls/', include('quiz.urls', namespace='quiz')),
    
    path('accounts/', include('django.contrib.auth.urls')),  # Keep

    # Sample applications
    path('autos/', include('autos.urls')),
]
