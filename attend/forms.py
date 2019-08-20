from django import forms
from .models import ApprovalTable




class ManualDateInputForm(forms.ModelForm):
    class Meta:
        model = ApprovalTable
        fields = ('user_id', 'datetime', 'reason')

        widgets = {
            'datetime': forms.DateTimeInput()
        }

