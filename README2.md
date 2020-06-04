page 2/
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
`.  Let's build main-nav.html.
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
- 3 more list items added:
1,  clothing
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







Welcome Sara Oliver,

This is the Code Institute student template for Gitpod. We have preinstalled all of the tools you need to get started. You can safely delete this README.md file, or change it for your own project.

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: *Make Public*,

Another blue button should appear to click: *Open Browser*.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: *Make Public*,

Another blue button should appear to click: *Open Browser*.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the backend lessons.

## Updates Since The Instructional Video

We continually tweak and adjust this template to help give you the best experience. Here are the updates since the original video was made:

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

--------

Happy coding!
