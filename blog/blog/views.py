from django.views.generic import TemplateView
from .models import Category, Article, ArticleTag, Comment, Tag
from django.db.models import Count, Sum


class BaseUserView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        most_popular_categories = Category.objects.annotate(articles_count=Count('article')).order_by(
            '-articles_count')[:3]
        most_commented_articles = Article.objects.annotate(comment_count=Count('comment')).order_by('-comment_count')[
                                  :10]
        most_populated_tags = Tag.objects.annotate(num_articles=Count('article__title')).order_by('-num_articles')[:10]

        context.update({
            'most_commented_articles': most_commented_articles,
            'most_popular_categories': most_popular_categories,
            'most_populated_tags': most_populated_tags,
        })

        return context


class IndexView(TemplateView):
    template_name = 'blog/index.tpl'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        categories = Category.objects.all()

        most_popular_categories = Category.objects.annotate(articles_count=Count('article')).order_by('-articles_count')[:3]
        most_commented_articles = Article.objects.annotate(comment_count=Count('comment')).order_by('-comment_count')[:10]
        most_populated_tags = Tag.objects.annotate(num_articles=Count('article__title')).order_by('-num_articles')[:10]

        context.update({
            'categories': categories,
            'most_commented_articles': most_commented_articles,
            'most_popular_categories': most_popular_categories,
            'most_populated_tags': most_populated_tags,
        })
        return self.render_to_response(context)


class CategoryView(BaseUserView):
    template_name = 'blog/category.tpl'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        category = Category.objects.get(id=kwargs.get('category_id'))
        articles = Article.objects.filter(category_id=category.id)

        context.update({
            'category': category,
            'articles': articles
        })

        return self.render_to_response(context)


class ArticleView(BaseUserView):
    template_name = 'blog/article.tpl'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        article = Article.objects.get(id=kwargs.get('article_id'))

        context.update({
            'article': article
        })

        return self.render_to_response(context)


class ArticleListView(BaseUserView):
    template_name = 'blog/articles.tpl'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # articles = Article.objects.all()[:3]
        articles = Article.objects.all()
        context.update({
            'articles': articles
        })

        return context


class TagListView(BaseUserView):
    template_name = 'blog/tags.tpl'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        tags = Tag.objects.all()
        context.update({
            'tags': tags
        })

        return context

    # def get(self, request, *args, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #
    #     tags = Tag.objects.all()
    #     context.update({
    #         'tags': tags
    #     })
    #
    #     return self.render_to_response(context)


class CategoryListView(TemplateView):
    pass


class ArticleTagView(BaseUserView):
    template_name = 'blog/tag_article.tpl'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        tag = Tag.objects.get(id=kwargs.get('tag_id'))
        articles = Article.objects.filter(tags=tag.id)

        context.update({
            'tag': tag,
            'articles': articles
        })

        return self.render_to_response(context)
