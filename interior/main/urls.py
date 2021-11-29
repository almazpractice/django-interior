from django.urls import path

from . import views


app_name = 'interior'


urlpatterns = [
    path('', views.index, name='index'),
    path('catalog', views.catalog, name='catalog'),
    path('cart', views.cart, name='cart'),
    path('group/<slug:slug>/', views.group_list, name='group_list'),
]