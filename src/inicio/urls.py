from django.urls import path
from .views import dashboard

app_name = 'inicio'

urlpatterns = [
    path('', dashboard, name='inicio'),
]
