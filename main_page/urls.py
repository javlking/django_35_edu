from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page),
    path('category/<str:pk>', views.get_category),
    path('course/<str:pk>', views.get_course),
    path('add_course/<str:pk>', views.add_to_cart),
    path('user_cart', views.get_user_cart),
    path('confirm_order', views.order_confirmation)
]

