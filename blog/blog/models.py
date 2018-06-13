from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone
from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation


class Category(models.Model):
    title = models.CharField(
        max_length=100,
        null=False,
        verbose_name=_('Название')
    )
    image = models.ImageField(
        verbose_name=_('Изображение'),
        blank=True,
        null=True
    )
    description = models.CharField(
        max_length=200
    )
    created = models.DateTimeField(
        auto_now_add=True,
        null=False
    )
    updated = models.DateTimeField(
        blank=True,
        null=True
    )
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        null=True,
        on_delete='DO_NOTHING'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Категория')
        verbose_name_plural = _('Категории')
        ordering = ('id',)


class Article(models.Model):
    title = models.CharField(
        max_length=100,
        null=False,
        verbose_name=_('Название')
    )
    description = models.CharField(
        max_length=200,
        null=False
    )
    content = models.TextField(
        null=False,
        verbose_name=_('Контент')
    )
    image = models.ImageField(
        verbose_name=_('Изображение'),
        null=True
    )
    created = models.DateTimeField(
        auto_now_add=True,
        null=False
    )
    updated = models.DateTimeField(
        auto_now=True,
        null=False
    )
    publication_date = models.DateField(
        auto_now_add=False,
        null=False
    )
    visible = models.BooleanField(default=False)
    category = models.ForeignKey(
        to='Category',
        null=True,
        on_delete='DO_NOTHING'
    )
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        null=True,
        on_delete='DO_NOTHING'
    )
    tags = models.ManyToManyField(
        to='Tag',
        through='ArticleTag',
        through_fields=('article', 'tag')
    )
    # comments = GenericRelation(Comment, related_query_name='comments')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Статья')
        verbose_name_plural = _('Статьи')


class Tag(models.Model):
    title = models.CharField(
        max_length=50,
        null=False
    )
    created = models.DateTimeField(
        auto_now_add=True,
        null=False
    )
    updated = models.DateTimeField(
        auto_now=True,
        null=False
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Тег')
        verbose_name_plural = _('Теги')


class ArticleTag(models.Model):
    article = models.ForeignKey(
        to='Article',
        null=True,
        on_delete='DO_NOTHING'
    )
    tag = models.ForeignKey(
        to='Tag',
        null=True,
        on_delete='DO_NOTHING'
)


class Comment(models.Model):
    content = models.TextField(
        null=False
    )
    created = models.DateTimeField(
        auto_now_add=True,
        null=False
    )
    article = models.ForeignKey(
        to='Article',
        null=True,
        on_delete='DO_NOTHING'
    )
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        null=True,
        on_delete='DO_NOTHING'
    )

    class Meta:
        verbose_name = _('Комментарий')
        verbose_name_plural = _('Комментарии')
