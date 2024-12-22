# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Documents


@admin.register(Documents)
class DocumentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'updated_at', 'document')
    list_filter = ('created_at', 'updated_at')
    date_hierarchy = 'created_at'