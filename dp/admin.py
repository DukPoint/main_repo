from django.contrib import admin
from .models import User, Store, Menu, Review, Payment

# Register your models here.
admin.site.register(Store)
admin.site.register(User)
admin.site.register(Menu)
admin.site.register(Payment)
