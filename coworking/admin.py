from django.contrib import admin

from .models import Place, Category


class PlaceAdmin(admin.ModelAdmin):
    search_fields = ('name', 'location')


admin.site.register(Place, PlaceAdmin)
admin.site.register(Category)
