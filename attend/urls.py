from django.conf.urls import include
from django.urls import path, re_path
from .views import AttendanceApiView,ApprovalTableApiView, AttendanceReportApiView
from rest_framework import routers

from.views import today_report,all_transaction,all_attendance_report,user_report_attendance,manual_attendance,approvalList,attendance_approved,attendance_declined



router = routers.DefaultRouter()
router.register('approval-table', ApprovalTableApiView)
router.register('attendance', AttendanceApiView)
router.register('attendance-report', AttendanceReportApiView)


urlpatterns = [
    path('api/attendance/', include(router.urls)),
    path('today/', today_report, name="today"),
    path('all-transaction/', all_transaction, name='all-transaction'),
    path('all-attendance-report/', all_attendance_report, name='all-attendance-report'),
    path('user-attendance-report/', user_report_attendance, name='user-attendance-report'),
    path('manual-attendance/', manual_attendance, name='manual-attendance'),
    path('approval-list/', approvalList, name='approval-list'),
    path('attendance/approved/', attendance_approved, name='attendance-approved'),
    path('attendance/declined/', attendance_declined, name='attendance-declined')
]
