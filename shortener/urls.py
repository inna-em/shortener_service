from django.contrib import admin
from django.urls import path, include
from .views import index_view, decode_view


urlpatterns = [
    path('', index_view),
    path('<str:code>/', decode_view, name='decode'),
]
