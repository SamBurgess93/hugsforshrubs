# HugsForShrubs

![Preview](???)

[Link to the Live Project](???).

HugsForShrubs has been built as the 4th milestone project as part of Code Institute's Full Stack Software Development course.
HugsForShrubs is a virtual 'E-commerce Website’ in whcih customers can purchase and browse Macrame plant hangers. It provides the user with a list of the various products available for purchase in the store. For the convenience of online shopping, a shopping cart is provided to the user. After the selection of the goods, it is sent to the order confirmation process for collection of payment. The system is implemented using Python’s web framework Django.

## Table of contents
1. [UX](#ux)
    1. [Project Goals](#project-goals)
    2. [User Stories](#user-stories)
    3. [Development Planes](#development-planes)
    4. [Changes Made During Project Development](#changes-made-during-project-development)
2. [Features](#features)
    1. [Existing Features](#existing-features)
    2. [Features to Implement in the future](#features-to-implement-in-the-future)
3. [Technologies Used](#technologies-used)
     1. [Languages and Frameworks](#languages-and-frameworks)
     2. [Applications](#applications)
4. [Testing](#testing)
5. [Deployment](#deployment)
     1. [Database Creation](#database-creation)
     2. [Local Copy Creation](#local-copy-creation)
     3. [Heroku App Creation](#heroku-app-creation)
6. [Credits](#credits)
     1. [Images](#images)
     2. [Code](#code)
7. [Acknowledgements](#acknowledgements)
***

## UX 
### Project Goals
The scope of this project is to create a 'E-commerce website'. 
 
This is my 4th and final Milestone Project that must be developed as part of my Full Stack software development course with Code Institute.

The primary goal of the HugsForShrubs website is engage with visitors to the website and as a result sell the handcrafted macrame plant hangers products.


### User Stories


**As a first time visitor, I want to:**

1. Easily understand the main purpose of the website.
2. Navigate through the site with ease.
3. View a list of specific products of my choosing based on their category. So that I can select a particular category of product from a specific list to buy.
4. View the details of a single product. So that I can understand the details and price of the product and also see and image of the product.
5. Sort the view of products by price low to high. So that I can make an informed purchased based on price.
6. Sort the view of products by price high to low. So that I can make an informed purchased based on price.
7. Be easily able to register and create my own account so I can have a personalised experience.
8. Receive an verification email to verify that my account was set up.
9. Easily view the value of my shopping cart anywhere on the website. So that I can understand how much I have selected.
10. Easily view a summary of what's in my shopping cart, including all prices such as delivery and grand total price before I purchase. So that I can see how much I will be spending.
11. See all reviews for the products.
12. Check out and purchase my items without having to log in. So that I can conveniently purchase items quickly.
13. Easily view the contact details for the company. So I can contact Hugs For Shrubs about my orders or requirements.
14. Have easy and quick access to the companies social media links.
15. Search for a specific product using keywords in a search bar.


**As a registered user, I want to:**
1. Login to my own account effortlessly so that I can access my profile to view my orders.
2. Logout of my account effortlessly to keep my details secure.
3. Easily recover my password if I forget it. So that I can recover my access to my profile.
4. Have a personalised profile so that I can view my order history.
5. View my order history, order confirmations, and saved payment information in my profile.
6. Be able to update my payment and personal details if required.


**As a superuser, I want to:**
1. Be able to add new products to the store easily.
2. Edit/update existing store products to change pricing, images and other criteria.
3. Delete items from the store.


### Development Planes

In order to design and create Hugs For Shrubs, I developer distinguished the required functionality of the site and how it would answer the user stories, as described above, using the **Five Development Planes**:

<strong>1. <u>Strategy</u></strong>

The Hugs For Shrubs is an online e-commerce site with front-end and back-end functionality, developed using HTML, JavaScript, CSS, Python and Django. The main objective is to create a site delivers on the user stories outlined above.

<strong>2. <u>Scope</u></strong>

The scope was created from using the Strategy previously defined. This allowed us to align the features to deliver on the strategy/ user stories. This was seperated into two categories:
- **Content Requirements**
     - The player will be looking for:
          - Dynamic and inviting visuals
          - Simple and vibrant content
          

- **Functionality Requirements**
     - The user will be able to:
          - Search with ease using a search bar
          - Log In to their own profile
          - Make payments with ease
          - Access to all products
          - Register for profile
          - Get contact details for owner

<strong>3. <u>Structure</u></strong>

### Allauth features
The sign up, register, password reset, email confirmation pages etc, have all been provided by Django allauth and formatted to suit the needs of the site.

#### Admin Features
  - Admin will have access to additional features across the site. Firstly admin members will have an additional icon in the delivery banner (on larger devices) or link in the burger menu (on smaller devices) to take the user to the site admin page. Here the admin user will have access to:
    - Add a product page link - This will take the admin user to the add product page. Here the user can fill in the form to add a product to the site. Once added the admin user will be taken to the product detail page for the product added.
    - On the product page and product detail page admin users will have access to the edit and delete products. The edit icon will take the user to the edit product form, where they can make changes to a product (i.e chnage the price). The delete icon will trigger a modal to make sure the user wishes to delete the product and avoid accidental deletions.

### Base Template
* Delivery Banner - The delivery banner contains information about free delivery and the free delivery threshold. It is fixed to the top of the screen to allow for ease of access and improved user navigation. The links take users to different parts of the site which are as follows:
 - Unregistered user:
   - Login link
   - Register link
 - Registered user:
   - Saved Items
   - My Account - Profile, Logout
   - Shopping Bag
 - Admin/ superuser
   - Wishlist
   - My Account - Product Management, Profile, Logout

### Navbar
The navbar has all product category links,
- All Products - here products may be sorted and selected based on price, name, rating or category
- Errigal - Errigal type plant hangers
- Eske - Eske Type plant hangers 

### Footer
The footer has the links to the social media links and contains the contact email information.

### Homepage
The home page has the navigation links, logo, hero image, call to action button, product categories and the footer.
### About Me
The about page gives the user information on the company and owner. This will have an image.
### Product page
The product page displays all products in the store.
The sorting range button is also displayed here to allow the users sort products based on price, name and category.
### Product detail page
   The product details page includes, name of the product, price , category, rating and product description.
   There are also two button links one to keep shopping that leads to the all products page and the other add to bag button that adds the product to the user's shopping bag.
   Admin/ superuser has two links to delete or edit product .
### Toasts 
  - Toast message boxes have been used through out the site to display the feedback to the user when they have made interactions with the site. These messages are color coded to transmit different kinds of information:
    - Green: Success
    - Red : Errors
    - Blue : Information
    - Yellow : Warning
### Shopping Bag  page
  The shopping bag page can be broken into 5 parts for each product added to their cart:
  - Product - which displays an image of the product the user has added to their bag.
  - Product info - displays the name of the product and product sku. 
  - Price - displays the individual product price.
  - Quantity - Users are able to update their order using the quantity selectors and the update button. Users can also remove that product from their shopping cart entirely by clicking the remove button.
  - Subtotal - displays the subtotal for each product (product price * quantity).
Underneath the products that are in the user's cart, there is information for cart total, delivery and grand total. If a user does not meet the free delivery threshold a helpful message will be displayed to let them know what they need to spend in order to qualify for free delivery.
  - There is a button to take the users back to the all product page, and a "Secure Checkout" button to take the user to the checkout page.
  - If the user has no items in the shopping cart, a message is displayed to the user to let them know this and a button to take the user to the all products page is displayed.
### Checkout page
The Checkout page is split into two columns on larger devices, and 2 rows on smaller devices:
 - Order Summary - Gives a nice overview of each of the products that they are purchasing. Users can also see a breakdown of the order total, delivery and grand total.
 - Checkout Form - split into 3 sections:
   - Details - where users are invited to fill out their full name and email address. Email address will be auto populated if a user has logged in and saved this information to their profile.
   - Delivery - Users can fill in where they wish their products to be delivered to. These fields will be auto populated if a user has logged in and saved this information to their profile.
   - Payment - Users can enter their card details here in order to make payments and purchase their chosen products.
 - Below the checkout form, users can click the "Adjust bag" button to make adjustments to their shopping bag, or click the "Complete Order" button to make their purchases. Users are informed exactly how much they will be charged with a helpful message directly underneath the "Complete Order" button.
 ### Checkout success page
 - When a user successfully checks out a success toast will be shown to the user with the order number and a confirmation email will be sent to the user with some of the details of their order.
 - The checkout success page itself is split into two sections:
   - Order information which details the order info, delivery details and billing info.
   - Order Summary - Gives a nice overview of each of the products that they are purchasing.
 - More products link which will take the user back to the all products page encouraging the user to make more purchases.

 ### Profile page
   - Here users can update their default information by filling in the form and clicking update info button allowing them to make quick purchases at checkout.
   - Regarding information aboutuser's past orders, users can click the order number to take them to the checkout success page .
 ### Saved Items
  - The wishlists app allows signed-in users to create a list of saved Items. A user can add a product to their wishlist from the product detail page and manage their lists in the account section.
  - When the used has added products to their wishlist ; they will be displayed here in the same format as the products page.

### Features left to implement

