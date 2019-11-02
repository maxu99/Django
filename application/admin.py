from django.contrib import admin

# Register your models here.
from application.models import City, Owner_Ship, Reservation, Date_Rent

admin.site.register(City)
admin.site.register(Owner_Ship)
admin.site.register(Reservation)
admin.site.register(Date_Rent)

