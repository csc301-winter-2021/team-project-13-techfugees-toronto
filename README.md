# Techfugees Toronto Housing App

## Description
Our team is working with Techfugees Toronto to build a web application that facilitates the housing search process for refugees and establishes a better mutual understanding and support between refugees, outreach workers, and housing providers.

In Toronto, only about half of refugees who have gone through the city’s shelter system in the past two years have been settled into permanent housing. Additionally, Toronto’s shelter system is operating at nearly 100% capacity. 40% of people staying in Toronto shelters are refugees. Additionally, settlement organizations that assist refugees in finding housing are understaffed and their employees are overworked.

This web application aims to solve the problems that refugees face when searching for housing. Through the website, landlords who are willing to help refugees are able to post housing listings aimed for refugees, with in-depth specifications. The functionalities of this web application are essentially that of a housing market application, but with emphasis on providing refugees exposure to a network of supportive housing providers.

## Key Features

#### Separate Registration for Landlords and Tenants
In addition to basic user information, landlord and tenant registration has been seperated due to the necessity of role-specific questions that seek to improve transparency. Landlord registration includes qustions which assesss payment and credit leniency, whereas tenants are asked to provide sponsor names. We felt it was pertinent to require these fields during registration due to the goal of our app - facilitating the house-seeking process for refugees.

#### Profiles for Landlords and Tenants
Users can access their own profile and the profiles of other users. Landlord profiles display basic user information, role specific information, and displays all the landlord's listings if present. Tenant profiles follow a similar structure. User's can also edit their own profile, which is auto-filled with their current information.

#### Add/Update Listings
A feature which is only accessible to users that have the landlord role. Landlord's can add new property listings. Once added, the listing is viewable by all users on the listings index. Only the landlord who created the property listing can edit its details.

#### Listings Index
Displays a preview of the nine most recently posted property listings. Users can choose to click on any of the previews and be taken to a more detailed breakdown of the listing, where they can also leave a review, or visit the profile of the listing's author. The listings index page is paginated, and sorted by most to least recent by default.

#### Wish List
Tenants can add their favorite listings to their wish list, or remove a listing from the wish list.  Also if a listing is in the wish list, it will be marked in the list on the main page.

#### Add Listing Reviews
The tenant can write a review about this listing and post it on the page of this listing. Tenants can delete their own reviews at any time. Review include star ratings, comments, and photos (optional).

#### Search tab
Landlords signup to post property listings with pictures and basic information like location, number of rooms, etc.
Tenants can sign up to view housing, search through them by location, number of bedrooms, number of bathrooms, building type, landlord's name, reviews and other options.
The search options come from all existing listing.

## Instructions

#### Features

##### Guest users
Unauthenticated users are greeted with the same listing preview index page as authenticatd users. Users can choose to browse anonymously, and with limited access to the only the index page containing the listings, the individual listings pages, and the search page.

##### Accessing a listing's page
All users of the app (registered and unregistered) are able to view a listing's details on the listing page. To do so, click on the title of the listing that appears on the index page.

##### Searching for a listing
All users of the app (registered and unregistered) are able to searh for listings based on the filters. The search page is accessible by clicking on the "Search" link in the navigation bar. To search for listings, fill out the form fields as desired.

##### Registering an account
Users without an account can create an acccount as a landlord or a tenant. There are two types of registration links in the navigation bar, "Landlord Registration" and "Tenant Registration". Both links lead to their respective registration forms, which creates the user with the appropriate role and according to the information provided in the registration form.

##### Logging in
Users can log into the app by entering their details in the form found in the "Login" tab from the navigation bar.

Once authenticated, users are granted permissions to access other pages, such user profiles. Additonally, logged-in users can perform actions based on their roles (e.g. add a listing to their wish list, posting a listing).

##### Accessing profiles
All registered users of the app have a profile with the appropriate information for their user role.

To access a user's own profile, click on the "Profile" tab in the navigation bar. To access another user's profile, users can click on their username (where it appears) to be led to their profile page, or click on the "Visit Profile" link on an individual listing page to see that landlord's profile.

##### Editing user information
Authenticated users can edit their own user details by clicking on the "Profile" tab in the navigation bar, where they will be taken to a form that is pre-filled with their current details. The update and delete buttons function as implied.

##### Landlord specific: Creating a post
Users with the landlord role are able to create and publish a listing to the site by accessing the "Add Listing" tab in the navigation bar. The resulting page is a form with details to be filled out for a property listing. Landlords are also able to upload photos of their listed property.

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

#### Getting Started

You must have Python-3 and a package manager [pip] installed on your computer before you start.

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

Since our project is already on GitHub, we decided to use GitHub Actions to automatically run the test scripts for Flask, our backend framework. Another pro-factor of using GitHub Actions is that it also has templates for workflows and auto suggests them based on the repository’s files.

On any push or merge, the workflow is run to make sure the newly added files don't break compatibility. Merges from branches and merge conflicts are regularly reviewed by Andi Fan and Kim Le. Whenever a new feature is being worked on, a new branch is created for it. After making sure it is working as intended, it gets merged back into main, our stable branch. We have specified the local project files in the `.gitignore` file.

## Licenses

We will apply the MIT license to our codebase. It is a permissive license, thus allowing a wide range of permissions for our partner with very little restrictions.
