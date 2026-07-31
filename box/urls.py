from django.contrib import admin
from django.urls import path
from box import views


urlpatterns = [
    path('',views.index ,  name = 'box'),
    path("add-recipe/", views.add_recipe, name="add_recipe"),
    path("saved/", views.saved, name="saved"),
]
