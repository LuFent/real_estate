from django.contrib import admin

from .models import Flat, Complaint, Owner


class OwnersInline(admin.TabularInline):
    model = Flat.owners.through
    raw_id_fields = ['flat', 'owner']


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owner')
    readonly_fields = ['created_at']
    list_display = ['address',
                    'price',
                    'new_building',
                    'construction_year',
                    'town']

    list_editable = ['new_building']
    list_filter = ['new_building']
    raw_id_fields = ['liked_by']
    inlines = [OwnersInline]


class СomplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ['flat']


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ['flats_owned']


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, СomplaintAdmin)
admin.site.register(Owner, OwnerAdmin)