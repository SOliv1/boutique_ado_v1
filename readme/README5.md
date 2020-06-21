# Personalized user profile and the admin and store management stories
# Profile App - Part 1 / 2 / 3 / 4
-  update forms.py
- `pip3 install django-countries`
- `pip3 freeze > requirements.txt`
-    In order (checkout) models, it's as simple as importing country field from django_ountries.fields.  line 7
-    change that field to use it
-   `python3 manage.py makemigrations`
-   Running the project now and navigating to the checkout page
    we can see the country drop-down box looks great, it's got all the countries in it,
-   go to *css* to fix the greyedout function in the country 
-   Refresh the *checkout page* in the website
-   Commit with update checkout form
#   Profile App - Part 2
-   `python3 manage.py startapp profiles`
-   profiles app will serve two purposes.
        First to provide a user with a place to
        save default delivery information.
        And second to provide them with a record of their order history.
        To do that we'll need a user profile model which is attached to the logged-in user.
        And we'll also need to attach the user's profile to all their orders.
        Let's begin by 
-   importing the user model.
-   import profiles and go to settings and add to apps
-   create models.py
-   update the checkout models.py
-   `python3 manage.py makemigrations --dry-run`
-   `python3 manage.py makemigrations`  if all good to go then migrate
-   `python3 manage.py migrate`
-   set up the basic URLs views and templates for the profiles app.
        Starting with views.py I'll create a simple view called profile.
        And it's just going to return a profile.html template with an empty context for now.
        Let's go create the URL for this view.
        And then include the URLs in the project level file.
        And finally we'll create the profile template.
        I'll copy the checkout template this time and make a couple minor adjustments.
        First removing bag tools.
        Then changing the extra CSS file to one for the profiles app
-   Create the URL for this view.
-   Then include the URLs in the *project level* (Boutique_ado) file
- finally create the profile template 
        - `templates/profiles/profile.html`
-   copy the checkout template this time and make a couple minor adjustments
-       -  `static/profiles/css/profile.css`
-   should be able to see the *profile template*
            - by manually going to the profile URL even if we're not logged in and test
            - go to checkout - delete checkout in browser and as you are logged in as admin you need to logout.
            - then delele the accounts/logout then add profiles to the browser to see the user profile page
            - commit changes - add profile app
# Profile App - Part 3
-   It'll be split into two text files in the *checkout apps* templates folder:
-   add a new folder in `checkout/templates/confirmation_emails` and inside that `confirmation_email_body.txt`
                        `confirmation_email_subject.txt`

-  Head over to webhook.handler and write a new private method called _send_confirmation_email
        -  send mail function from django.core. mail
        -    we'll need render_to_string from django.template.loader
        -   And also our settings file from django.conf
        -   With these imported, it's easy to send an email.
        -   Let's get the customers email from the order and store it in a variable.
        -   Then we can use the render_to_string method to render both the files we just created two strings
        -   add the DEFAULT_FROM_EMAIL to *settings.py*
        -   test it all out by making a purchase - `python3 manage.py runserver`