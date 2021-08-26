from django.contrib import admin

from .models import News, Category, Personal


class MyAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'published')
    list_display_links = ('title', 'category')
    list_filter = ('title', 'published')


class MyAdminPers(admin.ModelAdmin):
    list_display = ('name', 'surname', 'master', 'pidor', 'sellary')
    list_display_links = ('name', 'surname')



admin.site.register(News, MyAdmin)
admin.site.register(Category)
admin.site.register(Personal, MyAdminPers)
# admin.site.register(Personal)
