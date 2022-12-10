
from django.contrib import admin
from django.urls import path
from.views import index
urlpatterns = [
    path('order/<str:param>', index),
    # path('', index),
    # path('order/<str:param>', index),
]
