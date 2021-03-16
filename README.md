# Techfugees Rental App/Team-project-13-techfugees-toronto

> _Note:_ This document is intended to be relatively short. Be concise and precise. Assume the reader has no prior knowledge of your application and is non-technical.

## Description
 * Provide a high-level description of your application and it's value from an end-user's perspective
 * What is the problem you're trying to solve?
 * Is there any context required to understand **why** the application solves this problem?

Our team is working with Techfugees Totonto to build a web application that facilitates the housing search process for refugees and establishes a better mutual understanding and support between refugees, outreach workers, and housing providers.

In Toronto, only about half of refugees who have gone through the city’s shelter system in the past two years have been settled into permanent housing. Additionally, Toronto’s shelter system is operating at nearly 100% capacity. 40% of people staying in Toronto shelters are refugees. Additionally, settlement organizations that assist refugees in finding housing are understaffed and their employees are overworked.

This web application aims to solve the problems that refugees face when searching for housing. Through the website, landlords who are willing to help refugees are able to post housing listings aimed for refugees, with in-depth specifications. The functionalities of this web application are essentially that of a housing market application, but with emphasis on providing refugees exposure to a network of supportive housing providers.

## Key Features

#### Separate Registration for Landlords and Tenants
In addition to basic user information, landlord and refugee registration has been seperated due to necessity of role specific questions which seek to improve transparency. Landlord registration includes qustions which assesss payment and credit history leniency, whereas tenants are asked to provide sponsor names. We felt it was pertinent to require these fields during registration due to the nature of our app, as a landlord's tolerance of missing credit history can often be a deal breaker during negotiations.

#### Profiles for Landlords and Tenants
Users can access their own profile and the profiles of other users. Landlord profiles display basic user information, role specific information, and displays all the landlord's listings if present. Refugee profiles follow a similar structure. User's can also edit their own profile, which is auto-filled with their current information.

#### Add/Update Listings
A feature which is only accessible to users that have the landlord role. Landlord's can add new rental postings. Once added, the listing is viewable by all users on the listings index. Only the landlord who created the post can edit the details of the rental posting.

#### Listings Index
Displays a preview of the nine most recently posted rental listings. Users can choose to click on any of the previews and be taken to a more detailed breakdown of the rental posting, where they can also leave a review, or visit the profile of the listing's author. The listings index page is paginated, and sorted by most to least recent by default.

#### Wish List
Tenants can add their favorite listings to their wish list, or remove a listing from the wish list.  Also if a listing is in the wish list, it will be marked in the list on the main page.

#### Add Listing Reviews
The tenant can write a review about this listing and post it on the page of this listing. Tenants can delete their own reviews at any time. Review include star ratings, comments, and photos (optional).

#### Search tab
Landlords signup to post property listings with pictures and basic information like location, number of rooms, etc.
Tenants can sign up to view housing, search through them by location, number of bedrooms, number of bathrooms, building type, landlord's name, reviews and other options.
The search options come from all existing listing.

## Instructions
 * Clear instructions for how to use the application from the end-user's perspective
 * How do you access it? Are accounts pre-created or does a user register? Where do you start? etc.
 * Provide clear steps for using each feature described above
 * This section is critical to testing your application and must be done carefully and thoughtfully

#### Features

##### Guest users
Unauthenticated users are greeted with the same rental preview index page as authenticatd users. Users can choose to browse anonymously, and with limited access to the only the index page containing the listings, the individual listings pages, and the search page.

##### Accessing a listing's page
All users of the app (registered and unregistered) are able to view a listing's details on the listing page. To do so, click on the title of the listing that appears on the index page.

##### Searching for a listing
All users of the app (registered and unregistered) are able to searh for listings based on the filters. The search page is accessible by clicking on the "Search" link in the navigation bar. To search for listings, fill out the form fields as desired.

##### Registering an account
Users without an account can create an acccount as a landlord or a tenant. There are two types of registration links in the navigation bar, "Landlord Registration" and "Tenant Registration". Both links lead to their respective registration forms, which creates the user with the appropriate role and according to the information provided in the registration form.

Account creation will be successful if:
* The provided username does not already exist in the databse
* The provided email does not already exist in the databse
* The provided passwords match

##### Logging in
Users can log into the app by entering their details in the form found in the "Login" tab from the navigation bar.

Once authenticated, users are granted permissions to access other pages, such user profiles. Additonally, logged-in users can perform actions based on their roles (e.g. add a listing to their wish list, posting a listing).

##### Accessing profiles
All registered users of the app have a profile with the appropriate information for their user role.

To access a user's own profile, click on the "Profile" tab in the navigation bar. To access another user's profile, users can click on their username (where it appears) to be led to their profile page, or click on the "Visit Profile" link on an individual listing page to see that landlord's profile.

##### Editing user information
Authenticated users can edit their own user details by clicking on the "Profile" tab in the navigation bar, where they will be taken to a form that is pre-filled with their current details. The update and delete buttons function as implied.

##### Landlord specific: Creating a post
Users with the landlord role are able to create and publish a listing to the site by accessing the "Add Listing" tab in the navigation bar. The resulting page is a form with details to be filled out for a rental posting. Landlord are also able to upload photos of their listed property.

##### Landlord specific: Updating a post
Users with the landlord role are able to edit their existing listings by heading to the listing page and cllicking the "Update" button at the bottom of the page. The resulting page is a form identical to the one displayed when creating a post, except the form is pre-filled with the listing's existing details. Landlords are able to make changes as desired. The changes will be applied upon submitting the form.

##### Landlord specific: Deleting a post
Users with the landlord role are able to delete their existing listings by heading to the listing page and cllicking the "Delete" button at the bottom of the page. A prompt to confirm their decision to delete will appear. Upon confirming deletion, the listing will be removed from the database.

##### Tenant specific: Wish list
Users with the tenant role have a personal wish list, which they can view and edit. A user can access their wish list by clicking the "Wish List" link in the navigation bar.

Users can add listings to their wishlist by visiting the listing's details page and clicking on the "Wish List" button at the bottom of the page. Users can also remove a listing from their wish list by accessing the listing's details page and clicking the "Remove Wish" button at the bottom of the page.

##### Tenant specific: Leave a review
Users with the tenant role can leave a review on a listing by accessing the listing's details page and clicking on the "Review" button at the bottom of the page. Users are then prompted to fill out a review form, and their review will be posted to the listing upon submitting.


## Development requirements
 * If a developer were to set this up on their machine or a remote server, what are the technical requirements (e.g. OS, libraries, etc.)?
 * Briefly describe instructions for setting up and running the application (think a true README).


   #### Getting Started

   (You must have Python-3 and a package manager [pip] installed on your computer before you start)
   1. Install virtual environment in the team-project-13-techfugees-toronto folder:

      Mac/Linux: ```python3 -m venv venv```

      Windows: ```py -3 -m venv venv```

   2. Activate the virtual environment:

      Mac/Linux: ```. venv/bin/activate```

      Windows: ```venv\Scripts\activate```

   3. Install the dependencies in requirements.txt:

      ```pip install -r requirements.txt```

   4. Run the database script (Note: if `database.db` exists, delete the file before running the command below):

      ```python techfugees-app/db.py```

   5. Run the local development server:

      ```python techfugees-app/run.py```


 ## Deployment and GitHub Workflow

Describe your Git / GitHub workflow. Essentially, we want to understand how your team members shares a codebase, avoid conflicts and deploys the application.

 * Be concise, yet precise. For example, "we use pull-requests" is not a precise statement since it leaves too many open questions - Pull-requests from where to where? Who reviews the pull-requests? Who is responsible for merging them? etc.
 * If applicable, specify any naming conventions or standards you decide to adopt.
 * Describe your overall deployment process from writing code to viewing a live application
 * What deployment tool(s) are you using and how
 * Don't forget to **briefly explain why** you chose this workflow or particular aspects of it!

We used GitHub Actions to automatically run the test scripts for flask, our backend framework.
On any push or merge, the workflow is run to make sure the newly added files don't break compatibility.
Merges from branches were regularly reviewed by Andi Fan and Kim Le.
Whenever a new feature was being worked on, a new branch was created for it. After making sure it's working correctly, it gets merged back into main, our stable branch.
We used GitHub Actions for convenience, since it's already on GitHub. It also has templates for workflows and auto suggests them based on the repo’s files.

 ## Licenses

 Keep this section as brief as possible. You may read this [Github article](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/licensing-a-repository) for a start.

 * What type of license will you apply to your codebase?
 * What affect does it have on the development and use of your codebase?
 * Why did you or your partner make this choice?
