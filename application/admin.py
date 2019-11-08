from django.contrib import admin

# Register your models here.
from application.models import City, Owner_Ship, Reservation, Date_Rent


class Date_Rent_Inline(admin.TabularInline):
    model = Date_Rent
    fk_name = "owner_ship"
    max_num = 7


class OwnerShipAdmin(admin.ModelAdmin):
    inlines = [Date_Rent_Inline, ]


admin.site.register(City)
# admin.site.register(Owner_Ship)
admin.site.register(Reservation)
admin.site.register(Owner_Ship, OwnerShipAdmin)

