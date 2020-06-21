## Stripes Part 13 & 14 & 15 & 16 & 17
# Stripe 13
-   Before we get to the webhook code though we need to make
    a small addition to the *stripe elements javascript*
    Basically since the payment intent .succeeded webhook will be coming from stripe
    and not from our own code into the webhook handler, we need to somehow stuff the
    form data into the payment intent object so we can retrieve it once we receive the webhook.
    Most of this we can do by simply adding the form data to the
    confirmed card payment method. 
    For example if you were to look at the *stripe documentation* and see the structure of a payment intent object.
    You'd see it has a spot for a billing details object we can add right here under the card.
    It can take a name, email, phone number, and an address with mostly
    the same fields we've got in our form. 
    Add all this in getting the data from our form and using the trim method to strip off any excess whitespace.
    We can also add some shipping information with all the same fields except for email
    -   write a simple view to take care of it.
        let's head over to views.py and make a quick view called cash_checkout_data
        We'll expect only the post method here so I'll use the require_POST decorator
        and let's import that, an HttpResponse up here at the top.
        What's gonna happen here is before we call the confirm card payment method in the
        stripe JavaScrip. we'll make a post request to this view and give it the
        client secret from the payment intent. If we split that at the word secret the
        first part of it will be the payment intent Id, so I'll store that in a variable called pid.
        Then I'll set up stripe with the secret key so we can modify the payment intent.
        To do it all we have to do is call stripe.PaymentIntent.modify
        give it the pid, and tell it what we want to modify in our case we'll add some metadata.
        Let's add the user who's placing the order. Will add whether or not they wanted to save their information.
        If everything goes ok we should get a 200 response
# Stripe 14
-   finish this up let's first go create a URL to access our new view.
    And then go back to the JavaScript and create a few variables.
    We can get the boolean value of the saved info box by just looking at its checked attribute
    We'll also need the CSRF token which we can get from the input that Django generates on our form.
    Which will have a name of csrfmiddlewaretoken
    To do this we'll use our trusty post method built into jQuery
    -      Telling it we're posting to the URL and that we want to post the post data above.
            We'll want to wait for a response that
            the payment intent was updated before calling the confirmed payment method
            and this is really easy to do by just tacking on the .done method and
            executing the callback function.
            In the callback function, in other words, the one
            that will be executed if our view returns a 200 response, all we have to do
            is all the stripe stuff we're already doing, so we can just paste the whole
            stripe function inside here and we're done
            ttach a failure function, which will be triggered
        -if our view sends a 400 bad request response. And in that case, we'll just
            reload the page to show the user the error message from the view.
            Let's collapse these functions down a bit and review the sequence of events.
            When the user clicks the submit button the event listener prevents the form from submitting
            and instead disables the card element and triggers the loading overlay.
            Then we create a few variables to capture the form data we can't put in
            the payment intent here, and instead post it to the cache_checkout_data view
            The view updates the payment intent and returns a 200 response, at which point we
            call the confirm card payment method from stripe and if everything is ok
            submit the form.
    -   overlay will
            be hidden the card element re-enabled and the error displayed for the user.
            If anything goes wrong posting the data to our view. We'll reload the page and
            display the error without ever charging the user.
            This may seem like a lot but I encourage you to review this and make sure you understand it.
            Passing data back and forth between the front end and the back end is the essence of full-stack development
    -   with all this finished let's head
            to the webhook Handler and print out the payment intent coming from stripe
            once the user makes a payment. With any luck it should have our metadata attached.
            The payment intent will be saved in a key called event.data.object
            So we'll store that and print it out.
            Now let's go submit an order and see if it all works.
            As you can see in the terminal now. Here is our modified payment intent with the
            billing information attached.
            As well as our metadata.
            And, of course, the shipping information.
            We're now passing information from our custom form to stripe securely
            via the payment intent.
            And recapturing it in the webhook so we can use it to add the order to our database.
            Now is a good time to commit our changes and in the next video you'll
            see the value of this webhook handler as
            we complete the code for it and test how our payment system would stand up to an
            impatient or unwitting user
# Stripe 15
    -    passing customer information through a
            stripe payment intent as metadata.
            There are many reasons developers may want to do this but in our case,
            we're doing it to ensure that all orders are entered
            into our database even in the event of a user error during the checkout process.
            In this video, we'll finalize that code and test it out.
        -   et started let's get the payment intent id, as well as the shopping bag
            and the users save info preference from the metadata we added in the last video.
            I'll also store the billing details, shipping details, and grand_total
            All of which we'll need in a moment.
            Now to ensure the data is in the same form as what we want in our database.
            I'll replace any empty strings in the shipping details with none.
        -   Most of the time when a user checks out, everything will go well and the form
            will be submitted so the order should already be in our database when we
            receive this webhook.
            The first thing then is to check if the order exists already.
            If it does we'll just return a response, and say everything is all set.
            And if it doesn't we'll create it here in the webhook.
            Let's start by assuming the order doesn't exist.
            We can do that with a simple variable set to false
        -   I'm using the iexact lookup field to make it an exact match but case-insensitive.
            If the order is found we'll set order exists to true,
            and return a 200 HTTP response to stripe, with the message that we verified the order already exists.
            If it doesn't exist let's create it just like we would if the form were submitted.
            In fact, we can get almost all the code we need from the view that does the same thing.
            We'll still want to iterate through the bag items, the only difference here is
            that we're going to load the bag from the JSON version in the payment intent
            instead of from the session.
            Also, we don't have a form to save in this webhook to create the order
            but we can do it just as easily with order.objects.create
            using all the data from the payment intent.
            After all, it came from the form originally anyway
        -   wrap this whole thing in a try block.
            And if anything goes wrong I'll just delete the order if it was created.
            And return a 500 server error response to stripe.
            This will cause stripe to automatically try the webhook again later
        -   wrap this whole thing in a try block.
            And if anything goes wrong I'll just delete the order if it was created.
            And return a 500 server error response to stripe.
            This will cause stripe to automatically try the webhook again later.
# Stripe 16
    -Go to models.py and add code There -  dry run
    `python3 manage.py makemigrations --dry-run`
    make migrations:
    `python3 manage.py makemigrations`
    then migrate:
   - `migrate: python3 manage.py migrate`
   - add fields to admin
   - update views when forms submitted
   - To do that first add a hidden input 
     to the form in the check out (html)page containing the client secret
   - And then go to views.py and get it if the order form is valid
     And split it to get the payment intent id like we did in the cash check out data view
   - We need a few imports here at the top of webhook handler now
    since we're doing more stuff with it, add those now
    We need the Order, OrderLineItem and product models
    As well as the json and time modules from Python
# Stripe 17
- test the purchase process on the website with webhooks succeeded as the complete success of the purchase
- FINISH - Next page....
