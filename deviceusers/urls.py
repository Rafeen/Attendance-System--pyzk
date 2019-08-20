from django.conf.urls import include
from django.urls import path, re_path
from .views import DeviceUserApiView, DeviceUserUpdate, DeviceUserListView
from rest_framework import routers



router = routers.DefaultRouter()
router.register('device-users', DeviceUserApiView)


urlpatterns = [
    path('api/device-users/', include(router.urls)),
    path('device-user-edit/', DeviceUserUpdate.as_view(),name='device-user-edit'),
    path('device-user-list/', DeviceUserListView.as_view(),name='device-user-list'),


]