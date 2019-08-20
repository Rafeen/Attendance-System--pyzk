from zk import ZK, const

def edit_device_user(uid,name):
    conn = None
    zk = ZK('192.168.0.99', port=4370, timeout=5, password=0, force_udp=False, ommit_ping=False)
    try:
        conn = zk.connect()
        # your code here
        conn.test_voice()
        print('Enabling device ...')
        conn.enable_device()
        print('Enabled ...')
        conn.set_user(uid=int(uid), name=name, privilege=const.USER_DEFAULT, user_id=uid)
        users = conn.get_users()
        print('all user fetched ...')
        for user in users:
            #
                print(user)

    except Exception as e:
        print("Process terminate : {}".format(e))
    finally:
        if conn:
            conn.disconnect()

