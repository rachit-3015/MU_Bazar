from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Category)
admin.site.register(ads)
admin.site.register(tags)
admin.site.register(Ads_Images)
