from django.urls import path
from . import views

urlpatterns =[
    path('login/', views.login, name='login'),
    path('', views.home, name='home'),
    path('api/check_status/',views.check_status.as_view()),
    path('logout/',views.logout,name='logout'),
    path('otp/',views.otp,name='otp'),
    path('reset_password/',views.reset_password,name='reset_password'),
]