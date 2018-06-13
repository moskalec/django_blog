{% extends "core/base.tpl" %}

{% block title %}{{ article.title }}{% endblock %}

{% block content %}
    <h1 class="blog-post-title">{{ article.title }}</h1>
    <div class="blog-post">
        <img src="{{ article.image.url }}" alt="{{ article.title }}" style="width:500px;height:300px;border:0;>
        <p class="blog-post-meta"></p>
        <p>{{ article.content }}</p>
    </div>
{% endblock %}