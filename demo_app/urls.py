from django.urls import path

from demo_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login_view',views.login_view,name='login_view'),
    path('trainer_register',views.trainer_register,name='trainer_register'),
]