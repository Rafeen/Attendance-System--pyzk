from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from users.views import UserViewSet, user_login, register

from django.urls import path, re_path
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token


router = routers.DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('api/users/', include(router.urls)),
    path('token/obtain/', obtain_jwt_token),
    path('token/refresh/', refresh_jwt_token),
    path('token/verify/', verify_jwt_token),
    re_path(r'^auth/', include('rest_auth.urls')),

    path('login/', user_login,name='user_login'),
    path('register/', register,name='register'),

]