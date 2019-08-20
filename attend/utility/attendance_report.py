from attend.models import Attendance, AttendanceReport, Device_user
from rules.models import OfficeRules
from datetime import datetime, timedelta
from django.db import IntegrityError
from django.shortcuts import get_object_or_404



def push_data():

    attendances = Attendance.objects.raw(('''select user_id_id as id ,approval_status,late_status,name,day,inTime,outTime,hour (timediff(outTime,inTime))as totalhour,minute (timediff(outTime,inTime)) as totalminute from
                                            (select user_id_id,approval_status,late_status,day,name,min(time)as inTime ,max(time)as outTime from
                                            (select user_id_id,approval_status,late_status,name,DATE(datetime)as day,TIME(datetime)as time
                                            from attend_attendance a1
                                            inner join
                                            deviceusers_device_user d1 on a1.user_id_id = d1.user_id
                                            where DATE(datetime) > '1999-02-07')as t2
                                            group by day,user_id_id)as t3
                                            order by day desc '''))

    rules = OfficeRules.objects.filter(active=True).first()
    AttendanceReport.objects.filter(date__gt=datetime.now().date()-timedelta(days=7)).delete()


    if rules :
        limit = rules.late_limit.late_limit
        total_limit = (datetime.strptime(str(rules.office_start_time), '%H:%M:%S') + timedelta(minutes=int(limit))).time()

    else:
        total_limit = False

    batch = []
    for attendance in attendances:
        total = str(attendance.totalhour)+':'+str(attendance.totalminute)
        if attendance.inTime > total_limit and total_limit != False:
            late_flag = True
        else:
            late_flag = False

        try:
            data = AttendanceReport(user=get_object_or_404(Device_user, pk=int(attendance.id)),
                                    date=attendance.day,
                                    intime=attendance.inTime.replace(second=0),
                                    outtime=attendance.outTime.replace(second=0),
                                    is_late=late_flag,
                                    total_time=total,
                                    approval_status=attendance.approval_status)
            batch.append(data)
        except:
            print("user does not exist")
    try:
        print(len(batch))
        AttendanceReport.objects.bulk_create(batch, ignore_conflicts=True)
    except IntegrityError:
        for obj in batch:
            try:
                obj.save()
            except IntegrityError:
                continue
    # Test Voice: Say Thank You
    print('done fetching')
