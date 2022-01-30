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


#### 1.4 Template inheritance Part 1 - Sagmenting the home page template

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


#### 1.5 Template inheritance Part 2 - Sagmenting the base template

        ├── manage.py
        └── templates
            ├── base.html
            └── shared
                ├── footer
                │ ├── copyright.html
                │ ├── logo_and_sosmed.html
                │ ├── recent_posts.html
                │ ├── subscribe_newsletter.html
                │ └── useful_links.html
                ├── head.html
                ├── loader.html
                ├── navbar
                │ ├── logo.html
                │ ├── main_navbar.html
                │ └── search.html
                ├── scripts.html
                └── top_header.html

        modified:   README.md
        modified:   templates/base.html
        new file:   templates/shared/footer/copyright.html
        new file:   templates/shared/footer/logo_and_sosmed.html
        new file:   templates/shared/footer/recent_posts.html
        new file:   templates/shared/footer/subscribe_newsletter.html
        new file:   templates/shared/footer/useful_links.html
        new file:   templates/shared/head.html
        new file:   templates/shared/loader.html
        new file:   templates/shared/navbar/logo.html
        new file:   templates/shared/navbar/main_navbar.html
        new file:   templates/shared/navbar/search.html
        new file:   templates/shared/scripts.html
        new file:   templates/shared/top_header.html

        NOTE: :)


#### 1.6 Adding page title

        modified:   README.md
        modified:   apps/newsmag/templates/newsmag/index.html
        modified:   templates/base.html
        modified:   templates/shared/head.html

        NOTE: :)


#### 1.7 Adding Develop with love by ING AFTER 63 on the footer 

        modified:   README.md
        modified:   templates/shared/footer/copyright.html