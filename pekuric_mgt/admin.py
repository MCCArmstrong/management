from django.contrib import admin

from .models import caviet, unicornabout, unicornService, DailyTask, CustomerPurchaseForm

admin.site.register(caviet),
admin.site.register(CustomerPurchaseForm),
admin.site.register(unicornService),
admin.site.register(unicornabout),
admin.site.register(DailyTask)
