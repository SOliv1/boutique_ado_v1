<img src="https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png" style="margin: 0;">

## initial set up project 
pip3 install django
cd /workspace/.pip-modules/lib/python3.8/site-packages/`
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

## Adding Products part5
-   attach some plus and minus buttons to this input to make it easier to use on mobile.
<!-- And also to align it more closely with our current black and white theme.
To do this I can just use the built-in input group append
and input group prepend classes from bootstrap.
And toss a couple of buttons in them with the appropriate font awesome icons.
You'll see there are also a couple of extra attributes on these buttons.
data item id and the id attribute itself. -->
-   JavaScript handles updating the input box itself.
    Since these buttons won't do anything by default.
-   write that JavaScript right now.
    do it in an *include* since we'll also use it on the shopping bag page in the next video.
-    Create an includes directory in the products template folder.
-   And then an *html file* which I'll call quantity_input_script.html
    I'm doing this as an HTML file since it'll just be a script element we include at
    the end of the *product detail template*
    And this avoids having to deal with additional static files just for a single JavaScript file.
-   Let's begin script to increment the quantity.
## Adding Products part6
        add the *quantity selector box* to the shopping bag pages quantity column.

        replace this quantity in the *table with a form with a method of post*.
        It won't have an action yet since we haven't created the *proper URLs or views*
        but we'll get to that soon.
        I'll give it a *class of update form and attach the csrf token since it'll be posting data*.
        And from here it's as simple as copying the form group from the product detail
        page and pasting it in.
        And now we'll make a few changes to it.
        -   First I'll get rid of the 50% width class.
        -   Add some classes to make the icons buttons and input boxes a bit smaller.
        -   And I'll remove the icon class here in the span element
        -   which will allow Font awesomes fa-small class to handle the sizing.
        -  nstead of the icon class we copied from Bulma in the beginning of this project.
        -   need to update all the template variables that contain product.id to item.item_id
            Also, let's change the value of the input box
            to reflect the number of this item currently in the shopping bag.
            Finally because there's no size selector box on this page.
            We'll need to submit the size of the item the user wants to update or remove in a hidden input field.
            If the product does in fact have sizes.
