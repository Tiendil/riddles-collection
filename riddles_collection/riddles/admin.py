# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Riddle, Category

class RiddleAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'answer')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'url', 'name')


admin.site.register(Riddle, RiddleAdmin)
admin.site.register(Category, CategoryAdmin)
