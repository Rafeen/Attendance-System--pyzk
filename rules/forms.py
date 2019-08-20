from django import forms
from .models import OfficeRules,LateRule, RuleException



class OfficeRulesForm(forms.ModelForm):
    class Meta:
        model = OfficeRules
        fields = ('__all__')

class LateRuleForm(forms.ModelForm):
    class Meta:
        model = LateRule
        fields = ('late_limit',)