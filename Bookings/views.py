from django.shortcuts import render
from django.http.response import HttpResponseForbidden
from django.views import View
from django.db.models import Count
from datetime import datetime
from .forms import AddItem as AddItemForm
from .models import Item, Booking


# Create your views here.
class AddItem(View):
    def get(self, request):
        return render(request, "Bookings/add_item.html", {'form': AddItemForm})

    def post(self, request):
        form = AddItemForm(request.POST)
        if form.is_valid():
            item = form.save()
            return render(request, "Bookings/add_item.html", {'form': form, 'success': True})


class Items(View):
    def get(self, request):
        bookings = [x['item__title'] for x in request.user.account.bookings.all().values('item__title')]
        #  available = item that has copies available and is not yet booked by the user.
        available_items = Item.objects.filter(available=True)\
            .values('title', 'category__title')\
            .annotate(qt=Count('title'))\
            .filter(qt__gt=0)\
            .exclude(title__in=bookings)
        return render(request, "Bookings/available_items.html", {'items': available_items})

    def post(self, request):
        item_title = request.POST['item']

        # Fetch reference to first available item with given title.
        item = Item.objects.filter(title=item_title, available=True).first()
        booking = Booking(item=item,
                          user=request.user.account,
                          issuing_time=datetime.now(),
                          expiry_date=datetime.now(),
                          returned=False)

        item.available = False
        item.save()
        booking.save()
        available_items = Item.objects.filter(available=True).values('title').annotate(qt=Count('title')).filter(qt__gt=0)
        return render(request, "Bookings/available_items.html", {'items': available_items})


class AllBookings(View):
    def get(self, request):
        if not request.user.is_superuser:
            return render(request, "Bookings/all_bookings.html", {'bookings': Booking.objects.all()})
        else:
            return HttpResponseForbidden
