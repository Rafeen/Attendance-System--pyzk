from django.urls import resolve

def get_current_path(req):
    path = resolve(req.path_info).url_name
    return path