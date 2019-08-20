from django.db import models

# Create your models here.
class RuleException(models.Model):
    name = models.CharField(max_length=255, default='Not Specified')
    start_date = models.DateField()
    end_date =  models.DateField()

    office_start_time = models.TimeField(null=True)
    office_end_time = models.TimeField(null=True)

    def __str__(self):
        return self.name


class LateRule(models.Model):
    late_limit = models.IntegerField(default= 0, blank=True)

    def __str__(self):
        return str(self.late_limit)


class OfficeRules(models.Model):
    name = models.CharField(max_length=255)
    office_start_time = models.TimeField(null=True)
    office_end_time = models.TimeField(null=True)
    exceptions = models.ForeignKey(RuleException, blank=True, null=True, on_delete=models.CASCADE)
    late_limit = models.OneToOneField(LateRule, null=True, on_delete=models.CASCADE)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name





