# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.safestring import mark_safe

from .forms import NewsAdminForm
from .models import *


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'category', 'create_date', 'get_photo')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_filter = ('category',)
    save_on_top = True
    readonly_fields = ('views', 'likes', 'get_photo', 'create_date')
    fields = ('author', 'title', 'content', 'category', 'tags', 'create_date', 'get_photo', 'likes', 'views', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    form = NewsAdminForm

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width ="150">')
        return '-'

    get_photo.short_description = 'Фото'
