from django.contrib import admin

from .models import (
    Role,
    ContactDetails,
    Contractor,
    Hirer,
    HirerContactDetails
)

admin.site.register(Role)
admin.site.register(ContactDetails)
admin.site.register(Contractor)
admin.site.register(Hirer)
admin.site.register(HirerContactDetails)