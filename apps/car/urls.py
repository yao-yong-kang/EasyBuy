
from django.contrib import admin
from django.urls import path
from apps.car import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index,name='index'),
    path('car1/',views.car1,name='goodcar1'),
    path('car2/',views.car2,name='goodcar2'),
    path('car3/',views.car3,name='goodcar3'),
    path('car4/',views.car4,name='goodcar4'),
    path('car5/',views.car5,name='goodcar5'),
    path('dele/<id>/',views.dele,name='dele'),
]
