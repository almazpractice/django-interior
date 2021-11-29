from django.contrib import admin

from .models import Product, Card, Group

class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'picture', 'description', 'price', 'old_price', 'group')
    search_fields = ('title',)
    list_filter = ('old_price',)
    list_editable = ('old_price',)
    empty_value_display = ''


class GroupAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'slug', 'description')
    search_fields = ('slug',)
    empty_value_display = 'no_category'


class CardAdmin(admin.ModelAdmin):
    list_display = ('pk', 'product', 'add_datetime', 'count')
    search_fields = ('product',)
    empty_value_display = ''


admin.site.register(Product, ProductAdmin)
admin.site.register(Card, CardAdmin)
admin.site.register(Group, GroupAdmin)

