import os

from django.contrib import admin
from django.urls import path, include, re_path
# from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.views.static import serve

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


# Serve the static HTML
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
urlpatterns += [
    re_path(r'^site/(?P<path>.*)$', serve,
        {'document_root': os.path.join(BASE_DIR, 'site'),
         'show_indexes': True},
        name='site_path'
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
