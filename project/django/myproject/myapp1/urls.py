from django.urls import path
from . import views

# create views
urlpatterns = [
    path('', views.about, name='about'),
]