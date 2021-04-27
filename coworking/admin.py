from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from import_export.widgets import ForeignKeyWidget

from .models import Place, Categories, BookedTime, Reservation, AvailableTime, Comments, GroupOfPeople
from import_export import resources, fields
from import_export.admin import ImportExportActionModelAdmin

# class BookedTimeInline(admin.TabularInline):
#     model = BookedTime


class PlaceInline(admin.TabularInline):
    model = Place


class ReservationInline(admin.TabularInline):
    model = Reservation


class PlaceResource(resources.ModelResource):
    category = fields.Field(column_name='categories', attribute='categories', widget=ForeignKeyWidget(Categories, 'title'))

    class Meta:
        model = Place


class PlaceAdmin(ImportExportActionModelAdmin):
    resource_class = PlaceResource
    # inlines = [ReservationInline]
    list_display = ('name', 'location', 'price')
    search_fields = ('name',)
    list_filter = ('categories',)


# class ReservationAdmin(admin.ModelAdmin):
#     inlines = [BookedTimeInline]


class UserAdmin(BaseUserAdmin):
    inlines = (ReservationInline,)


class CategoriesAdmin(admin.ModelAdmin):
    search_fields = ('title',)


admin.site.register(Place, PlaceAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(AvailableTime)
admin.site.register(BookedTime)
admin.site.register(Reservation)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Comments)
admin.site.register(GroupOfPeople)
