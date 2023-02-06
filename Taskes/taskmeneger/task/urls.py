from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('singin/', views.singin, name='singin'),
    path('login/', views.login, name='login'),
    path('important/', views.important, name='important'),
]
