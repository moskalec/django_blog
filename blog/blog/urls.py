from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.IndexView.as_view()),
    re_path(
        r'^categories/$',
        views.IndexView.as_view()
    ),
    re_path(
        # r'^(?P<category_title>[\w.@+-]+)/$', views.CategoryView.as_view(),
        r'^(?P<category_id>[\d]+)/$',
        views.CategoryView.as_view(),
    ),
    re_path(
        r'^(?P<category_id>[\d]+)/(?P<article_id>[\d]+)/$',
        views.ArticleView.as_view()
    ),
    re_path(
        r'^tags/$',
        views.TagListView.as_view()
    ),
    re_path(
        r'^tags/(?P<article_id>[\d]+)/$',
        views.ArticleTagView.as_view()
    ),
    re_path(
        r'^articles/$',
        views.ArticleListView.as_view()
    ),
    re_path(
        r'^articles/(?P<article_id>[\d]+)/$',
        views.ArticleView.as_view()
    ),
]
