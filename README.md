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


#### 1.8 Modified main_navbar

        modified:   README.md
        modified:   templates/shared/navbar/main_navbar.html

        NOTE: :)


### 2. CRUD MAIN NAVBAR (CATEGORIES)
------------------------------------


#### 2.1. Create Category model and run migrations

        modified:   README.md
        modified:   apps/newsmag/admin.py
        new file:   apps/newsmag/migrations/0001_initial.py
        modified:   apps/newsmag/models.py


#### 2.2. CRUD: CREATE categories from the form

        STEPS:

        1. In apps/newsmag create a new file: apps/newsmag/forms.py
           and create CategoryCreateForm
        2. In views, create CategoryCreateView method and Add logig it
        3. In apps/newsmag create a new file: category_create.html and add form to it
           *** this form copied from source code of the django admin panel
        4. In category_create.html, loop and load form instance from the CategoryCreateView
        5. Define the path in urls 
        6. Test it out and check the result :)

        modified:   README.md
        new file:   apps/newsmag/forms.py
        new file:   apps/newsmag/templates/newsmag/create_category.html
        modified:   apps/newsmag/urls.py
        modified:   apps/newsmag/views.py   
        
        NOTE: :)

        NEXT> USE TEMPLATETAGS to show categories to main navbar



#### 2.3. CRUD: READ data categories in db and fetch them  to main navbar

        STEPS:

        1. Create custom_template: apps/newsmag/templatetags/custom_template.py
        2. Define show_menu function in: apps/newsmag/templatetags/custom_template.py
        3. Loop categories in: templates/shared/navbar/main_navbar.html
        4. Load custom_template: templates/base.html
        5. fetch show_menu in : templates/base.html

        modified:   README.md
        new file:   apps/newsmag/templatetags/__init__.py
        new file:   apps/newsmag/templatetags/custom_template.py
        modified:   templates/base.html
        modified:   templates/shared/navbar/main_navbar.html

        NOTE: 
        
        Well DONE :)

        NEXT> UPDATE categories       


#### 2.4. CRUD: UPDATE category

        STEPS:

        1. In views, create CategoryCreateView method and Add logig it
        2. In apps/newsmag create a new file: category_update.html and add form to it
           *** this form copied from source code of the django admin panel
        3. In category_update.html, loop and load form instance from the CategoryCreateView
        4. Define the path in urls 
        5. Test it out and check the result :)

        modified:   README.md
        new file:   apps/newsmag/templates/newsmag/category_update.html
        modified:   apps/newsmag/urls.py
        modified:   apps/newsmag/views.py

        
        NOTE: :)

        NEXT> DELETE categories


#### 2.5. CRUD: DELETE category


        STEPS:

        1. In views: create CategoryDeleteView, and
           add logic to delete a category
        2. Create path
        3. Test it out :)

        modified:   README.md
        new file:   apps/newsmag/templates/newsmag/category_delete.html
        new file:   apps/newsmag/templates/newsmag/category_delete_confirm.html
        modified:   apps/newsmag/urls.py
        modified:   apps/newsmag/views.py

        
        NOTE: :)

        There was no confirmation or message
        about warning if you are sure to delete
        the object.


### 3. USERS APP
----------------


#### 3.1 Create Users app

        .
        ├── LICENSE
        ├── README.md
        ├── apps
        │ ├── newsmag
        │ └── users
        ├── config
        │ ├── __init__.py
        │ ├── __pycache__
        │ ├── asgi.py
        │ ├── settings.py
        │ ├── static
        │ ├── urls.py
        │ └── wsgi.py
        ├── db.sqlite3
        ├── manage.py
        └── templates
            ├── base.html
            └── shared


#### 3.2 USER Login

        STEPS:

        1. Refer to DJANGO-LOGIN,REGISTER,LOGOUT.txt file in HOW-TO folder
        2. Remember: Form model, Views and login.html
        
        modified:   README.md
        new file:   apps/users/forms.py
        new file:   apps/users/templates/users/login.html
        new file:   apps/users/urls.py
        modified:   apps/users/views.py
        modified:   config/settings.py
        modified:   config/urls.py
        modified:   templates/shared/top_header.html

        NOTE: :) :) :)


#### 3.3 House keeping - codes re-organization

        deleted:    apps/newsmag/templates/newsmag/category_create.html
        deleted:    apps/newsmag/templates/newsmag/category_delete.html
        deleted:    apps/newsmag/templates/newsmag/category_delete_confirm.html
        deleted:    apps/newsmag/templates/newsmag/category_update.html
        new file:   apps/newsmag/templates/newsmag/crud/category_create.html
        new file:   apps/newsmag/templates/newsmag/crud/category_delete.html
        new file:   apps/newsmag/templates/newsmag/crud/category_delete_confirm.html
        new file:   apps/newsmag/templates/newsmag/crud/category_update.html
        modified:   apps/newsmag/views.py
        modified:   config/asgi.py
        modified:   config/settings.py
        modified:   config/wsgi.py
        new file:   templates/base_admin.html
        new file:   templates/shared/admin/footer.html
        new file:   templates/shared/admin/head.html

        NOTE: :)


#### 3.4 USER Login - Add flash message

        modified:   README.md
        modified:   apps/newsmag/views.py
        modified:   apps/users/templates/users/login.html
        modified:   apps/users/views.py

        NOTE: :)


#### 3.4 USER Logout - Using django auth to log user out, showing/hiding menu username and logout, and showing/hiding menu login and register

        modified:   README.md
        new file:   apps/users/templates/registration/login.html
        modified:   apps/users/urls.py
        modified:   config/settings.py
        modified:   templates/shared/top_header.html

        NOTE: :)


#### 3.5 USER Registration - Register a new user

        STEPS:

        1. Refer to DJANGO-LOGIN, REGISTER-LOGOUT.txt
        2. Pay attention to:
                - form action
                - form method
                - form model
                - view logic
                - avoid to have the same codes in different folder open at once
                  in your text editor

        modified:   README.md
        modified:   apps/users/forms.py
        renamed:    apps/users/templates/registration/login.html -> apps/users/templates/users/login.html
        new file:   apps/users/templates/users/register.html
        new file:   apps/users/templates/users/register_done.html
        modified:   apps/users/urls.py
        modified:   apps/users/views.py
        modified:   templates/shared/top_header.html


#### 3.6 PASSWORD - Password change views

        modified:   README.md
        renamed:    apps/users/__init__.py -> apps/accounts/__init__.py
        renamed:    apps/users/admin.py -> apps/accounts/admin.py
        renamed:    apps/users/apps.py -> apps/accounts/apps.py
        renamed:    apps/users/forms.py -> apps/accounts/forms.py
        renamed:    apps/users/migrations/__init__.py -> apps/accounts/migrations/__init__.py
        renamed:    apps/users/models.py -> apps/accounts/models.py
        renamed:    apps/users/templates/users/login.html -> apps/accounts/templates/accounts/login.html
        renamed:    apps/users/templates/users/register.html -> apps/accounts/templates/accounts/register.html
        renamed:    apps/users/templates/users/register_done.html -> apps/accounts/templates/accounts/register_done.html
        new file:   apps/accounts/templates/registration/password_change_done.html
        new file:   apps/accounts/templates/registration/password_change_form.html
        renamed:    apps/users/tests.py -> apps/accounts/tests.py
        renamed:    apps/users/urls.py -> apps/accounts/urls.py
        renamed:    apps/users/views.py -> apps/accounts/views.py
        modified:   config/settings.py
        modified:   config/urls.py
        modified:   templates/shared/top_header.html
   
        E:.
        ├───apps
        │   ├───accounts
        │   │   ├───templates
        │   │   │   ├───accounts
        │   │   │   └───registration
        │   │   └───__pycache__
        │   └───newsmag
        │       ├───templates
        │       │   └───newsmag
        │       │       ├───crud
        │       │       ├───partials
        │       │       │   ├───featured
        │       │       │   └───most_popular
        │       │       └───shared
        │       ├───templatetags
        │   ├───static
        │   │   ├───admin
        │   │   └───assets
        │   │       ├───css
        │   │       ├───fonts
        │   │       ├───img
        │   └───__pycache__
        └───templates
            └───shared
                ├───admin
                ├───footer
                └───navbar
        
        NOTE:

        A lot of changes were made:

        1. Change app name
                FROM : apps/users
                TO   : apps/accounts
        2. accounts app must be placed on the top 
           of the INSTALLED_APPS in settings.py
        3. Othe changes were made because of the poin 1.

        4. At last, now user can:
           - register
           - login
           - logout
           - change password 

        :)


#### 3.7 PASSWORD - Password reset views

        modified:   README.md
        modified:   apps/accounts/templates/accounts/login.html
        new file:   apps/accounts/templates/registration/password_reset_complete.html
        new file:   apps/accounts/templates/registration/password_reset_confirm.html
        new file:   apps/accounts/templates/registration/password_reset_done.html
        new file:   apps/accounts/templates/registration/password_reset_email.html
        new file:   apps/accounts/templates/registration/password_reset_form.html
        modified:   apps/accounts/urls.py
        modified:   config/settings.py

        NOTE:

        The book does not provied instruction to
        add this "EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' in settings.py.

        Whithout EMAIL_BACKEND, it produced this error: ConnectionRefusedError at /password-reset/ [WinError 10061] No connection could be made because the target machine actively refused it

        Solution found here:
        https://stackoverflow.com/questions/57353548/connectionrefusederror-at-password-reset-winerror-10061-no-connection-could

        NOW :)


### 4. EXTENDING USER MODEL
---------------------------


#### 4.1 USER MODEL - Creating user Profile

        modified:   README.md
        modified:   apps/accounts/admin.py
        new file:   apps/accounts/migrations/0001_initial.py
        modified:   apps/accounts/models.py

        NOTE:

        1. This is a preparation to create user Profile.
        2. This model will be use in UserRegisterView in the accounts/views.py

        DONE: :)        


#### 4.2 USER MODEL - Creating user profile

        modified:   README.md
        modified:   apps/accounts/forms.py
        new file:   apps/accounts/migrations/0002_remove_profile_email.py
        modified:   apps/accounts/models.py
        new file:   apps/accounts/templates/accounts/profile.html
        modified:   apps/accounts/urls.py
        modified:   apps/accounts/views.py
        modified:   templates/shared/top_header.html

        NOTE:

        Refer to HOW-TO: 6. DJANGO-Creating user profile

