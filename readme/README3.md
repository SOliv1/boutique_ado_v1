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
## Stripes Part 3
  - give stripe_elements some functionality with card event listener to check to see if there are any rrors.
  - if so then it will show on the checkout page - on card errors div we created near the card element on the checkout page.
  - update views.py in checkout with stripe card elemaents and then install `pip3 install stripe`
  - if not using gitpod you may need to look up the instructions on setting environemt variables called set on windows for your specific situation.
  - This should also work on OSX and Linux operating systems.  These will not be permanent. And you'll have to re-export them each time you start your workspace
    But if you're using gitpod you can make them permanent by going to your main workspaces page
    Clicking your account icon in the upper right. And going to settings
    And entering them there under the environment variables section.  However,
    if you're using gitpod you can make them permanent by going to your main workspaces page
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
