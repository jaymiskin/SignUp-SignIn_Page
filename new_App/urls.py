from django.urls import path
from .views import *


urlpatterns = [
    path('', signup, name='signup'),
    path('signin_page/', signin_page, name='signin_page'),
    path('index/', index, name='index'),
    path('profile_page/', profile_page, name='profile_page'),
    path('update_profile_page/',update_profile_page,name='update_profile_page'),


    path('update_profile_function/',update_profile_function,name='update_profile_function'),
    path('signin/', signin, name='signin'),
    path('profile_update/', profile_update, name='profile_update'),
    path('profile_data/', profile_data, name='profile_data'),
    path('logout/', logout, name='logout'),
    path('delete_account_function/',delete_account_function,name='delete_account_function'),
]