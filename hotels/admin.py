from django.contrib import admin
from .models import City, Hotel, ApartmentType


admin.site.register(City)


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('has_perking', 'has_wifi', 'has_pool', 'stars', 'city',)
    list_filter = ('city',)


@admin.register(ApartmentType)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('hotel', 'room', 'price',)
    list_filter = ('hotel',)
