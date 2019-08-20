from django.db import models
from deviceusers.models import Device_user

class Attendance(models.Model):
    class Meta:
        unique_together = ['user_id', 'datetime']
        ordering = ('-datetime',)

    Auto = 'Auto'
    Manual = 'Manual'
    Ontime = 'On Time'
    Late = 'Late'
    APPROVAL_CHOICES = (
        (Auto,'Auto'),
        (Manual,'Manual')
    )
    LATE_CHOICES = (
        (Ontime,'On Time'),
        (Late,'Late')
    )

    user_id = models.ForeignKey(Device_user, null=True, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    approval_status = models.CharField(max_length=20, choices=APPROVAL_CHOICES, default=Auto)
    late_status = models.CharField(max_length=20, choices=LATE_CHOICES, default=Ontime)

    def __str__(self):
        return ("user: " + str(self.user_id) + '  ' + "Date: " +str(self.datetime.strftime("%A %d %b %Y %H:%M:%S")))

#Approval Table model
class ApprovalTable(models.Model):
    class Meta:
        unique_together = ['user_id', 'datetime']
        ordering = ('-datetime',)


    user_id = models.ForeignKey(Device_user, null=True, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    reason = models.TextField()

    Approved = 'Approved'
    Pending = 'Pending'
    Rejected = 'Rejected'
    STATUS_CHOICES = (
        (Approved, 'Approved'),  # First element is value, Second element is human readable representation of the value
        (Pending, 'Pending'),
        (Rejected, 'Rejected'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=Pending)
    def __str__(self):
        return ("User Name: " + str(self.user_id) + '       ' + "Date: " +str(self.datetime))

#model for approval history
class ApprovalHistory(models.Model):

    # approval_id = models.ForeignKey(ApprovalTable, null=True, on_delete=models.CASCADE)
    user_id = models.IntegerField()
    datetime = models.DateTimeField()
    reason = models.TextField()
    action_type = models.TextField()
    action_time = models.DateTimeField()
    action_by = models.TextField()
    def __str__(self):
        return ("Approval Type: " + str(self.type) + '       ' + "Date: " +str(self.datetime))



class AttendanceReport(models.Model):
    class Meta:
        unique_together = ['user', 'date']
        ordering = ('-date',)

    date = models.DateField()
    user = models.ForeignKey(Device_user, null=True, on_delete=models.CASCADE)
    intime = models.TimeField()
    outtime = models.TimeField()
    total_time = models.CharField(max_length=255)
    approval_status = models.CharField(max_length=255)
    is_late = models.BooleanField(default=False)
    remarks = models.TextField(default="",blank=True)



    def __str__(self):
        return (str(self.user.name) + '       ' + "Date: " +str(self.date))



