# Walkabout 

Walkabout is an app for managing political party leafleting and canvassing campaigns.

**Background**

I am an active member of South Tyneside Green Party (STGP), an affiliate of the Green Party of England and Wales (GPEW). The idea for developing this app has come from my own experience of leafleting on behalf of STGP using paper copies of maps and street rounds. These are not only cumbersome to handle and susceptible to weather conditions but, from an organiser’s point of view, the later collation of valuable information from the round, such as missed streets and households, new supporters, and so forth, is difficult and time consuming, especially across teams of activists. Furthermore, while most leafleting campaigns cover every household in the round, there are times when only specific households are delivered to e.g. New Year cards to supporters. Canvassing also tends to be targeted at known or likely supporters. Correctly selecting the data for printing out data for specific households only, is currently a labour-intensive job. An app could automate all these routine and tedious functions.

**Glossary of terms**

- Campaign. A Campaign refers to the leafleting, canvassing and surveying activities that occur across an electoral area, usually carried out within one calendar month. They are made up of a set of Rounds.

- Round. A Round is a group of streets within an electoral area.

- Street. A Street is a generic term for any place where households are situated, and includes paths, roads, lanes, avenues, cul-de-sacs, courts, etc.


**Commercial considerations**

I am approaching the development of this app with a view to making it a professional product that would not only satisfy the criteria of the milestone project but could, perhaps, be further developed beyond to become a useful app in the real world.

Although I my activities on behalf of my local Green party are done on a voluntary basis, a development such as this, along with ongoing support, would be too much to undertake without some form of remuneration. I have listed some business models ideas below that I am considering.

- The GPEW has a federal structure, with each local party responsible for its own funding and activities. Although, I surmise many local parties do not have high incomes or reserves, there are many of them, so the app could further developed on a ‘hobby’ basis and, after field-testing by my local party, be gradually licensed out to a number of them on a high-volume, reasonable-cost subscription basis, preferably with the endorsement of GPEW. One potential pitfall of this approach is the increasing amount of support required, so the app would have to be properly proven in field-use before being released. Data uploads and updates or training could additionally be charged for.

- Generalise the app in such a way so that it could also easily be configured, without too much technical intervention for use by commercial companies involved in leafleting, parcel delivery, etc. By ‘generalise the app’, I mean abstract as much content (like logos, organisational titles, organisational terms, etc) as possible into the database so the front-end needs little, or no, change between different customers. Commercial companies would be charged a commercial rate for a licence subscription. Any remaining revenues, after costs, could be used to subsidise the subscription cost to local Green parties wanting to use the app.

- Give the app away for free to local parties but with in-app adverts to fund development and support. The adverts could be removed on payment of a subscription. Such adverts, and the organisations that produce them, would have to be carefully vetted to ensure they comply with the Green Party’s core values and standards. This approach is unlikely to be financially viable, as the audience would not be large, even across all local parties affiliated to GPEW.

- A series of crowdfunding efforts by the local party (or a consortium of local parties) to fund the development and marketing of the app. My local party has successfully used crowdfunding a number of times, so this may be a viable option. It’s a commonly used method of raising funds for election expenses across the GPEW. In return, the crowdfunding party (or consortium would get use of the app for free, or low-cost, an agreed share of any remaining revenues, after costs, generated from licensing the app to other local parties across England and Wales. I envisage the app could be installed for free, either with limited functionality, or with full functionality but with constraints on the amount of usable data, or the number of users accessing it at any one time. Such constraints could be automatically removed on payment of a subscription.

**Fulfilling the Milestone project criteria**

It is too early at this stage to decide which model to use but for the purpose of the milestone project, I will assume the latter scenario above i.e. that the app is in a well-developed state, and can be used for free, either with limited functionality or data. The customer organisation will then have the option remove those constraints on payment of a subscription using Stripe’s test functionality. I envision subscription payments would be made by the customer on behalf of a group of users, rather than individual users making payments themselves i.e. a local Green party would pay on behalf of its active members, or a commercial company would pay on behalf of its employees. I will generalise the app, so that it is “future-proofed” for potential use by other organisations, not just local Green parties. In any case the idea of separating content from presentational structure is a good development practice that appeals to me.

## UX

**App Audience**

The app is primarily aimed at local Green Party activists to help them manage election leafleting and canvassing in local council wards or parliamentary constituencies. As discussed above, the app may also be of use to commercial companies for bulk leafleting, parcel delivery, etc.

### User Stories

Initially, the site will have two types of User: Basic and Admin. It may be desirable to create other types of users, e.g. a Trusted User. A facility to do this will be included in the app functionality.
**User permissions**

**Basic Users**

It is important that app users do not accidentally, or deliberately, perform CHUD (Create, Hide, Update and Delete) operations on data outside their round, hence the need for this user type so that data for their round is ring-fenced to them and other members on the same team. At the same time, movement of members between teams needs to be flexible to cope with changing circumstances on the ground. Assignment of such members to different rounds needs to be done without waiting for the approval of an Admin User.

**Admin Users**

This is the app’s customer organisation, or any trusted individuals assigned by it to such a role. They will have full control over the entire data content of the site, including creating, viewing, updating, archiving and deleting of any data. Most of this should be possible through the app, rather than by direct access to the database.

**Basic User** stories to be catered for:

I want to

- Register myself as app user.

- Login to the app.

- Logout of the app.

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

ADMIN USER stories to be catered for:

I want to

- carry out all the functions that a Basic User can do (as above).

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

The files below are stored in:

[To be updated]

### Database structure

The MySQL relational database will be used by this app for all data storage. Table structures for this release are shown in the Excel spreadsheet below, stored in:

[To be updated]

## Features

In this section, you should go over the different parts of your project, and describe each in a sentence or so.
 
### Existing Features
- Feature 1 - allows users X to achieve Y, by having them fill out Z
- ...

For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.

In addition, you may also use this section to discuss plans for additional features to be implemented in the future:

### Features Left to Implement
- Another feature idea

## Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.


## Testing

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

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
