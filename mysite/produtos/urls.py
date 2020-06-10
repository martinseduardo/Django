from django.urls import path
from .views import home, novo

urlpatterns = [
    path('', home),
    path('novo', novo),
]
