
from django.contrib import admin
from django.urls import path
from MyProject.views import *
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('admin/', admin.site.urls),
    path('HomePage/',homePage,name='homePage'),
    path('',loginPage,name='loginPage'),
    path('registerPage/',registerPage,name='registerPage'),
    path('logoutPage/',logoutPage,name='logoutPage'),
    path('profilePage/',profilePage,name='profilePage'),

    path('addjob/',addjob,name='addjob'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
