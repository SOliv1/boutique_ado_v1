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

*pre-receive hook declined:*
- found large files on my workspace and could not push to github. What you need to do is `.gitignore` them in the future if you should ever find them again.
it ignored these files below - have no idea where they came from but it  works now thank goodness. 
`core.Microsoft.Pytho.2803.1590767825`
`core.Microsoft.Pytho.6042.159076802`

- mkdir static
- mkdir media
- mkdir static/css

- css framework: https://bulma.io/  -  ensures that whenever we use font awesome icons.
They will always stay perfectly centred and have a consistent size.

- go to lato in google fonts and select for the css in base css.
add `<link href="https://fonts.googleapis.com/css2?family=Lato:it.al,wght@0,100;0,400;0,700;0,900;1,300;1,400;1,700;1,900&display=swap" rel="stylesheet">`
`<link href="https://fonts.googleapis.com/css2?family=Lato&display=swap" rel="stylesheet">`
to main core.css block.

- go to font awesome account and sign in:`https://fontawesome.com/icons?d=gallery`
`https://fontawesome.com/`

- add kit code: `<script src="https://kit.fontawesome.com/1e03de6694.js" crossorigin="anonymous"></script>`

## Main site navigation

- code paste in directly from the 'bootstrap navbar documentation'.

- `mkdir templates/includes`
- `main-nav.html`
- `mobile-top-header.html`

3 - list items 
1.  will give us a button to open the `search bar`.
1.  One to open the `My account drop-down menu`.
1.  a.  And while we're at it let's get rid of this profile URL since we haven't created that one yet
1.  And one to access the `shopping bag`.
1.  At this point, you should pause the video
    on each of these items to make sure that your code matches before moving on.
1.  Now that the mobile version of the top portion of the header is complete.
`.  Let's build main-nav.html.
-   div with the classes, 
    collapsed and navbar-collapse.
    And I'lll give an id of main-nav which will match it up with the toggle button we
    put into the base template.
-   Inside the div goes a standard unordered list using the required class from bootstrap.
-   As well as a couple to make it auto width and auto left and right margins.
-   Again the shell of all this code comes from the bootstrap documentation
-   so all we're doing is using that as the base and customizing it.
-   Next, I'm going to paste in the first list item which will be the all products menu.
-   As you can see this is pretty standard it's just a link that says all products.
    Which triggers a drop-down of four other links
- 3 more list items added:
1,  clothing
1.  homeware
1.  special offers

-   finish, save and include in base.html
- add mobile views to base.html / run and test in browser
## 



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
