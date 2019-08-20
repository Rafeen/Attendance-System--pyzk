from rest_framework import serializers
from attend.models import Attendance, ApprovalTable, AttendanceReport

#attendance serializer
class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ('url','user_id', 'datetime')

#approvalTable serializer
class ApprovalTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApprovalTable
        fields = ('url', 'user_id', 'datetime')

#attendance report serializer
class AttendanceReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceReport
        fields = ('url', 'user', 'date', 'intime', 'outtime', 'is_late', 'total_time', 'approval_status')
