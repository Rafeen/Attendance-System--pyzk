from django.shortcuts import render, redirect
from rest_framework import viewsets
from .rules_serializers import OfficeRulesSerializer, LateRulesSerializer, RulesExceptionSerializer
from django.views.generic import CreateView
from .forms import OfficeRulesForm,LateRuleForm
from .models import OfficeRules, RuleException, LateRule
from datetime import datetime


# Create your views here.
class OfficeRulesApiView(viewsets.ModelViewSet):
    queryset = OfficeRules.objects.all()
    serializer_class = OfficeRulesSerializer

class LateRulesApiView(viewsets.ModelViewSet):
    queryset = LateRule.objects.all()
    serializer_class = LateRulesSerializer

class RulesExceptionApiView(viewsets.ModelViewSet):
    queryset = RuleException.objects.all()
    serializer_class = RulesExceptionSerializer

#renders rule.html and takes office rule input
def office_rules_get_create(request):
    if request.POST:

        office = OfficeRules()

        office.name = request.POST.get("name")
        office.office_start_time = datetime.strptime(request.POST.get("start"), '%H:%M:%S').time()
        office.office_end_time = datetime.strptime(request.POST.get("end"), '%H:%M:%S').time()

        if int(request.POST.get("exception")) > 0 :
            office.exceptions = RuleException.objects.get(id=int(request.POST.get("exception")))

        if int(request.POST.get("late")):
            office.late_limit = LateRule.objects.get(id = int(request.POST.get("late")))

        office.save()
        print('created office rule')

        return redirect('office-rules')

    exception = RuleException.objects.all()
    late = LateRule.objects.all()

    context = {
        'exceptions': exception,
        'late_times': late
    }

    return render(request, 'rule.html', context)

def create_exception(request):
    if request.POST:
        exception = RuleException()

        exception.name = request.POST.get("exception_name")
        exception.start_date = datetime.strptime(request.POST.get("start_date"), '%m-%d-%Y').date()
        exception.end_date = datetime.strptime(request.POST.get("end_date"), '%m-%d-%Y').date()
        exception.office_start_time = datetime.strptime(request.POST.get("start_time"), '%H:%M:%S').time()
        exception.office_end_time = datetime.strptime(request.POST.get("end_time"), '%H:%M:%S').time()

        exception.save()
        print('created office rule')

        return redirect('/')

    return redirect('office-rules')


def create_late_limit(request):
    if request.POST:
        late = LateRule()

        late.late_limit = int(request.POST.get('late'))

        late.save()
        print('created office rule')

        return redirect('office-rules')

    return redirect('office-rules')



