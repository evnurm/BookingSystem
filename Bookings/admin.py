from django.contrib import admin
from .models import Booking, Item, Period, ItemCategory
# Register your models here.
admin.site.register(Booking)
admin.site.register(Item)
admin.site.register(Period)
admin.site.register(ItemCategory)