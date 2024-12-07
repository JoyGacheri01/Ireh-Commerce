from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('insert_message', views.insert_message, name="insert_message"),
    path('about/', views.about, name='about'),
    path('product/', views.product, name='product'),
    path('cart/', views.cart, name='cart'),
    path('services/', views.services, name='services'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('product_list/', views.product_list, name='product_list'),
    path('cart/', views.view_cart, name='view_cart'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('search/', views.search, name='search')

    
  
]