from django.contrib import admin
from django.urls import path
from .views import IndexView, SearchView, AddsView, product_detail ,logout

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('search/', SearchView.as_view(), name='search'),
    path('logout/', logout.as_view(), name='logout'),
    path('adds/', AddsView.as_view(), name='adds'),

    path('product_detail/',product_detail,name='product_detail' ),
]