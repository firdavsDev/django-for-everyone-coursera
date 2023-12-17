from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('hello.urls', namespace='hello')),
    path('admin/', admin.site.urls),
    path('polls/', include('quiz.urls', namespace='quiz')),
]
