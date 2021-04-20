from django.contrib import admin
from .models import Post, Category, Comment


class CategoriesAdmin(admin.ModelAdmin):
    """ Post categories list display with order """
    list_display = (
        'name',
        'friendly_name',
    )

    ordering = ('name',)


admin.site.register(Post)
admin.site.register(Category, CategoriesAdmin)
admin.site.register(Comment)
