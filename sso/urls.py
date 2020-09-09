from django.conf.urls import url
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from .views import UserRegister

urlpatterns = [
    url(r'^register/', UserRegister.as_view()),
    url(r'^login/', obtain_jwt_token),
]