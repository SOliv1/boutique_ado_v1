# Deploying heroku app part 2

    We'll just use the free plan for this project.
    -   To use Postgres we need to go back to gitpod and 
    `pip3 install dj_database_url`
    `pip3 install psycopg2-binary`
    -   Now I can freeze the requirements with 
    `pip3 freeze > requirements.txt`
    -And that'll make sure Heroku installs all our apps requirements when we deploy it.

## make migrations and load the data
-       `python3 manage.py showmigrations`
        `python3 manage.py makemigrations`
        `python3 manage.py migrate`
        `python3 manage.py loaddata categories`
         `python3 manage.py loaddata products`
        remember it's important to do them in that order because the products
        depend on the categories already existing
        `python3 manage.py createsuperuser`
        Create a superuser to login with
        uncomment database and remove the postgress url before commit to avoid version control

##  deploy to heroku part 2 
-   replace the database urls after commiting with an if statement - see above
    -`pip3 install gunicorn`
-   `pip3 freeze > requirements.txt`
    -Create *Procfile*
    - `heroku config:set DISABLE_COLLECT_STATIC`
    `heroku config:set DISABLE_COLLECT_STATIC=1 --app sjk-boutiqueado`
Add the hostname of our Heroku app to *allowed hosts in settings.py*
Save all and commit to git hub before deploying and pushing to heroku
        go to https://aws.amazon.com/
        to set up your free storage structure account to store your images and files
    pip3 install dj_database_url
AWS Amazon web services = 

     I had an issue with deploying to my heroku app - it turned out that I had commented out my env.py so my variables were not being read hence aws not being imported and 
     thus my website not deployed.  Stephen the tutor very kindly pointed this out to me and explained the method of thinking which I have added here for future reference.
     "All I did was see that your environmental variables were not being read.  Eg - you aws keys weren't being read so the styling was off, so I just presumed they weren't being imported, 
     so I just checked your import, saw it was commented out and then uncommented it"
     
     Thank you Stephen for clarifying this simple error to me and how you found it.  Much appreciated.  A;; good now - yay!!

        Make sure everything on the website is working from admin to signing in to website to profiles to stripe paymnets and products and services are all working.
        This should now be a fully functioning website with the ground work having been laid.  To make it fully funcitoning in the real world.
            send a test webhook from stripe to make sure that our listener is working.
            With all this complete our e-commerce store is deployed and anyone on the
            Internet can navigate our products, create a profile, and even check out
            using a test credit card number.
            If you make a purchase you'll find your order faithfully created in the django admin.
            And if you're logged in it'll be attached to your profile and displayed in your order history.
            if we wanted to turn this into a real store at this point
            it would involve some additional testing on stripe.
            Setting up real confirmation emails.
            And switching our stripe settings to use the live keys rather than the test ones we're using now.
            we would also likely want to write a plethora of tests for our application.
            In particular in the checkout and shopping bag apps.
            And make some security adjustments as well as some minor changes to make it easier to work
            between our development and production environments seamlessly.
            The groundwork has been laid though.
            And the remaining videos will be focused on tidying up some of the design elements
            some discussion of code refactoring.
            And handling how to send real emails with our django application.

## Sending real emails

            Sign into your gmail account or create one if you have not already.
                    -   Go to settings in the upper right.
                    -   Click accounts and import.
                    -   And then other Google account settings.
                    -   On this screen, I'll go to the security tab and under, signing into Google
                    -   we're going to turn on 2-step verification.
                    -   This will allow us to create an app password specific to our Django app.
                    -   That will allow it to authenticate and use our Gmail account to send emails.
                    -   To turn it on just click get started, enter your password.
                    -   And then you'll have to select a verification method.
                    -   I'll have them send a verification code via text but you can choose any method you prefer.
                    -   Once you've verified and turned on two-step verification.

                    - new option called app passwords under the signing in to Google heading.
                            - new option called app passwords under the signing in to Google heading.
                            -    click that enter my password again if needed.
                            -   Then on the *app password screen*, select mail for the app.
                            -   Then under device type, select other and type in Django.
                            -   Again you can set whatever you want here but I'm doing this just to keep things organized.
                            -   With that done we'll be given a 16 character password to copy.
                            -   And then go to the Heroku app to enter it as a config variable.
                            -   lets call the variable EMAIL_HOST_PASS. And paste it in and click Add.
                            -    we need another variable here called EMAIL_HOST_USER
                            -   Which will be set to my Gmail account.
                            -   last step then is just to add a few 
                                 *settings to settings.py*
                            -   Let's follow a similar procedure to our other settings here,
                            -   where we check if development is in os.environ.
                            -   To determine which email setup to use.
                            -   If that variable is set, we'll log emails to the console.
                            -   the only setting we need to specify is the default from email.
                            -   i.e.  be boutiqueado@example.com
                                -Otherwise, for *production* we need to set several variables.
                                - EMAIL_BACKEND, which will be set to django.core.mail.backends.smpt.EmailBackend
                                - EMAIL_USE_TLS which will be true
                                - EMAIL_PORT which will be port 587
                                - EMAIL_HOST which will be smtp.gmail.com
                            - then the username, password, and DEFAULT_FROM_EMAIL
                            all of which will get from the environment.
                            With that complete all we need to do is finish the set up we just need to deploy to Heroku.
                            -commit to github - adding all our changes.
                                                - Committing.
                                                -  And then issuing a git push
                            Test it out let's head to our Heroku app. And try to register for an account.
                            - use a temporary email from tempmail.org
                            - get the confirmation email which means email is being sent properly.
                            - And now  veriwe can the account.
                            And now be  able to login.

## Base CSS, Login & Registration Refactor 
        Focus mainly on base.css.
            Where we'll make some adjustments to various font size and layout issues
            on the smallest mobile screens.
            And then on the shopping bag page, which currently doesn't have
            a very mobile-friendly layout.
            All the CSS we'll add is going to go in the media query at the bottom of base.css here.
-   fix mobile friendly in media queries for the whole site in base.css
-   then allauth templates - accounts base.html - fix the col size there 50 % width only on medium and up: `<div class="col-12 col-md-6">`
-   add link to profile page in the *mobile-top-header.html*
-    add new list item in the *main-nav.html* just above products.  `display: block. But display: none, on medium and up`


