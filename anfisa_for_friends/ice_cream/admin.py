from django.contrib import admin

# Register your models here.
from .models import Category, Wrapper, IceCream, Topping

admin.site.register(Category)
admin.site.register(Wrapper)
admin.site.register(IceCream)
admin.site.register(Topping)
