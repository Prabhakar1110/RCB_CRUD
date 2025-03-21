from django.contrib import admin
from .models import *

class PlayerAdmin(admin.ModelAdmin):
    list_display = ("id", "pk", "name", "age", "role")

admin.site.register(Player, PlayerAdmin)
admin.site.register(Food)
