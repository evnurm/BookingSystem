"""BookingSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from Users import views
from Bookings.views import AddItem, Items, AllBookings


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.Index.as_view(), name="index"),
    url(r'^users/', include('Users.urls')),
    url(r'^add_item/$', AddItem.as_view(), name="add_item"),
    url(r'^items/$', Items.as_view(), name="items"),
    url(r'^bookings/$', AllBookings.as_view(), name="all_bookings")
]
