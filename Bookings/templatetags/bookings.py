from django import template
from Bookings.models import Booking
from datetime import datetime

register = template.Library()


@register.inclusion_tag('Bookings/bookings_table.html', takes_context=False)
def bookings_table(user):
    bookings = Booking.objects.filter(user=user.account, expiry_date__gt=datetime.today())
    return {'bookings': bookings}


@register.inclusion_tag('Bookings/bookings_table.html', takes_context=False)
def past_bookings_table(user):
    bookings = Booking.objects.filter(user=user.account, expiry_date__lte=datetime.today())
    return {'bookings': bookings}
