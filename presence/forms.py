from django.forms import ModelForm
from django import forms
from presence.models import Permit
from bootstrap3_datetime.widgets import DateTimePicker
from datetimepicker.widgets import DateTimePicker

class PermitForm(ModelForm):
    class Meta:
        model = Permit
        fields = ['presence_type', 'begin_time', 'end_time', 'reason']
        labels = {
            'presence_type':"Presence Type",
            'begin_time':'Begin of Permit Time',
            'end_time':'End of Permit Time',
            'reason':'Reason',
        }
        error_messages = {
            'presence_type': {
                'required': 'Choose the presence_type'
            },
            'begin_time' : {
                'required': "Choose The Begin of Permit Time"
            },
            'end_time' : {
                'required': "Choose The End of Permit Time"
            },
            'reason':{
                'required': "Input Your Reason"
            }
        }
        widgets = {
            'reason': forms.Textarea(attrs={ 'cols':50, 'rows': 10 })
        }