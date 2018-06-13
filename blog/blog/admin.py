from django.contrib import admin
from . import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Tag)
class ArticleAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Comment)
class ArticleAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ArticleTag)
class ArticleTagAdmin(admin.ModelAdmin):
    pass