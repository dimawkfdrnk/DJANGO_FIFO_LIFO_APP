from django.contrib import admin

from .models import DonationItem, RequestItem, Stocks, HelpRequest, Donation, CompletedRequest


class StocksAdmin(admin.ModelAdmin):
    list_display = ('name_stock', 'vacancies', 'occupied_places', 'id')

admin.site.register(Stocks, StocksAdmin)


class CompletedRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'status')

admin.site.register(CompletedRequest, CompletedRequestAdmin)


class DonationItemInline(admin.TabularInline):
    model = DonationItem


class DonationAdmin(admin.ModelAdmin):
    inlines = [DonationItemInline, ]

admin.site.register(Donation, DonationAdmin)


class DonationItemAdmin(admin.ModelAdmin):
    list_display = ('name_item', 'category', 'status', 'stock', 'id', 'donation_id')
    readonly_fields = ('donation_id', 'id')

    fieldsets = (
        (None, {
            'fields': ('name_item', 'category', 'status', 'stock')
        }),
        ('Дополничельные данные', {
            'fields': ('donation_id', 'id', )}
         )
    )
    search_fields = ['donation_id__id', 'id', 'name_item']

admin.site.register(DonationItem, DonationItemAdmin)


class RequestItemInline(admin.TabularInline):
    model = RequestItem


@admin.action(description='Close selected cases')
def close_appeal(modeladmin, request, queryset):
    queryset.update(status='Close')


class HelpRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'status')
    inlines = [RequestItemInline, ]
    actions = [close_appeal]

admin.site.register(HelpRequest, HelpRequestAdmin)

class RequestItemAdmin(admin.ModelAdmin):
    list_display = ('name_item', 'category', 'status', 'stock', 'id', 'request_id')
    readonly_fields = ('request_id', 'id')
    fieldsets = (
        (None, {
            'fields': ('name_item', 'category', 'status', 'stock')
        }),
        ('Дополничельные данные', {
            'fields': ('request_id', 'id',)}
         )
    )
    search_fields = ['request_id__id', 'id', 'name_item']
    list_filter = ('category', 'status', 'stock')
    actions = [close_appeal]

admin.site.register(RequestItem, RequestItemAdmin)






