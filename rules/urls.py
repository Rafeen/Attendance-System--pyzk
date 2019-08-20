from django.conf.urls import include
from django.urls import path, re_path
from rest_framework import routers

from .views import OfficeRulesApiView, LateRulesApiView, RulesExceptionApiView, office_rules_get_create, create_exception, create_late_limit

router = routers.DefaultRouter()
router.register('office-rules', OfficeRulesApiView)
router.register('late-rules', LateRulesApiView)
router.register('exception-rules', RulesExceptionApiView)

urlpatterns = [
    path('api/rules/', include(router.urls)),
    path('office-rules/', office_rules_get_create, name='office-rules'),
    path('create-exception/', create_exception, name='exception'),
    path('create-late/', create_late_limit, name='late'),
]