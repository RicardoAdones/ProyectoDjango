from django.contrib import admin
from .models import Page

#configuracion extra

class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('title', 'content')
    list_filter = ('visible',)
    list_display = ('title', 'visible', 'created_at')
    ordering = ('-created_at',)

# Register your models here.

admin.site.register(Page, PageAdmin)

title = 'Panel de Django'
subtitle = 'Panel de gestión'

#configuracion de panel admin
admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = subtitle