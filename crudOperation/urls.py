from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_notification, name='add_notification'),
    path('delete/<int:id>/', views.delete_notification, name='delete_notification'),
]
