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
Add the user profile field to the order admin in so ththe checkout apps admin.py - Add checkout/views.py - This is so we really can find a way to associate the order with the user's profile when it's created which happens during the checkout process. 
IMPORTANT! insert this in the views.py checkout: def checkout_success(request, order_number): 
""" 
Handle successful checkouts
 """ 
Here in the checkout success view. All we need to do is check whether the user is authenticated. re-fill all its fields with the relevant information.
# Profile App - Part 9 & 10
-   Go to webhook handler to update the user authentication experience
*TIP* to select multiple areas to type at once use:
 Alt + Click and use END, HOME 
AND CONTROL LFT/RGHT 
to skip around and make changes much faster
-    comment out the form submit(); function(line 111 in checkout/js) so that form will fail then go and test the function. the webhandler should 
      successfully allow the payment to go through even if the form fails.
      And we'll never get to the checkout success page.
        If our code is working though that should be no problem
        since the webhook handler will catch the payment intent succeeded webhook from
        stripe and handle everything for us.
        Even with our form completely broken. Payments still work, and we can see
        stripe posting to the webhook URL in the terminal.  It will still show in admin
        profile was attached as expected.
        In fact even though the checkout page failed.
        If the user were to come back to their profile. Later on, they'd see it in their order history.
        Let's re-enable form submission in the stripe elementsJavaScript file.
        you will see this in admin (go to orders and you will see it has been successfully posted, 
        and stripe posting to the webhook URL in the terminal that payment has succeeded.
        Stripe has the payment and it has succeeded in the webhooks on stripe
        Re-enable form submission in the stripe elementsJavaScript file. Save and commit as "045 profile part5 update webhookhandler to handle profiles"
# Product App - Part 1 & 2
        create forms.py in product app
        add to products views 
        With the product form ready to go.
        We can now create a view for store owners to add products to the store.
        In the product apps views.py, I'll call this view add_product
        And for now, all it will do is render an empty instance of our form so we can see how it looks.
        It will use a new template which we'll create in a moment called add_product
        And will include a context including the product form
        Now create a new url for it and call it add_product
        Add an iteger to it - go to website and test it out then commit 
        Then go over to views.py in products and  Finish The Add Product Functionality

# Product App - Part 3 & 4
     Add new products to add_product page 
     add to views.py in products and success notification tries to render the image with its url.
        To fix this we can just add a simple if statement around whether to render the image
        and if it doesn't have one we'll render the default no image.   
        Also add to toasts_success.html to render the default image if there is no image to avoid throwing an erro.
        Also go to shopping bag page and fix it there too
        With that done let's add a link to the add product page in the base template.
        then test it out and add an image url and check it out on site and admin then commit "finish the add product functionality"
# The Edit Page
    Duplicate the *add_product* page and change accordingly to suit the edit page
        Rename it.
        Change the heading here to edit a product
        And the button at the bottom to update product
        also need to send our form to a new URL called edit_product
         include the product ID with it.
            Now we need a new view to render this template.
            So let's go to *views.py* and create a new view called edit_product.
            Which will take the request and the product ID the user is going to edit.
            Let's start by just pre-filling the form by getting the product using get_object_or_404 etc etc
            then go to urls.py to add the path `path('edit/<int:product_id>/', views.edit_product, name='edit_product'),`
            go to terminal and then to server and run `products/edit/1` to see and edit the page

