from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="app"),
    path('add/', views.add, name="add"),
    path("addRec/", views.add_record, name="addRec"),
    path('delete/<int:id>/', views.delete, name="delete"),
    path('change/<int:id>/', views.upRec, name="change"),
    path('change/upRec/<int:id>/', views.upRec, name="upRec"),  
]