"""Attendance URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_swagger.views import get_swagger_view
from rest_framework.documentation import include_docs_urls
from users import views
from attend.views import sync_attendance_all, sync_user
# from attend.views import Manual_date_input
from deviceusers.views import device_user_edit
schema_view = get_swagger_view(title='Attendance API')
# from .views import DeviceUserListView
from deviceusers.views import DeviceUserListView
from attend.views import all_transaction,approvalList
from attend.views import all_attendance_report

urlpatterns = [
    path('admin/', admin.site.urls),


    # Webapp url
    path('',views.index,name='index'),
    path('logout/', views.user_logout, name='logout'),
    path('approval-list/', approvalList, name='approval-list'),


    # service url
    path('sync-user/', sync_user, name='sync-user'),
    path('sync-attendance/', sync_attendance_all, name='sync-attendance'),
    path('edit/', device_user_edit, name='user-edit'),




    # App url
    re_path('', include('users.urls')),
    re_path('', include('attend.urls')),
    re_path('', include('deviceusers.urls')),
    re_path('', include('rules.urls')),

    # API Documentation url
    path('api/swagger-doc', schema_view),
    path('api/core-doc', include_docs_urls(title='Coredoc Attendance API')),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)