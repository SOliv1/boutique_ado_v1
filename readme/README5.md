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
# Profile App - Part 3 & 4
 -  Update *allauth base.html*
 -  Update *accounts base.html*
 -  Update all the templates in the *accounts folder*
 -  Update the *base.css* to match all the other templates
    By the way, you could also do this by adding the BTN or text info
        or whatever other bootstrap classes you wanted to all the elements in the allauth templates
        But since there's a lot of templates it's faster to just copy the styles
        and apply them globally via the CSS here.
        That's another reason I added the allauth inner content div as it gives us a way to isolate all the forms
        in all the allauth templates and apply CSS to them.
-   Now if I try to log in you'll see it won't let me anymore since I have no user profile.
        That's because the signal in the profiles app is picking up that my user name isn't new
        so it's trying to save my profile which doesn't exist.
        -    comment out the signal in profiles/models.py to login presently
    # if created:
    UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    # instance.userprofile.save()
        once in just set back to the way it was
-       The last thing I'll do just to prove that profiles are working correctly is to update the link
        in the base template to point at the profile url.
    -   Create profiles/profile.html in profiles/templates
-   Then go to our profiles views.py and Import the user profile model
        Get the profile for the current user. And then return it to the template.
        Then in the template, just render the profile.
        And we'll see the user name printed out and test out in webbrowser
# Profile App - Part 5 & 6
-   Begin by copying the *checkout apps forms.py* into the *profiles app*
    -   Let's now go to the profile *views.py* import the form
    -   Populate it with the user's current profile information
    -   And return it to the template - render form in *profile.html*
    -   Update *models.py* in profile app. Then refresh and test in browser. *Tip = Use alt + up/down arrows to move lines up or down*
    -   With that resolved let's make sure that the profile forms placeholders are all colored correctly.
    And to do that I'll just grab the *CSS from the search box*. And change the selector.
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
        -   add jquery (js/folder/countryfield.js) to profiles/static/profiles
        -   update toasts_success.html in line with the profiles success page
        -   update views.py and import messages
# Profile App - Part 7 & 8

# Profile App - Part 9 & 10
# Profile App - Part 11 & 12
# Profile App - Part 13 & 14