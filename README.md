<img src="https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png" style="margin: 0;">

## initial set up project 
pip3 install django

`cd /workspace/.pip-modules/lib/python3.8/site-packages/`
 `ls -la` 
 - to view list of site packages

 - use a shortcut `cd -` to get back to the last directory that we were working in.

django-admin startproject boutique_ado .

touch .gitignore

python3 manage.py runserver

exit out Ctrl + C

python3 manage.py migrate

python3 manage.py createsuperuser

git status 
git add .
git commit -m "initial commit"
git push

##Allauth Setup 1
pip3 install django-allauth

go to settings to grab the documentation:
https://django-allauth.readthedocs.io/en/latest/installation.html

https://django-allauth.readthedocs.io/en/latest/installation.html

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




















Welcome Sara Oliver,

This is the Code Institute student template for Gitpod. We have preinstalled all of the tools you need to get started. You can safely delete this README.md file, or change it for your own project.

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: *Make Public*,

Another blue button should appear to click: *Open Browser*.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: *Make Public*,

Another blue button should appear to click: *Open Browser*.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the backend lessons.

## Updates Since The Instructional Video

We continually tweak and adjust this template to help give you the best experience. Here are the updates since the original video was made:

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

--------

Happy coding!
