import string

from zk import ZK, const
from attend.models import Attendance
from django.shortcuts import redirect
from django.db import IntegrityError
from django.utils import timezone
from datetime import date

from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

from celery import shared_task

@shared_task
def sync_attendance():
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


        batch = []
        for attendance in attendances:

            timestamp = str(attendance.timestamp)
            timestampDate = timestamp.split(" ")
            print(attendance.timestamp)

            if timestampDate[0] == str(date.today()):
                data = Attendance(user_id=attendance.user_id, datetime=timezone.make_aware(attendance.timestamp, timezone.get_current_timezone()))
                batch.append(data)

        try:
            Attendance.objects.bulk_create(batch, ignore_conflicts=True)
            print("Creted Bulk Objects")

        except IntegrityError:
            for obj in batch:
                try:
                    obj.save()
                except IntegrityError:
                    continue

        # Test Voice: Say Thank You
        conn.test_voice()

        # re-enable device after all commands already executed
        conn.enable_device()
    except Exception as e:
        print("Process terminate : {}".format(e))
    finally:
        if conn:
            conn.disconnect()

    print("Just Executed Task")