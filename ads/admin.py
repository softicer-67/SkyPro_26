from django.contrib import admin
from .models import Cat, Ads, User, Location


@admin.register(Cat)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Ads)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', 'price', 'image']
    search_fields = ('name', 'price',)


@admin.register(User)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['username']


@admin.register(Location)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

