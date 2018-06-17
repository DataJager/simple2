from django.contrib import admin
from .models import Vendor, Listing, Task

admin.site.register(Vendor)
admin.site.register(Listing)
admin.site.register(Task)
