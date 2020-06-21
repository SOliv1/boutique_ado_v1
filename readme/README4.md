## Stripes Part 13 & 14 & 15 & 16 & 17

# Stripe 13


# Stripe 14


# Stripe 15



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
- test the purchase process on the website 
- FINISH - 