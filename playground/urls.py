from django.urls import path
from . import views

# NOTE: URLConf

urlpatterns = [
   path('hello/', views.say_hello),
]
