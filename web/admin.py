from django.contrib import admin

from web.models import MoneySlot, MoneySlotTag


class MoneySlotAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'amount_spent')
    search_fields = ('id', 'title')
    list_filter = ('amount_spent', 'user')


class MoneySlotTagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user')
    search_fields = ('id', 'title')
    list_filter = ('user', )


admin.site.register(MoneySlot, MoneySlotAdmin)
admin.site.register(MoneySlotTag, MoneySlotTagAdmin)
