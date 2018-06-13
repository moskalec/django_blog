{% extends "core/base.tpl" %}

{% block title %}Index{% endblock %}

{% block content %}
    <h1>Категории</h1>
    <br>
    {% for category in categories %}
        <h2><a href="/{{ category.id }}/">{{ category.title }}</a></h2>
        <hr>
    {% endfor %}
{% endblock %}
