{% extends "core/base.tpl" %}

{% block title %}Articles{% endblock %}

{% block content %}
    <h1>Articles</h1>
    <br>
    {% for article in articles %}
              <div class="blog-post">
                <h2 class="blog-post-title"><a href="/articles/{{ article.id }}/">{{ article.title }}</a></h2>

                <a href="/articles/{{ article.id }}/">
                  <img src="{{ article.image.url }}" alt="{{ article.title }}" style="width:250px;height:150px;border:0;">
                </a>

                <p class="blog-post-meta">{{ article.created }}</p>
                <p>{{ article.description }}</p>
               </div>
    {% endfor %}
{% endblock %}