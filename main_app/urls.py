from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("aula/<int:aula_id>/", views.aula_detail, name="aula_detail"),
    path("test/", views.test_view, name="test_view"),
]

