
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
    Let's build main-nav.html.
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
-    more list items added:
1.  clothing
1.  homeware
1.  special offers
-   finish, save and include in base.html
- add mobile views to base.html / run and test in browser
## Adding products
`python3 manage.py startapp products`
Add to installed apps in settings.py
`mkdir products/fixtures`

Add categories and products json
`https://jsonformatter.org/ `
to validate

Go to models.py and add code There - `python3 manage.py makemigrations --dry-r`
dry run 
-   `pip3 install pillow`
- dry run again...
- `python3 manage.py migrate --plan`
- `python3 manage.py makemigrations`
-  `python3 manage.py migrate`
    *then*...
-`python3 manage.py loaddata categories`
`python3 manage.py loaddata products`

check it out - python3 manage.py runserver - go to admin

## products admin

`mkdir -p products/templates/products`

file = `products.html`

 -     we're creating that inner products directory to make
        sure that django knows which app these templates belong to.
        In case any of them end up having the same names as other templates.
        And let's now create a products.html inside that directory.
        And copy the content of the home template in as a shell.
        The products template will still extend base.html
        And will still require static files as well as the page header


`python3 manage.py runserver`

## Product Details
Starting with main `nav.html` let's add url products for this link.
And then we'll add the same here on the shop now button in `index.html`.
To `create the product details page` we need a new `view` which will take the `product id` as a
parameter and return the template including the product, this will be
almost identical to the *all products view* so I'll copy that as a base.

## Shopping cart

-   `python3 manage.py startapp bag`
-   add to settings:
    installed apps `bag`
-   add `views.py` by copying and pasting the views from home and changing the wording to the appropriate views.
-   create `urls.py` and add to the bag directory - copy and paste from home urls and add as appropriate urls code.
-   And then include the `bag URLs` in the `project level URLs` file.
-    head over to `base template`  Add the link to view the bag.
-    head over to `mobile-top-header`  Add the link to view the bag in there too. 
-    `python3 manage.py runserver`
-   add `contexts.py`
-   commit changes

-       alt + click to select mutltiple regions
-  
-   when making changes to the model make sure you do the following to check all is correct:
    `python3 manage.py makemigrations --dry-run`

    products/migrations/0002_auto_20200605_0009.py
    - Change Meta options on category
    - Add field has_sizes to product
    The above report is technically a bug in django but because it is not critical developers have chosen not to fix it as it could cause other issues along the way.  So it is ok to go ahead and make migrations
-   `python3 manage.py migrate --plan` to verify the migrations we are making
-   and then `python3 manage.py migrate`
-   `python3 manage.py shell`
-   input into the shell for quick 'on the fly' without having to resort to your views.py 

-   
    `python3 manage.py shell`
-   input into the shell for quick 'on the fly' without having to resort to your views.py 

-   `from products.models import Product `
-   `kdbb = ['kitchen_dining', 'bed_bath'] `
    `clothes = Product.objects.exclude(category__name__in=kdbb)`
    `clothes.count()`
    for item in clothes:
    item.has_sizes = True
    item.save()
-   `Product.objects.filter(has_sizes = True)`
-   `Product.objects.filter(has_sizes = True).count()`
-   130
-   exit()


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
## Adjusting and Removing Products Part 1
        Go to bag views and copy and paste for views in bag dir.  Adjust as required for the adjustment & removal of products
    -   views.py
    -   add URL for it
    -`  shopping bag template submit item to the adjust bag view
## Adjusting and Removing Products Part 2
    -   get jquery code  in minified form here from codejquery.com
    `       'https://code.jquery.com/'

    -   *new folder in bag directory called templatetags/bags_tools.py*
    -   
    -  *new __init__.py new file to accompany the template/bags_too

## Checkout

-   `python3 manage.py startapp checkout`
Add to the models.py in the checkout app and then dry run the applications to be created.
    `python3 manage.py makemigrations --dry-run`
    then 
     `python3 manage.py makemigrations`
     then
    `python3 manage.py migrate --plan`  to make sure we are not missing anything
    then finally actually run them:
    `python3 manage.py migrate`     
    Let's commit these changes with git add .
    git commit -m "created check out app and models"
    git push

## Create models
Create models.py 

## Admin, Signals & Forms Part 1
Add to admin.py 
first import the order and OrderLineItem models - check it out in the admin on site.
Create signals.py in the same level as models.py in checkout.
Update the apps.py in checkout.


