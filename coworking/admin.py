from django.contrib import admin

from .models import Place, Categories, Services, AvailableTime, BookedTime


class BookedTimeInline(admin.TabularInline):
    model = BookedTime


class PlaceAdmin(admin.ModelAdmin):
    inlines = [BookedTimeInline]


admin.site.register(Place, PlaceAdmin)
admin.site.register(Categories)
admin.site.register(Services)
admin.site.register(AvailableTime)
admin.site.register(BookedTime)
