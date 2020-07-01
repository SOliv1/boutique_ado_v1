# Product App - Part 3 & 4
     Add new products to add_product page 
     add to views.py in products and success notification tries to render the image with its url.
        To fix this we can just add a simple if statement around whether to render the image
        and if it doesn't have one we'll render the default no image.   
        Also add to toasts_success.html to render the default image if there is no image to avoid throwing an erro.
        Also go to shopping bag page and fix it there too
        With that done let's add a link to the add product page in the base template.
        then test it out and add an image url and check it out on site and admin then commit "finish the add product functionality"
# The Edit products Page
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
# Delete products page
        Finally users have the ability to delete products
        No template is required for this functionality
        All we need is a url and view
        then add the delete function in products/views.py
        get_object_or_404
        And then we'll just call product.delete.
        Add a success message.
        And redirect back to the products page.
        In this way whenever someone makes a request to products/delete/ some product id.
        That product will be deleted.
        I'm going to make a small change to the add_product view here also
        then change and add links to product.detail and on product.html page
# Security measures and tidy image fields
        Go to views.py in product and views.py in profiles git commit _m"securing views"
        Finally tidy the image field in djgango - go to Django github > go to django folder > Forms, then open widgets.py
        And search for ClearableFileInput then look for and add in widgets.py https://github.com/search?l=HTML&q=ClearableFileinput.html&type=Code
        Create widget and widget template 
        then lastly to forms.py and import our custom clearable file widget clas
# tools  https://www.diffchecker.com/dif

# Fixing image field
-   Add this in *base.css* since it'll be applied on both the edit template
-   and the add product template.
-   First we're going to set the overflow of the span wrapped around our file input two hidden.
-   And give it relative positioning.
-   Then for the actual input itself, we'll position it absolutely in the top right of the span element
-   add product template.
        First we're going to set the overflow of the span wrapped around our file input two hidden.
        And give it relative positioning.
        Then for the actual input itself, we'll position it absolutely in the top right of the span element
        giving it a min-width and height of 100% so it takes up the entire span.
        Now I'll give it zero opacity so it doesn't cover the button.
        And turn the cursor into a pointer.
        Effectively what we're doing here is making sure that the entire
        input which is clickable lives inside this span that looks like a button.
        And then making it invisible so it appears you're clicking the button.
        While I'm here in the CSS I'll also add some fine-tuning for the custom checkbox.
        update edit and add product.html to update the image field
    runserver and check to see how it all looks
    Add javascript to edit and copy to add.html and use *backticks '``'only

# Deploying to heroku app

-   Amazon  web services  - 's3' stands for simple storage service
-   deploy to heroku - go to website and create new project 
-   go to resources and search postgres and then click that to add the database
-   To use Postgres we need to 
            go back to gitpod and 
            install dj_database_url, 
            and psycopg2

    `pip3 install dj_database_url`
    `pip3 install psycopg2-binary`
    `pip3 freeze > requirements.txt`

    get stores new database setup. By going to *settings.py*
    and importing *dj_database_url*
    add to settings - replace default databasewith the following and going to settings in heroku revela vars and copy databse url:
            "# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
#   if 'DATABASE_URL' in os.environ:
#    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('postgres://bbwkjtasosvyad:a94d0cbfbfec0da1226df9090e480bca9e31d3a588fb0c933905a415db462ee3@ec2-54-247-79-178.eu-west-1.compute.amazonaws.com:5432/dfsgat5es99hd6'))
    }
#   else:
#    DATABASES = {
#        'default': {
#            'ENGINE': 'django.db.backends.sqlite3',
#            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#        }
#    }

## make migrations and load the data
-       `manage.py showmigrations`
        `Python3 manage.py migrate`
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




         
