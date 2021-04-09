from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Place, Categories, Services, AvailableTime, BookedTime


class BookedTimeInline(admin.TabularInline):
    model = BookedTime


class PlaceAdmin(admin.ModelAdmin):
    inlines = [BookedTimeInline]


class UserAdmin(BaseUserAdmin):
    inlines = (BookedTimeInline,)


admin.site.register(Place, PlaceAdmin)
admin.site.register(Categories)
admin.site.register(Services)
admin.site.register(AvailableTime)
admin.site.register(BookedTime)
# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
