from django.urls import path
from . import views
urlpatterns = [
    path('add/', views.addCategory, name='add_category'),
]
