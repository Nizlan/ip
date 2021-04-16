from django.contrib import admin
from .models import FreeServices, Equipment, UniqueQualities
from coworking.admin import PlaceInline


class FreeServicesAdmin(admin.ModelAdmin):
    inlines = [PlaceInline]
    list_display = ('free_tea', 'free_wifi', 'parking_spaces')
    actions = ["addServices", "deleteServices"]
    def addServices(self, request, queryset):
        row_update = queryset.update(free_tea=True, free_wifi=True, parking_spaces=True)

    def deleteServices(self, request, queryset):
        row_update = queryset.update(free_tea=False, free_wifi=False, parking_spaces=False)
    addServices.short_description = "Выделить всё"
    deleteServices.short_description = "Снять выделение везде"


admin.site.register(FreeServices, FreeServicesAdmin)
admin.site.register(Equipment)
admin.site.register(UniqueQualities)
