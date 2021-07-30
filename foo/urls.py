from django.urls import path, include
from .views import BadassListView


urlpatterns = [
    path('', BadassListView.as_view(), name='home')
]
