from django.shortcuts import render
from .forms import ContractorDetailsForm
from django.views.generic.edit import FormView
# Create your views here.

class ContractorContactView(FormView):
    template_name = 'jobsolutely/contractor-signup.html'
    form_class = ContractorDetailsForm
    success_url = '/contractor/card-details/'

    # going to override this later so include just now
    def form_valid(self, form):
        return super().form_valid(form)


