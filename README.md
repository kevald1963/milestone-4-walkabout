# Walkabout 

Walkabout is a general app for managing leafleting, canvassing and surveying campaigns.

**Inspiration for project**

I am an active member of South Tyneside Green Party (STGP), an affiliate of the Green Party of England and Wales (GPEW). The idea for developing this app has come from my own experience of leafleting on behalf of STGP using paper copies of maps and street rounds. These are not only cumbersome to handle and susceptible to weather conditions but, from an organiser’s point of view, the later collation of valuable information from the round, such as missed streets and households, new supporters, and so forth, is difficult and time consuming, especially across several teams of activists. Furthermore, while most leafleting campaigns cover every household in the round, there are times when only specific households are delivered to e.g. New Year cards to supporters. Canvassing also tends to be targeted at known or likely supporters. Correctly selecting the data for printing out data for specific households only, is currently a labour-intensive job. An app could automate all these routine and tedious functions.

However, this app is not just for use by political parties, it can also be used by parcel delivery companies, market researchers, trade advertisers, community groups and so on. The app has been written so that much of the content relating to the organisation using it, is stored on the database so that it can be displayed on the app's pages rather than hard-coding into them. This means that the content can easily be changed by the end user. Various custom pages have been created to allow management of such user data.

**Glossary of terms**

- Campaign. A Campaign refers to the leafleting, canvassing and surveying activities that occur across a geographical area. They are made up of a set of Rounds.

- Round. A Round is a group of streets within a geographical area.

- Street. A Street is a generic term for any place where households, businesses or other types of properties are situated, and includes paths, roads, lanes, avenues, cul-de-sacs, courts, etc.

- Address. An Address is an individual property or tenancy where people live, work or gather for an activity.

**Commercial considerations**

I have approached the development of this app with a view to making it a professional product that would not only satisfy the criteria of the milestone project but could, perhaps, be further developed beyond to become a useful app in the real world.

I have implemented the following approach to its design:

- Have generalised the app in such a way so that it can easily be configured, without too much technical intervention for use by commercial companies involved in leafleting, parcel delivery, etc. By ‘generalised’, I mean abstract as much content (like logos, organisational titles, organisational terms, etc) as possible into the database so the front-end needs little, or no, change between different customers.
 
- A limited, free product is offered to appeal to community organisations and small businesses. Limitation will be implemented by the number of devices that can concurrently use the app at anyone time. Larger organisations will be able to purchase subscriptions for larger numbers of concurrent devices. These products are called BASE products.

- Paid-for address data loads will be available to all customers, even for those with the free product. They wil only be limited by the number of devices their base product allows. 

**How the app operates - or should!**

The purpose of the app is to earn revenue by providing a convenient data service to organisations involved in leafleting, canvassing and surveying campaigns.

The app is well-developed but from a real world point of view it is still a prototype. It currently only caters for one customer organisation. Obviously, it will need to cater for many if it is going to earn any serious revenue. It is absolutely crucial that data does not get mixed up between customers, so a separate schema for each may need to be created for each at the time of them subscribing. 

Here is the typical expected scenario for a new customer looking for an app for their campaigning needs:

- They browse the site for information about the app without registering to begin with.

- They want to try, or buy, the app, so register on the site first. Alternatively, they select a product, view it in the cart and try to check it out. If they have not registered then they will be asked to do so at that point before being allowed to proceed.

- They enter their order and make payment.

- Their schema is created with all necessary tables and the following is done:

  - An Admin group, with permissions, is created and the user is assigned to it.

  - The parent organisation data is created from the order header.

  - The subscription data is created from the order details.

- The customer will now be granted access to all data entry forms to create Admin and Agent users, create sub-organisations or groups for campaign purposes. 

- They will also be able to create campaigns, rounds, streets and addresses, or use a paid-for address data load if they do not want to create all the addresses they need.

## UX

**User Stories**

Initially, the site will have five types of User: 
- Superuser
- Administrator
- Agent
- Guest
- Anonymous.

It may be desirable to create other types of users, e.g. a Trusted Agent with some administrative permissions. A facility to do this is included in the app functionality.

**User Types**

*Anonymous users*

These are visitors who are not yet registered, or signed in to the app. These will only be able to see and use the app’s landing page, information pages, product page, cart page, etc. They will not be able view or create any campaign data until they either register a product or sign in with the appropriate Agent or Administrator permissions set up for them.

*Guest users*

These are visitors who have registered and signed in with a view to subscribing to the app. Typically, they will be representatives of businesses, charities, local government, or they may be a sole trader, such as a tradesperson, who wants to use the app to assist in advertising their service. They will not only be able to see and use the pages available to Anonymous Users but, crucially, will be able to access the checkout to make a subscription, free or paid-for. Initially, they are not assigned to any group, so have no permissions, but once they have subscribed to a product, they will be assigned to the Admin group and thereby become Administrators over their own systems.
 
*Agents*

These are the people who do the literature deliveries, canvassing or surveying. They have access to data that pertains to the particular campaigns to which they have been assigned. An Administrator can also act as an Agent of the same organisation. It is important that app users do not accidentally, or deliberately, perform CUD (Create, Update and Delete) operations on data outside their assigned round, hence the need for this user type so that data for their round is ring-fenced to them and other members on the same team. At the same time, movement of members between teams needs to be flexible to cope with changing circumstances on the ground. Assignment of such members to different rounds needs to be done without waiting for the approval of an Admin User. Agent status will be conferred on a user by assigning them to the Agent group. See below for permissions.

*Administrators*

This is the app’s customer organisations, or any trusted individuals assigned by them to such a role. They will have full control over the entire data content of the site, including creating, viewing, updating, archiving and deleting of any data. Most of this should be possible through the app, rather than by direct access to the database. Administrator status will be conferred on a user by assigning them to the Admin group. See below for permissions.

*Superusers*

This is the owner of the app, and/or the owner’s employees or representatives. They will have access to all data on the system. A Superuser can also act as a customer Administrator, if intervention is required to correct problems in a customer’s system such as diagnosing a data corruption, faulty page or whatever.

*Security issues*

There is an issue with the current version of the app, in that there is nothing stopping an Administrator to assign Superuser status to themselves or someone else. An attempt was made to disable the 'Is superuser?' field in the Django Admin system to all except Superusers, but was unable to get it to work. This will be dealt with in the next phase.

**Django default Group Permissions**

These are not set up manually, but are created when a first base product has been successfully subscribed to. Thereafter, checks are made on subsequent subscriptions to see if the groups exist. If they are not they will be recreated.

*Agent Group:*

* campaign | campaign | Can change campaign

* round | address | Can add address
* round | address | Can change address

* round | round | Can add round
* round | round | Can change round

* round | street | Can add street
* round | street | Can change street

*Admin Group:*

* auth | group | Can add group
* auth | group | Can change group

* auth | user | Can add user
* auth | user | Can change user
* auth | user | Can delete user

* campaign | campaign | Can add campaign
* campaign | campaign | Can change campaign
* campaign | campaign | Can delete campaign

* organisation | organisation | Can add organisation
* organisation | organisation | Can change organisation
* organisation | organisation | Can delete organisation

* round | address | Can add address
* round | address | Can change address
* round | address | Can delete address

* round | round | Can add round
* round | round | Can change round
* round | round | Can delete round

* round | street | Can add street
* round | street | Can change street
* round | street | Can delete street

**Anonymous User stories to be catered for:**

I want to

- Register myself as an app user.

- Login to the app.

- Logout of the app.

- Explore the apps pages for information on what it does, how it works, products offered, how much it costs, etc.

**Guest User stories to be catered for:**

- All the things that Anonymous User can do.

- Select a product, or products, and place it/them in the cart.

- Go to the checkout and subscribe to the app, for the free or paid-for service. 

**Agent User stories to be catered for:**

- Assign myself to a round if no round has been assigned to me.

- Transfer myself from one round to another where this is desirable.

- view an interactive map of the round I have been assigned to.

- view a list of streets, and addresses within those streets.

- update individual addresses as ‘not done’ where I have been unable to access them, and record a reason for doing so against each of them.

- update an entire street as ‘done’ once I have covered it, whether or not there are individual addresses that are ‘not done’. I should get an overrideable warning message if the number of addresses ‘done’ is less than a certain percentage. 

- update the entire round as ‘done’, but only if all streets within it have been updated as ‘done’.

- update the entire round as ‘part done’, if only some of the streets within it have been updated as ‘done’. I want to record a reason for doing this.

- update the entire round as ‘done’, even if some streets within it have not been updated as ‘done’. I should get an overrideable warning message if I try to do this.

- insert a street, or individual addresses, if they have been missed off the round, and record a reason for doing so.

- hide (but not delete) a street, or individual addresses, where they have been included in error, and record a reason for doing so.

- assign a street, or individual addresses, to another round where they have been included in this round in error, and record a reason for doing so.

- view other people’s rounds to check on their progress i.e. see which streets they have done.

- view information about other people’s rounds such as the percentage of addresses they have covered.

**Administrator user stories to be catered for:**

I want to

- carry out all the functions that an Agent User can do.

- Create organisations

- Create other Administrators for my system.

- Create Agents for my system.

- Create streets of addresses.

- Create rounds of streets.

- Create campaigns of rounds.

- View streets.

- View rounds.

- View campaigns.

- Update streets.

- Update rounds.

- Update campaigns.

- Delete streets.

- Delete rounds.

- Delete campaigns.

- Allocate individuals to a round.

- View the progress of a campaign i.e. view which rounds have been done.

- View the progress of a round i.e. view which streets have been done.

- View various statistics relating to a campaign or round.

### Wireframes

Although these are a good starting point, they bear little resemblance to the final design!

They can be downloaded from [this folder](https://github.com/kevald1963/milestone-4-walkabout/tree/master/_Project%20Documentation/Screen%20layouts) on GitHub.

### Database structure

The Postgres relational database has been used by this app for all dynamic data storage. The database contains the following tables:

- Users
- Organisation
- Campaign
- Round
- Street
- Address
- Product
- Order
- OrderLineItem
- Subscription (created but not yet used)

The structure is complex and needs a diagram to express the relationships properly. However, the size of the project overtook me so I will just give a brief description here:

- The Round, Street and Address tables are linked to each other by foreign keys .

- The Round and Campaign tables have a many-to-many relationship.

- The OrderLineItem has a FK relationship to both the Order and Product table.

- The Subscription has a FK relationship to both the Order and Organisation table but needs some further thought. 

- The relationships between User, Organisation and Campaign need some further thought. There are some FK relationships but many-to-many relationships may need to be implemented between all three tables.

## Features

Please click [here](https://...) to see the Functional Specification for this section. 
 
### Existing Features
- Feature 1 - allows users X to achieve Y, by having them fill out Z
- ...

For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.

In addition, you may also use this section to discuss plans for additional features to be implemented in the future:

### Features Left to Implement
- Another feature idea

## Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

- [HTML5](https://www.w3.org/TR/html52/) 
  - To build page structure and content

- [CSS3](https://www.w3.org/standards/techs/css#w3c_all)
  - To style page structure and content.

- [Bootstrap 3.3.7](https://getbootstrap.com/docs/3.3/getting-started/)
  - To provide template components to easily create and style responsive elements like the navigation menu, buttons, etc.

- [Google Fonts](https://fonts.google.com/)
  - For 'Roboto' font style used.

- [Font Awesome 4.7](https://fontawesome.com/icons?d=gallery)
  - Used to create 'icon' characters for menus, email links, etc.

- [JQuery](https://jquery.com) / [JavaScript](https://www.w3schools.com/js/js_versions.asp)
  - Used to simplify DOM manipulation for search fields, operation of collapsible components, etc.

- [Django 1.11](https://www.djangoproject.com/)
  - A Python framework for rapid web development.

- [Python 3.8](https://www.python.org/)
  - Server side programming language to interface between database and HTML pages.

- [PostgreSQL](https://www.postgresql.org/)
  - An open source relational database used to store all user data, accessed using Django's Object Relational Mapper.
  
## Testing

The huge scale of this project has prevented me from creating any automated tests for it. However, I am well aware of the crucial need for these in the next phase of development, where the project is going to get even bigger and more difficult to test.

However, I have thoroughly tested the project manually and documented the tests in the test plan below. The test plan consists of 74 functional and 16 responsiveness tests. I have written up any issues found in the Notes field of the relevant test.

- Excel workbook,'Test plan - Walkabout'. Download from GitHub [here](https://github.com/kevald1963/milestone-4-walkabout/blob/master/_Project%20Documentation/Test%20plan/Test%20plan%20-%20Walkabout.xlsx). 

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.

## Credits

### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)

### Media
- The photos used in this site were obtained from ...

### Acknowledgements

- I received inspiration for this project from X

[![Build Status](https://travis-ci.com/kevald1963/milestone-4-walkabout.svg?branch=master)](https://travis-ci.com/kevald1963/milestone-4-walkabout)