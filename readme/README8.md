## Shopping bag
Shopping bag needs tyding up
And this is really just because a horizontal table doesn't work well as a mobile design.
Without forcing the user to scroll sideways which is just an awkward user experience.
In order to maintain the same experience on mobile.
Lets Refactor it into a grid instead of a table. But only on mobile views.
To accomplish this elegantly - break the bag table up into a number of
includes which we can reuse.
If we look at the layout of the page it's broken into several core pieces.
The product image the product info its price the quantity selector the subtotal
and the bag total and check-out buttons at the bottom.
We can reuse all these chunks of code and just put them into a grid instead of a table.
So create a separate HTML file for each one which we can include in each layout
                        *product-image.html*
                        *product.info.html*
                        *quantity-form.html*
                        *bag-total.html*
                        *checkout-buttons.html*
We copy each block of code into its respective file.
So copy the product image block and save that.
Then copy in the product info.
Grab the entire quantity form and save that in its own HTML file.
And do the same for the bag total and checkout buttons.
Delete each block in bag.html
And replace it with the appropriate include statem
        create the mobile layout I'll create a div here with display block
        and display medium none. So it will only display on mobile.
        And while I'm at it I'll set the opposite on the table so it'll be hidden on mobile.
        But display on medium and up.
        Back inside this mobile div. Let's make two rows each with a single full-width column.
        The first one will include the bag total and the next will include the
        checkout buttons and a small paragraph letting the user know that a summary
        of their bag contents is below.
        And I'm putting these at the top just so the user doesn't have to scroll all the way
        to the bottom of the page to find the checkout button.
        Check it out to see how it looks so far.
        We need to iterate through the bag items
            and generate a row for each item.
        Each row will have four columns stacked on top of each other on extra small screens.
            and side by side on small.
                    In the first column, place the product image.
                    The second will have the product info.
                    The third will contain the price and the subtotal.
                    And the last will contain the quantity form.
            Lets include another row with the horizontal divider after each product.
            Lastly, as this is mobile layout, it could get quite long if there are a lot of products.
            Give the user a quick way to get back to the top of the page by
                    copying the back to top link from the products page along with its JavaScript.

            With both the link and the JavaScript copied.
            let's take a look at our new shopping bag page.
            With everything across the site looking quite nice on all modern screen layouts.
I'm going to call this visually finished and commit changes.

In the final video, we'll take a look at the problems monitor in gitpod.
And fix any bugs in our Python code.
To finally complete our e-commerce store

## Flake8 and Python refactoring 
    - run command: 
            `python3 -m flake8`
     to see all the output issues 

    hold ctrl and click on the individual files.
It will take me right to that line where the issue is.
Taking this first one for example. It's just telling us that the line is too long
And we should reformat our code to make it less than 79 characters.
This is just a style convention. And an easy way to fix the problem with imports
is to wrap them in parentheses so we can move them down to the next line.
        Ignore migration issues as developers do not need to use them visually
        UNUSED IMPORTS - Another common issue we're seeing here is imports that are unused.
                            This is because for example in the home app.
                            Django created a models.py for us
                            But we never used it. Since that app has no models.
                            Some developers prefer to just delete these files if they're not being
                            used to get rid of the warnings.
                            If you see a warning like this in a file you are using you should just remove the import
                            since you're not using it anyway.
                            In general most of the issues in this project seem to be code style issues.
                            Which of course we should fix.
                            Ultimately they're not critical to the functionality of our project.
So you can feel free to choose whether to fix them.
As long as you ensure these types of warnings don't show up in any projects
you submit for assessment.


## Heroku deployment

`pip3 install boto3`
`pip3 install django-storages`
`pip3 freeze > requirements.txt`
======//---

If you are having trouble with login:
2 factor login:
heroku login -i
heroku logs --tail -a sjk-boutiqueado



