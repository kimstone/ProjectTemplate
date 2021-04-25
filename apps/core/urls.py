from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="core/index"),
    path('dtg', views.current_datetime, name="core/dtg"),
]