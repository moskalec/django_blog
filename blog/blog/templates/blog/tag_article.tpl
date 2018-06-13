{% extends "core/base.tpl" %}

{% block title %}{{ tag.title }}{% endblock %}

{% block content %}
    <h1>{{ tag.title }}</h1>
    <br>
    {% for tag in tags %}
        <h2><a href="/tags/{{ article.id }}/">{{ article.title }}</a></h2>
        <hr>
    {% endfor %}
{% endblock %}