Cont..from page/2
## Stripes Part 2
Go to:
    https://stripe.com/docs/payments/accept-a-payment#web-collect-card-details
    get the javascript details and paste in check_out.html in corejs script at top and at the bottom of template - 
    save and inspect values for values. Public key matches secret.client key. 
    get basic styles from the stripe js Docs.  Update the default colour of the element to black.
    And I'll change the invalid colour to match bootstraps text danger class.
    I can also get some CSS for our actual CSS file from the stripe documentation
    which I'll paste in here.  test and check that all matches with the 
    -   js/stripe_elements.js 
    -   and css.check_out.css
## exp Part 3
  - give stripe_elements some functionality with card event listener to check to see if there are any rrors.
  - if so then it will show on the checkout page - on card errors div we created near the card element on the checkout page.
  - update views.py in checkout with stripe card elemaents and then install `pip3 install stripe`
  - export environment variables
  
        export STRIPE_PUBLIC_KEY=pk_test_51GtAGjDvyPDUJbikVWyYOumfWpQlZdzXnhDKRPPeNvSX0RTApmHnUmOvnsgpHwaqoUUp5ekqlKl8xxHlcFyKKvVT00WWP5gmou
        export STRIPE_SECRET_KEY=sk_test_51GtAGjDvyPDUJbikpwurphl2orPFN3yLUIWg7GhBxnGFoyPtIhS1RjlSldLJjsItel7d2OWONC3Yj8uPudKqXpmS00hqKMIbtF
  - 
  if not using gitpod you may need to look up the instructions on setting environemt variables called set on windows for your specific situation.
  - This should also work on OSX and Linux operating systems.  These will not be permanent. And you'll have to re-export them each time you start your workspace
    But if you're using gitpod you can make them permanent by going to your main workspaces page
    Clicking your account icon in the upper right. And going to settings
    And entering them there under the environment variables section.  
## Stripes Part 4
        **update in checkout views.py:
        order_form = OrderForm()

        if not stripe_public_key:
            messages.warning(request, 'Stripe public key is missing. \
                Did you forget to set it in your environment?')
        template = 'checkout/checkout.html'
        context = {
            'order_form': order_form,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,
        }**
## Stripes Part 5
    add `listener` by copying from stripe docs and make a few changes. 
    Since we are writing in java script we need to stick to best pratices and change all variables to camel case.
    stripe test card number = 4242424242424242
    You can use any CVC, any date in the future for the expiration date.
    And any five-digit postal code.
## Stripes Part 6 - success order order_form
        Create checkout/views.py continue success orderform
        add to checkout/urls.py success
## Stripes Part 7
        Make sure you add env.py to your project so that the Stripe card system works and that it is secure.
        
        import os

        os.environ.setdefault("STRIPE_PUBLIC_KEY", 'pk_test_')

    
        os.environ.setdefault("STRIPE_SECRET_KEY", 'sk_test_')
        
        Create success template along side of checkout.html template
        Go to init-_py and add details to that
            *default_app_config = 'checkout.apps.CheckoutConfig'*
        make a tiny adjustment to the order models update_total method
        by adding or zero to the end of this line that aggregates all the line item totals.
        This will prevent an error if we manually delete all the line items from an order
        by making sure that this sets the order total to zero instead of none.
    -   add credentials again:
            export STRIPE_PUBLIC_KEYm=pk_test_51GtAGjDvyPDUJbikVWyYOumfWpQlZdzXnhDKRPPeNvSX0RTApmHnUmOvnsgpHwaqoUUp5ekqlKl8xxHlcFyKKvVT00WWP5gmouy 
            export STRIPE_SECRET_KEY=sk_test_51GtAGjDvyPDUJbikpwurphl2orPFN3yLUIWg7GhBxnGFoyPtIhS1RjlSldLJjsItel7d2OWONC3Yj8uPudKqXpmS00hqKMIbtF

                test card no = 
                4242424242424242
## Stripes Part 8 & 9
        Add a *border* around the checkout_success.html - add summary to order checkout success page.
        add an *overlay* to checkout success page and then add to the checkout css page as well at the bottom
        Add a loading spinner in checkout.html
        -   https://stripe.com/docs/payments/accept-a-payment#web-test-integration

        -  second test card no. to trigger the overlay spinner:- 
            test card spinner:- 4000002500003155
        -   to test the integrations for stripe payments and the spinner overlay.
## Stripes Part 10 & 11 & 12
        - Create webhook_handler.py then import `from django.http import HttpResponse` add code.
        - These instances of webhook can be changed and modified by names and the directory and methods with each new project and update.
        - add to checkout urls
        - create webhooks.py and get the code directly from stripe add a few moderations
                https://stripe.com/docs/payments/handling-payment-events
                Triggering actions with webhooks
                    How to use webhooks to respond to offline payment events.
                    save and go to *settings.py* and add new environment variable
                    `STRIPE_WH_SECRET = os.getenv('STRIPE_WH_SECRET', '')`
                    to confirm it is working print('success!') in webhooks.py
                        print('success!')
                        returnHttpResponse(status=200)
               set up the stripe API key.
                set up the stripe API key.
                And the webhook secret which will be used to verify that the webhook actually came from stripe.
                And we'll need a few imports.
                We'll need our settings file to get the webhook and the stripe API secrets.
                We need HttpResponse so these exception handlers will work.
                We'll need our webhook handler class and of course stripe.
                And last we need two decorators require_post which as the name implies will make
                this view require a post request and will reject get requests.
                And CSRF exempt since stripe won't send a CSRF token like we'd normally need.
                Let's save that for now and head to settings.py
                And I'll add a new environment variable called stripe webhook secret
                which we'll get from stripe in a moment.
                To confirm the webhook view is working. Let's just print out success and then return a 200 response.
                To connect the URL, first we need to run the server in order to get the address of our site.
                I'll copy that and then go to the stripe dashboard.
                On the Left, I'll click developers.
                Then find webhooks.
                And select add endpoint.
                Now I'll paste in the URL and add /checkout/wh onto the end.
                Making sure to include the trailing slash.
                Click receive all events and then click add endpoint.
                This opens up the details of our new webhook endpoint.
            -   Get the signing secret.  go back to workspace and export:
                export STRIPE_WH_SECRET='whse....'
                restart the terminal
                then go back to stripe and test the webhook and if successful it should be seen in the terminal as a 200 checkout 
                


        