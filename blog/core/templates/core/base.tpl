<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <link rel="stylesheet" href="{{ STATIC_URL }}css/bootstrap.min.css">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>{% block title %}{% endblock %}</title>
    </head>
    <body>
    <header>
        <nav class="navbar navbar-dark bg-primary">
          <span class="navbar-text">
              <a href="/">Home</a>
              <a href="/categories">Categories</a>
              <a href="/tags">Tags</a>
              <a href="/articles">Articles</a>
          </span>
        </nav>


        {% block content %}
            {% render_breadcrumbs %}
        {% endblock %}
    </header>

     <div class="container">

      <div class="row">

        <div class="col-sm-8 blog-main">


            {% block content %}
            {% endblock %}


        </div><!-- /.blog-main -->

        <div class="col-sm-3 offset-sm-1 blog-sidebar">
          <div class="sidebar-module sidebar-module-inset">
            <h4>most_populated_tags</h4>
            {% for most_tag in most_populated_tags %}
                <h5>{{ most_tag.title }}({{ most_tag.num_articles }} articles)</h5>
            {% endfor %}
            <hr>
          </div>
          <div class="sidebar-module">
            <h4>most_popular_categories</h4>
            {% for most_category in most_popular_categories %}
                <h5>{{ most_category.title }}({{ most_category.articles_count }} articles)</h5>
            {% endfor %}
            <hr>
          </div>
          <div class="sidebar-module">
            <h4>most_commented_articles</h4>
            {% for most_article in most_commented_articles %}
                <h5>{{ most_article.title }}({{ most_article.comment_count }} comments)</h5>
            {% endfor %}
          </div>
        </div><!-- /.blog-sidebar -->

      </div><!-- /.row -->

    </div><!-- /.container -->

    <footer class="blog-footer blue">

            <nav class="navbar navbar-dark bg-primary">
              <span class="navbar-text">
                  <a href="/">Home</a>
                  <a href="/categories">Categories</a>
                  <a href="/tags">Tags</a>
                  <a href="/articles">Articles</a>
              </span>
            </nav>

      <div class="footer-copyright text-center py-3">© 2018 Copyright:
        <a href="https://devclub.com"> DevClub.com</a>
      </div>

    </footer>


    </body>
    <script src="{{ STATIC_URL }}js/bootstrap.min.js"></script>
</html>
