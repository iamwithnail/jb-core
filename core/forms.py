from django import forms
from .models import ContractorContactDetails


class ContractorDetailsForm(forms.ModelForm):
    class Meta:
        model = ContractorContactDetails
        exclude = ['contractor']
