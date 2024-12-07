from django.contrib import admin
from .models import Slider, About, New_Arrival, Best_sellers, Discounted, Message, Cleansing, Oil, Treatment, Braiding
from .models import Product, CartItem

# Register your models here.
admin.site.register(Slider)
admin.site.register(About)
admin.site.register(New_Arrival)
admin.site.register(Best_sellers)
admin.site.register(Discounted)
admin.site.register(Message)
admin.site.register(Cleansing)
admin.site.register(Oil)
admin.site.register(Treatment)
admin.site.register(Braiding)
admin.site.register(Product)
admin.site.register(CartItem)

