from django.contrib import admin
from .models import Sweet, Category


class SweetAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Sweet, SweetAdmin)
admin.site.register(Category, CategoryAdmin)
