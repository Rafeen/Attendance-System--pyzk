from django.contrib import admin
from .models import OfficeRules, LateRule, RuleException

# Register your models here.
admin.site.register(LateRule)
admin.site.register(RuleException)
admin.site.register(OfficeRules)
