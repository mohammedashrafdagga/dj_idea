from django.urls import path
from . import views


app_name = 'user_app'
urlpatterns = [
    path('', views.main, name='main_fun'),
    path('sign-up', views.sign_up, name='sgin_up')
]
