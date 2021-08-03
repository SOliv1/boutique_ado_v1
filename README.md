<img src="https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png" style="margin: 0;">

## view the website here:

https://sjk-boutiqueado.herokuapp.com/


[![CodeQL](https://github.com/SOliv1/boutique_ado_v1/actions/workflows/codeql-analysis.yml/badge.svg)]

## initial set up project 
`pip3 install django`
cd /workspace/.pip-modules/lib/python3.8/site-packages/`
 `ls -la` 
 - to view list of site packages

 - use a shortcut `cd -` to get back to the last directory that we were working in.

`django-admin startproject boutique_ado .`

`touch .gitignore`

`python3 manage.py runserver`

exit out Ctrl + C

`python3 manage.py migrate`

`python3 manage.py createsuperuser`

git status 
git add .
git commit -m "initial commit"
git push

## Python3 manage.py start app home
mkdir -p home/templates/home
- right-click the inner home directory, new file and create an index.html
-   Inside the index.html page, I'm first going to extend the base template with extends base.html
-   And load the static tag with load static, so we can use static files as needed.
-   Lastly, we just need a content block with some content in it. So let's start with block content.
-   And inside that, I'll just add a simple h1 with class equals display-4 and text-success
-   to ensure bootstrap is working.
-    add the text it works.
-    Of course, we need a view to render this template so let's head into views.py
-    And define an index view.
-      Which will simply render the index template.
        And I'll add a docstring here as well.
-       A view to return the index page.
-       Next copy our project-level urls.py
-       Create a new file in the home app, called urls.py
-       And paste it in to use as a shell
        And I'm just gonna add one empty path to indicate that this is the route URL.
        And it's going to render views.index. With the name of home.
         import views from the current directory here at the top.
        And save that.
    -       And now go back to the project level URLs file and include the home URLs.
        The very last thing we need to do is add the home app to our installed apps in settings.py
        And wire up our template directories.
        Add home to installed apps.
        Add both the route templates directory.
        Add custom allauth directory to the template dirs setting.

## Allauth Setup 1
`pip3 install django-allauth`

<!-- go to settings to grab the documentation:
https://django-allauth.readthedocs.io/en/latest/installation.html

https://django-allauth.readthedocs.io/en/latest/installation.html -->

check the templates docs UP TO DATE OTHER WISE COPY/PASTE IN YOUR SETTINGS.
then add the following to your settings immediately below the templates

- `
THEN add the following apps in installed apps [] section below the other apps:

-

update migrations
`python3 manage.py migrate`

`python3 manage.py runserver`
-
##Log in to admin in the browser
go to admin and log in with your username and password.
go to the domain site name and change to new name. then log out.
log out of the browser ctrl + C

-add '/' to accounts path in the `urls.py patterns` so that the path is properly generated.

##Log emails into the console by going to settings.py
add the following:
    """
`SITE_ID = 1

`EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'`

WSGI_APPLICATION = 'boutique_ado.wsgi.application'`

    """
test by going python.py manage.py runserver
go to url and add `/accounts/login` at the end of the browser
test the username by logging in and it should redirect to `verify your email address` page.

`pip3 freeze > requirements.txt`

`mkdir templates`
`mkdir templates/allauth`

`cp -r ../.pip-modules/lib/python3.8/site-packages/allauth/templates/* ./templates/allauth/`

- head over to `https://getbootstrap.com/` to download the boilerplate for bootstrap

- go to documentation and on the first page you land on:
-- copy and paste the starter template into your base.html
    """
<meta http-equiv="X-UA-Compatible" content="ie=edge">

-  move the scripts from the bottom to the top

    """
- git commit -m ""

- simple base template now. And that's going to act as the framework for our entire project.
  lets organize everything in base templates into blocks.
- So that when we extend this template, later on, we can replace chunks of it as needed.
For example, 
- lets wrap all this "meta" in a block meta.
which will give the ability to replace or extend it in templates 
that extend this base.
- lets do the same to CSS and the JavaScript, wrapping the CSS in a block corecss.

- `git commit dash -m "add blocks to base template"`
-   `python3 manage.py startapp home`
- `mkdir -p home/templates/home`
- add `home`, to installed apps in settings.py
- add to backends 
- startup the development server: `python3 manage.py runserver`

<!-- *pre-receive hook declined:*
- found large files on my workspace and could not push to github. What you need to do is `.gitignore` them in the future if you should ever find them again.
it ignored these files below - have no idea where they came from but it  works now thank goodness. 
`core.Microsoft.Pytho.2803.1590767825`
`core.Microsoft.Pytho.6042.159076802` -->

- mkdir static
- mkdir media
- mkdir static/css

<!-- - css framework: https://bulma.io/  -  ensures that whenever we use font awesome icons.
They will always stay perfectly centred and have a consistent size.

- go to lato in google fonts and select for the css in base css.
add `<link href="https://fonts.googleapis.com/css2?family=Lato:it.al,wght@0,100;0,400;0,700;0,900;1,300;1,400;1,700;1,900&display=swap" rel="stylesheet">`
`<link href="https://fonts.googleapis.com/css2?family=Lato&display=swap" rel="stylesheet">`
to main core.css block.

- go to font awesome account and sign in:`https://fontawesome.com/icons?d=gallery`
`https://fontawesome.com/`

- add kit code: `<script src="https://kit.fontawesome.com/1e03de6694.js" crossorigin="anonymous"></script>` -->

[![CodeQL](https://github.com/SOliv1/boutique_ado_v1/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/SOliv1/boutique_ado_v1/actions/workflows/codeql-analysis.yml)


