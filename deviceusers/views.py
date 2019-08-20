from rest_framework import viewsets
from .models import Device_user
from .deviceusers_serializers import DeviceUserSerializer
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.shortcuts import render, redirect, get_object_or_404
from .services.edit_device_user import edit_device_user
from attend.service.fetch_user import sync_all_user
from attend.models import Attendance


# Create your views here.
class DeviceUserApiView(viewsets.ModelViewSet):
    queryset = Device_user.objects.all()
    serializer_class = DeviceUserSerializer
#view for editing user
def device_user_edit(request):
    if request.method == "POST":
        name = request.POST.get("device_username")
        uid = request.POST.get("id")
        edit_device_user(uid,name)
        sync_all_user()
    return redirect("device-user-list")
#view for updating user
class DeviceUserUpdate(TemplateView):
    template_name = 'user_edit_form.html'
    success_url = 'device-user-edit/'
#view for showing the list of users
class DeviceUserListView(ListView):
    template_name = 'device_user_list.html'
    queryset = Device_user.objects.all()
    context_object_name = 'users'

