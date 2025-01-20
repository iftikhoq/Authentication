from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name = 'home'),
    path('signup', views.SignupPage, name = 'signup'),
    path('login', views.LoginPage, name = 'login'),
    path('logout/', views.LogoutPage, name='logout'),
    path('profile/', views.ProfilePage, name='profile'),
    path('changepasswithprev/', views.Changepasswithprev, name='changepasswithprev'),
    path('changepasswithoutprev/', views.Changepasswithoutprev, name='changepasswithoutprev'),
    path('admin/', admin.site.urls),
]
