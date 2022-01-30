# 2022-django4-news-mangazine
Building News Magazine Application using Django Version 4.0

Github repository: https://github.com/gurnitha/2022-django4-news-mangazine


### 1. BASIC SETUP
------------------


#### 1.1 Created django project 'config' and django app 'apps/newsmag'

        E:.
        ├───apps
        │   └───newsmag
        │       ├───migrations
        │       │   └───__pycache__
        │       └───__pycache__
        └───config
            └───__pycache__

        modified:   README.md
        new file:   apps/newsmag/__init__.py
        new file:   apps/newsmag/admin.py
        new file:   apps/newsmag/apps.py
        new file:   apps/newsmag/migrations/__init__.py
        new file:   apps/newsmag/models.py
        new file:   apps/newsmag/tests.py
        new file:   apps/newsmag/views.py
        new file:   config/__init__.py
        new file:   config/asgi.py
        new file:   config/settings.py
        new file:   config/urls.py
        new file:   config/wsgi.py
        new file:   manage.py


#### 1.2 Created Views, Templates, Urls for home page, added and loaded static and media files 

        modified:   .gitignore
        new file:   apps/newsmag/templates/newsmag/index.html
        new file:   apps/newsmag/urls.py
        modified:   apps/newsmag/views.py
        modified:   config/settings.py
        modified:   config/urls.py

        NOTE: :)


#### 1.3 Creating and extending base template

        modified:   README.md
        modified:   apps/newsmag/templates/newsmag/index.html
        modified:   config/settings.py
        new file:   templates/base.html

        NOTE:

        1. No errors in the browsers: Edge, Chrome and Firefox

        SUPER TEMPLATE :)


#### 1.4 Sagmenting the template and use template inheritance

        modified:   README.md
        modified:   apps/newsmag/templates/newsmag/index.html
        new file:   apps/newsmag/templates/newsmag/partials/featured/featured.html
        ..
        new file:   apps/newsmag/templates/newsmag/shared/categories.html
        ..
        new file:   apps/newsmag/templates/newsmag/shared/tags.html

        .
        ├── LICENSE
        ├── README.md
        ├── apps
        │ └── newsmag
        │     ├── __init__.py
        │     ├── admin.py
        │     ├── apps.py
        │     ├── migrations
        │     ├── models.py
        │     ├── templates
        │     │ └── newsmag
        │     │     ├── index.html
        │     │     ├── partials
        │     │     │ ├── featured
        │     │     │ │ └── featured.html
        │     │     │ └── most_popular
        │     │     │     ├── business.html
        │     │     │     ├── culture.html
        │     │     │     ├── health.html
        │     │     │     ├── most_popular_news.html
        │     │     │     ├── politics.html
        │     │     │     ├── sports.html
        │     │     │     └── top_videos.html
        │     │     └── shared
        │     │         ├── categories.html
        │     │         ├── featured_reports.html
        │     │         ├── instagram.html
        │     │         ├── latest_news.html
        │     │         ├── most_shared.html
        │     │         ├── popular_posts.html
        │     │         ├── social_media.html
        │     │         ├── subscribe_newsletter.html
        │     │         └── tags.html
        │     ├── tests.py
        │     ├── urls.py
        │     └── views.py
        ├── config
        ...

        NOTE: :)