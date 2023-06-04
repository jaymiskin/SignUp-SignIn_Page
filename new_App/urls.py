from django.urls import path
from .views import *


urlpatterns = [
    path('signin_page/', signin_page, name='signin_page'),
    path('index/', index, name='index'),
    path('', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('logout/', logout, name='logout'),
]