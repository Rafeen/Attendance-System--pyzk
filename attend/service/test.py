import string

from zk import ZK, const
from deviceusers.models import Device_user
from django.utils import timezone
from django.shortcuts import get_object_or_404
from attend.models import Attendance




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
    users=  conn.get_users()
    batch=[]
    for i in attendances:
        try:
            data = Attendance(user_id=get_object_or_404(Device_user, pk=int(i.user_id)),
                              datetime=timezone.make_aware(i.timestamp,
                                                           timezone.get_current_timezone()))
            batch.append(data)
        except:
            pass






    # Test Voice: Say Thank You
    print(batch)
    print(len(batch))
    Attendance.objects.bulk_create(batch, ignore_conflicts=True)
    conn.test_voice()

    # re-enable device after all commands already executed
    conn.enable_device()
except Exception as e:
    print("Process terminate : {}".format(e))
finally:
    if conn:
        conn.disconnect()

print("Just Executed Task")