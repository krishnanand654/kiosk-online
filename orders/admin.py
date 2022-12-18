from django.contrib import admin
from .models import Category, RegularPizza, SicilianPizza, Toppings, Sub, Pasta,  DinnerPlatters, UserOrder, SavedCarts, Drinks, Snacks
from tinymce.widgets import TinyMCE
from django.db import models

class CategoryAdmin(admin.ModelAdmin):
    formfield_overrides = {
            models.TextField: {'widget': TinyMCE()},
            }

class RegularPizzaAdmin(admin.ModelAdmin):
    formfield_overrides = {
            models.TextField: {'widget': TinyMCE()},
            }

class SicilianPizzaAdmin(admin.ModelAdmin):
    formfield_overrides = {
            models.TextField: {'widget': TinyMCE()},
            }


admin.site.register(Category,CategoryAdmin)
admin.site.register(RegularPizza, RegularPizzaAdmin)
admin.site.register(SicilianPizza, SicilianPizzaAdmin)
admin.site.register(Toppings)
admin.site.register(Sub)
admin.site.register(Pasta)
admin.site.register(Snacks)
admin.site.register(DinnerPlatters)
admin.site.register(Drinks)
admin.site.register(UserOrder)
admin.site.register(SavedCarts)
