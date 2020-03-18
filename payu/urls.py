from django.urls import path
from .views import *


urlpatterns =[
    path('', index, name='home'),
    path('payment', Home, name='payment'),
    path('payment/success', success, name='success'),
    path('payment/failure', failure, name='failure'),
]