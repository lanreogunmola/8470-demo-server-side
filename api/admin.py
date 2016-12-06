from django.contrib import admin
from api.models import *

# Register your models here.
admin.site.register(Profile, Profile.Admin)
admin.site.register(Cloth, Cloth.Admin)

