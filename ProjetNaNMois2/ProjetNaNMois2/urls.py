"""ProjetNaNMois2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views


from account.views import (
    # home_page,
    registration_view,
    logout_view,
    login_view,
    account_view
)

from scraping.views import (
    scrappe_view,
    scrap_view
)
from bookmak.views import pariform_view

urlpatterns = [
    path('admin/', admin.site.urls),
    
    #Scrapping
    path('', scrap_view, name="scraping"),
    path('scrapper/', scrappe_view, name="scrapper"),            
    
    # Account
    path('register/', registration_view, name="register"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('account/', account_view, name="account"),

    path('pari/', pariform_view, name="pari"),



    # Mot de passe Change
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='Password/password_change.html'), 
    name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='Password/password_change_done.html'),
    name='password_change_done'),

    # Mot de Passe oublier
    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='Password/password_reset_done.html'),
    name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
    name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='Password/password_reset_complete.html'),
    name='password_reset_complete'),
]


# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
