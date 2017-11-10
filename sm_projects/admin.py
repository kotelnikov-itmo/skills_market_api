from django.contrib import admin
from .models import Project, Assignment
# Register your models here.

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    pass