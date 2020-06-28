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
# Security measures
        Go to views.py in product and views.py in profiles


