from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('create', views.user_create, name='create'),
    path('login', views.login_view, name='login'),
]
