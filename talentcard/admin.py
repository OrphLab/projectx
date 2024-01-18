from django.contrib import admin
from .models import TalentCard, Skill, UserSkill, Country



class UserSkillInline(admin.TabularInline): #Allows to edit UserSkill in TalentCard
    model = UserSkill
    

# Register your models here.

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('country_code',)
    list_filter = ('country_code',)
    search_fields = ('country_code',)
    ordering = ('country_code',)

@admin.register(TalentCard)
class TalentCardAdmin(admin.ModelAdmin):
    inlines = [UserSkillInline] #Allows to edit UserSkill,  in TalentCard
    list_display = ('talent','industry', 'expertice', 'origin_country')
    list_filter = ('talent','industry', 'expertice', 'origin_country')
    search_fields = ('talent','industry', 'expertice', 'origin_country')
    ordering = ('industry', 'expertice', 'origin_country')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(UserSkill)
class UserSkillAdmin(admin.ModelAdmin):
    list_display = ('skill', 'skill_level', 'skill_years')
    list_filter = ( 'skill', 'skill_level', 'skill_years')
    search_fields = ('skill', 'skill_level', 'skill_years')
    ordering = ('skill', 'skill_level', 'skill_years')


    