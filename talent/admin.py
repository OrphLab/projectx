from django.contrib import admin

# Register your models here.
from .models import Talent


@admin.register(Talent)                     
class TalentAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email')

