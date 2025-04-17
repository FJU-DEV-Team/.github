from django.urls import path
from . import views

app_name = 'index'

urlpatterns = [
    path('', views.index, name='home'),
    path('campus-food/', views.campus_food, name='campus_food'),
    path('nearby-food/', views.nearby_food, name='nearby_food'),
    path('popular-food/', views.popular_food, name='popular_food'),
    path('about/', views.about, name='about'),
]
