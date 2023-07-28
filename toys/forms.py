from django import forms
from .models import Toys

class DateInput(forms.DateInput):
    input_type = 'date'

class ToysModelForm(forms.ModelForm):
    tags = forms.CharField(required=False)

    class Meta:
        model = Toys
        fields = "__all__"
        widgets = {
            'date': DateInput(),
        }
