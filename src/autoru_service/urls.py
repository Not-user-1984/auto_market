from django.urls import path
from autoru_service import views

urlpatterns = [
    path('update_autoru_catalog/', views.update_autoru_catalog, name='update_autoru_catalog'),
    path('delete_autoru_catalog/', views.delete_autoru_catalog, name='delete_autoru_catalog'),
    path('', views.home, name='home'),
]