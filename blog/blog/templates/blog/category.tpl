{% extends "core/base.tpl" %}

{% block title %}{{ category.title }}{% endblock %}

{% block content %}
    <h1>{{ category.title }}</h1>
    <br>
    {% for article in articles %}
        <h2><a href="/{{ category.id }}/{{ article.id }}/">{{ article.title }}</a></h2>
        <hr>
    {% endfor %}
{% endblock %}