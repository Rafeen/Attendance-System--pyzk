from rest_framework import serializers
from .models import OfficeRules, LateRule, RuleException

class OfficeRulesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OfficeRules
        fields = '__all__'

class LateRulesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LateRule
        fields = "__all__"

class RulesExceptionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RuleException
        fields = "__all__"