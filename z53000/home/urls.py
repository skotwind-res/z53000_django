from django.urls import path
from .views import *


urlpatterns = [
    path('', home),
    path('news/', news),
    path('api/', my_api),
    path('contact/', contact),
    path('add_new/', add_new),
    path('pidor_update/', pidor_update)
]