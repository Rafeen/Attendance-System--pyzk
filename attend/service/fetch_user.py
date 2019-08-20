from zk import ZK, const
from deviceusers.models import Device_user
from django.http import HttpResponse
from django.shortcuts import redirect
from django.db import IntegrityError

def sync_all_user():
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
        users = conn.get_users()
        print(users)
        formData = Device_user()

        for user in users:
            name = user.name
            password = user.password
            user_id = user.user_id

            formData.name = name
            formData.password = password
            formData.user_id = user_id

            formData.save()

        # Test Voice: Say Thank You
        conn.test_voice()

        # re-enable device after all commands already executed
        conn.enable_device()
    except Exception as e:
        print("Process terminate : {}".format(e))
    finally:
        if conn:
            conn.disconnect()

