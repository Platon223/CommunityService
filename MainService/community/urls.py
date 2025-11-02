from django.urls import path
from . import routes

urlpatterns = [
    path('find', routes.find_community)
]