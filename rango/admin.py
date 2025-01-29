from django.contrib import admin
from rango.models import Category, Page

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')  # 确保顺序为 title, category, url

admin.site.register(Category)
admin.site.register(Page, PageAdmin)
