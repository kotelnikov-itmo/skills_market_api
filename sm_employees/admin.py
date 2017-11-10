from django.contrib import admin
from .models import Employee, Position, PositionHistory
from sm_skills.models import SkillHistory
# Register your models here.


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    pass


class SkillHistoryInline(admin.TabularInline):
    extra = 2
    model = SkillHistory


class PositionHistoryInline(admin.TabularInline):
    extra = 2
    model = PositionHistory


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    inlines = [SkillHistoryInline, PositionHistoryInline]
