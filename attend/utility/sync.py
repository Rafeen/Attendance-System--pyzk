from attend.service.fetch_user import sync_all_user
from attend.service.optimized_fetch_attendance import sync_new_attendances

def sync_all():
    sync_new_attendances()
    sync_all_user()
