from django.urls import path
from . import views

app_name='library_app'

urlpatterns = [
    path('', views.home, name='home')
    path('catalog/', views.catalog, name='catalog')
    path('checkout/', views.checkout, name='checkout')
    #include the detailed_view one here
]