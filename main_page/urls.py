from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page),
    path('category/<str:pk>', views.get_category)
]
