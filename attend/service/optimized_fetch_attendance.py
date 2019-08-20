from zk import ZK, const
from django.db import IntegrityError
from django.utils import timezone
from django.utils.dateparse import parse_datetime
from django.utils.timezone import is_aware, make_aware
from django.shortcuts import get_object_or_404

from attend.models import Attendance
from deviceusers.models import Device_user

from attend.utility.attendance_report import push_data



def sync_new_attendances():
    push_data()
    conn = None
    # create ZK instance
    zk = ZK('192.168.0.99', port=4370, timeout=5, password=0, force_udp=False, ommit_ping=False)
    try:
        # connect to device
        conn = zk.connect()
        # disable device, this method ensures no activity on the device while the process is run
        conn.disable_device()
        # another commands will be here!
        # Example: Get All Users
        attendances = conn.get_attendance()

        latest=Attendance.objects.latest('id')
        batch = []
        for attendance in attendances:
          # timestamp = str(attendance.timestamp)
            timestampDate = parse_datetime(str(attendance.timestamp))
            if not is_aware(timestampDate):
                timestampDate = make_aware(timestampDate)

            if timestampDate >= latest.datetime:
                try:
                    data = Attendance(user_id=get_object_or_404(Device_user, pk=int(attendance.user_id)),
                                      datetime=timezone.make_aware(attendance.timestamp,
                                                                   timezone.get_current_timezone()))
                    batch.append(data)
                except:
                    print("user does not exist")
        try:
            print(len(batch))
            Attendance.objects.bulk_create(batch, ignore_conflicts=True)
        except IntegrityError:
            for obj in batch:
                try:
                    obj.save()
                except IntegrityError:
                    continue
        # Test Voice: Say Thank You
        print('done fetching')
        conn.test_voice()
        # re-enable device after all commands already executed
        conn.enable_device()
    except Exception as e:
        print("Process terminate : {}".format(e))
    finally:
        if conn:
            conn.disconnect()
