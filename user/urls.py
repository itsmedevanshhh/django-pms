from django.contrib import admin
from django.urls import path,include
from .views import *
from django.contrib.auth.views import LogoutView
from user import views
urlpatterns = [
 
    path('managerregister/',ManagerRegisterView.as_view(),name='managerregister'),
    path('developerregister/',DeveloperRegisterView.as_view(),name='developerregister'),
    path('login/',UserLoginView.as_view(),name='login'),
    path('logout/',UserLogoutView.as_view(),name='logout'),
    path('dashboard/',dashboard,name='dashboard'),
    path('managerlogin/',managerlogin.as_view(),name='managerlogin'),
    path('developerlogin/',developerlogin.as_view(), name='developerlogin'),
    path('managerpage/',ManagerPage.as_view(),name='managerpage'),
    path('developerpage/',DeveloperPage.as_view(), name='developerpage'),
    path('manager_dashboard/',ManagerDashboardView.as_view(),name='manager_dashboard'),
    path('contactus/', ContactUs.as_view(), name='contactus'),
    path('aboutus/', AboutUs.as_view(), name='aboutus'),  
    path('registration/', Registrations.as_view(), name='registration'),
    # path('home/' ,home,name='home'),

]