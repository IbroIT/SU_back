from .models import RequisitiesForeign, requirement, BankRequisites, Fee, Contacts, FeeForeign, Contacts, ContactForeign, RequisitiesForeign, FAQ
from django.contrib import admin

admin.site.register(Fee)
admin.site.register(Contacts)
admin.site.register(FeeForeign)
admin.site.register(RequisitiesForeign)
admin.site.register(ContactForeign)
admin.site.register(BankRequisites)
admin.site.register(requirement)
admin.site.register(FAQ)

