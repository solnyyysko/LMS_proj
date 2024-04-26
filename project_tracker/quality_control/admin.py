from django.contrib import admin
from .models import BugReport, FeatureRequest

@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'task', 'priority', 'status', 'created_at', 'updated_at')
    list_filter = ('project', 'priority', 'status')
    search_fields = ('title', 'description')
    list_editable = ('status',)
    readonly_fields = ('project', 'task', 'created_at', 'updated_at')

@admin.register(FeatureRequest)
class FeatureRequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'task', 'priority', 'status', 'created_at', 'updated_at')
    list_filter = ('project', 'priority', 'status')
    search_fields = ('title', 'description')
    list_editable = ('status',)
    readonly_fields = ('project', 'task', 'created_at', 'updated_at')