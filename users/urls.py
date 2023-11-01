from django.urls import path

from .views import RegisterAPI, LoginAPI

urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register_api'),
    path('login/', LoginAPI.as_view(), name='login_api')
]