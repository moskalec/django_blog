{% extends "core/base.tpl" %}

{% block title %}Tags{% endblock %}

{% block content %}
    <h1>Tags</h1>
    <br>
    {% for tag in tags %}
        <h2><a href="/{{ tag.id }}">{{ tag.title }}</a></h2>
        <hr>
    {% endfor %}
{% endblock %}