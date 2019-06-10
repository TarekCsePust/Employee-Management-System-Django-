from django.forms import ModelForm
from django import forms
from .models import Employee
import datetime

from django.utils.translation import gettext_lazy as _
now = datetime.datetime.now()
YEARS= [x for x in range(1900,now.year+1)]
class EmployeeForm(ModelForm):

    birthdate = forms.DateField(widget=forms.SelectDateWidget(years=YEARS))
    class Meta:
        model = Employee
        fields = [
            "name",
            "post",
            "address",
            "birthdate",
            "mobile_no",
            "image",
            
            "active"
            
        ]

        

    		