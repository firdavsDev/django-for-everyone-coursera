import os

from django.contrib import admin
from django.urls import path, include
from django.views.static import serve

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('accounts/', include('django.contrib.auth.urls')),  # Keep
    path('oauth/', include('social_django.urls', namespace='social')),  # Keep

    # Sample applications
    path('autos/', include('autos.urls')),
    path('cats/', include('cats.urls')),
    path('polls/', include('quiz.urls', namespace='quiz')),
    path('', include('ads.urls')),

    # path('', include('hello.urls', namespace='hello')),
    # path('', include('home.urls')),  # Change to ads.urls

]


# Serve the static HTML
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
urlpatterns += [
    path('site/', serve,
        {'document_root': os.path.join(BASE_DIR, 'site'),
         'show_indexes': True},
        name='site_path'
        ),
]

# Serve the favicon - Keep for later
urlpatterns += [
    path('favicon.ico', serve, {
            'path': 'favicon.ico',
            'document_root': os.path.join(BASE_DIR, 'home/static'),
        }
    ),
]

# Switch to social login if it is configured - Keep for later
try:
    from . import github_settings
    social_login = 'registration/login_social.html'
    urlpatterns.insert(0,
                       path('accounts/login/', auth_views.LoginView.as_view(template_name=social_login))
                       )
    print('Using', social_login, 'as the login template')
except:
    print('Using registration/login.html as the login template')

# References

# https://docs.djangoproject.com/en/3.0/ref/urls/#include
