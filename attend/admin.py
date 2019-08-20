from django.contrib import admin
from .models import Attendance, ApprovalTable, AttendanceReport

# Register your models here.
admin.site.register(Attendance)
admin.site.register(ApprovalTable)
admin.site.register(AttendanceReport)
