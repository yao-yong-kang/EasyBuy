from django.contrib import admin
from django.urls import path
from .views import IndexView, SearchView, KindView, AddsView, product_detail ,logout

app_name = 'goods'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('search/', SearchView.as_view(), name='search'),
    path('kind/', KindView.as_view(), name='kind'),
    path('logout/', logout.as_view(), name='logout'),
    path('adds/', AddsView.as_view(), name='adds'),

    path('product_detail/',product_detail,name='product_detail' ),
]