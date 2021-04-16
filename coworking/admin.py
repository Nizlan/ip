from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Place, Categories, BookedTime, Reservation, AvailableTime, Comments


class BookedTimeInline(admin.TabularInline):
    model = BookedTime


class ReservationInline(admin.TabularInline):
    model = Reservation


class PlaceAdmin(admin.ModelAdmin):
    inlines = [ReservationInline]


class ReservationAdmin(admin.ModelAdmin):
    inlines = [BookedTimeInline]


class UserAdmin(BaseUserAdmin):
    inlines = (ReservationInline,)


admin.site.register(Place, PlaceAdmin)
admin.site.register(Categories)
admin.site.register(AvailableTime)
admin.site.register(BookedTime)
admin.site.register(Reservation, ReservationAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Comments)
