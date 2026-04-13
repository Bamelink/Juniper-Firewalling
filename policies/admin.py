"""Admin interface for policies."""
from django.contrib import admin
from .models import Zone, Address, Service, Policy, PolicyLog


@admin.register(Zone)
class ZoneAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'updated_at']
    search_fields = ['name', 'description']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['name', 'address_type', 'value', 'created_at']
    list_filter = ['address_type', 'created_at']
    search_fields = ['name', 'value', 'description']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'protocol', 'port', 'created_at']
    list_filter = ['protocol', 'created_at']
    search_fields = ['name', 'description']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(Policy)
class PolicyAdmin(admin.ModelAdmin):
    list_display = ['priority', 'name', 'source_zone', 'destination_zone', 'action', 'enabled']
    list_filter = ['action', 'enabled', 'source_zone', 'destination_zone']
    search_fields = ['name', 'description']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'priority', 'description')
        }),
        ('Policy Scope', {
            'fields': ('source_zone', 'destination_zone')
        }),
        ('Traffic Definition', {
            'fields': ('source_addresses', 'destination_addresses', 'services')
        }),
        ('Action', {
            'fields': ('action', 'enabled', 'logging_enabled')
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    filter_horizontal = ['source_addresses', 'destination_addresses', 'services']


@admin.register(PolicyLog)
class PolicyLogAdmin(admin.ModelAdmin):
    list_display = ['policy', 'action', 'user', 'timestamp']
    list_filter = ['action', 'timestamp', 'policy']
    search_fields = ['policy__name', 'user']
    readonly_fields = ['timestamp', 'policy', 'action', 'user', 'changes']
    
    def has_add_permission(self, request):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False
