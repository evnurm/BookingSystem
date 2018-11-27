from django.db import models
from Users.models import Account


class Period(models.Model):
    duration = models.DurationField(blank=False)


class ItemCategory(models.Model):
    title = models.CharField(max_length=32, blank=False, unique=True)

    def __str__(self):
        return self.title


class Item(models.Model):
    title = models.CharField(max_length=127, blank=False)
    available = models.BooleanField(default=True)
    category = models.ForeignKey(ItemCategory, on_delete=models.DO_NOTHING, related_name="items")

    def __str__(self):
        return self.title + "_" + str(self.pk)


class Booking(models.Model):
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING, related_name="bookings")
    user = models.ForeignKey(Account, on_delete=models.DO_NOTHING, related_name="bookings")
    issuing_time = models.DateField(blank=False)
    expiry_date = models.DateField(blank=False)
    delivered = models.BooleanField(blank=False, default=False)
    returned = models.BooleanField(blank=False, default=False)

    def confirm_return(self):
        self.returned = True
        self.item.available = True
        self.save()
        self.item.save()
