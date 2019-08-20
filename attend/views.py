from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Attendance, ApprovalTable, Device_user, AttendanceReport,ApprovalHistory
from .attend_serializers import AttendanceSerializer, ApprovalTableSerializer, AttendanceReportSerializer
from .forms import ManualDateInputForm
from django.views.generic import CreateView
from django.utils.timezone import datetime #important if using timezones
from django.utils import timezone
import datetime
from datetime import date
from datetime import datetime
from django.db.models import Max
from django.http import HttpResponseRedirect
from .service.optimized_fetch_attendance import sync_new_attendances
from .service.fetch_user import sync_all_user
from django.utils.timezone import is_aware, make_aware
from datetime import datetime, timedelta
from django.shortcuts import get_object_or_404



# Create your API views here.
class AttendanceApiView(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

class ApprovalTableApiView(viewsets.ModelViewSet):
    queryset = ApprovalTable.objects.all()
    serializer_class = ApprovalTableSerializer

class AttendanceReportApiView(viewsets.ModelViewSet):
    queryset = AttendanceReport.objects.all()
    serializer_class = AttendanceReportSerializer


def manual_attendance(request):
    if request.method == 'GET':
        users = Device_user.objects.all()

        context = {

            'users': users
        }
        return redirect(request, 'manual-attendance', context)

    if request.POST:
        manual_entry = ApprovalTable()
        entry_date = datetime.strptime(request.POST.get("date"), '%Y/%m/%d').date()
        print(entry_date)
        entry_time = datetime.strptime(request.POST.get("time"), '%H:%M:%S').time()
        combined = datetime.combine(entry_date, entry_time)
        combined = make_aware(combined)
        manual_entry.datetime = combined
        manual_entry.user_id = Device_user.objects.get(user_id=int(request.POST.get('user_id')))
        manual_entry.reason = request.POST.get('reason')

        manual_entry.save()

    return redirect('/')




def all_transaction(request):
    attendance =Attendance.objects.all()
    context = {
        'attendance':attendance
    }
    return render(request, 'all_transactions.html', context)

#view for approvalList
def approvalList(request):
    approval = ApprovalTable.objects.all()
    context = {
        'approval':approval
    }
    # if request.POST.get('Approved'):
    #     approve = ApprovalTable()
    #     approve.status = 'Approved'
    #     print("approved")
    #     approve.save(update_fields=["status"])
    return render(request, 'Approval_latest.html', context)

def attendance_approved(request):
   id = request.POST.get("id")
   print(id)
   instance = ApprovalTable.objects.get(id=id)
   print(instance.user_id.user_id)
   if instance.status != "Approved":
    instance.status = "Approved"
    instance.save()
    approval_history = ApprovalHistory()
    approval_history.user_id = instance.user_id.user_id
    approval_history.datetime = instance.datetime
    approval_history.reason = instance.reason
    approval_history.action_by = "Admin"
    approval_history.action_type = instance.status
    approval_history.action_time = datetime.now()
    approval_history.save()
   # attendance = Attendance()
   # attendance.user_id = instance.user_id
   # attendance.datetime = instance.datetime
   # attendance.approval_status = 'Manual'
   # attendance.save()

   return render(request, 'Approval_latest.html')

def attendance_declined(request):
   id = request.POST.get("id")
   print(id)
   instance = ApprovalTable.objects.get(id=id)
   if instance.status != "Rejected":
    instance.status = "Rejected"
    instance.save()
   approval_history = ApprovalHistory()
   approval_history.user_id = instance.user_id.user_id
   approval_history.datetime = instance.datetime
   approval_history.reason = instance.reason
   approval_history.action_by = "Admin"
   approval_history.action_type = instance.status
   approval_history.action_time = datetime.now()
   approval_history.save()
   return render(request, 'Approval_latest.html')



#view for attendance reports
def today_report(request):

    attendance = AttendanceReport.objects.filter(date=date.today())

    total_users = Device_user.objects.all().count()
    present = len(list(attendance))

    users = Device_user.objects.all()
    print(attendance)

    context = {
        'attendance': attendance,
        'total_users': total_users,
        'absent' : total_users-present,
        'users': users
    }
    return render(request, 'today_report.html', context)

def all_attendance_report(request):
    if request.POST:
        date = datetime.strptime(request.POST.get("date"), '%Y/%m/%d').date()
        attendance = AttendanceReport.objects.filter(date=date)
    else:
        attendance = None
    users = Device_user.objects.all()
    context = {
        'attendance':attendance,
        'users': users
    }
    return render(request, 'all_attendance_report.html', context)

def user_report_attendance(request):

    if request.method == 'GET':
        print('currently in get')
        user_attendance = AttendanceReport.objects.filter(date__gte=datetime.now()-timedelta(days=7))

    user_id = '0'
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        user_attendance = AttendanceReport.objects.filter(user_id=user_id)

    users = Device_user.objects.all()
    context = {
        'user_attendance': user_attendance,
        'users': users,
        'uid': int(user_id)
    }
    return render(request, 'user_attendance_report.html', context)



def sync_attendance_all(request):
    sync_new_attendances()
    referer = request.META.get('HTTP_REFERER')
    if referer is None:
        return redirect('/')
    return redirect(referer)

def sync_user(request):
    sync_all_user()
    referer = request.META.get('HTTP_REFERER')
    if referer is None:
        return redirect('/')
    return redirect(referer)


