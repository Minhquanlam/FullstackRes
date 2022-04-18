from django.contrib import admin
from rectAPI.models import order, pizza, drink, hamburger
# Register your models here.

admin.site.register(pizza)
admin.site.register(drink)
admin.site.register(hamburger)
