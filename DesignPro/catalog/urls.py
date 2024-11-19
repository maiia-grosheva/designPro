from django.urls import path
from .views import index
from . import views


urlpatterns = [
    path('catalog/', index, name='index'),
    path('catalog/login/', views.Login.as_view(), name='login'),
]