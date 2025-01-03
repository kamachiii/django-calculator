from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="math-index"),
    path("calculator/", views.calculator, name="math-calculator"),
]

