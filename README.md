# Techfugees Rental App/Team-project-13-techfugees-toronto

> _Note:_ This document is intended to be relatively short. Be concise and precise. Assume the reader has no prior knowledge of your application and is non-technical. 

## Description 
 * Provide a high-level description of your application and it's value from an end-user's perspective
 * What is the problem you're trying to solve?
 * Is there any context required to understand **why** the application solves this problem?

A web application called Techfugees Toronto. A website made for refugees to facilitate their housing search process.
Only half the refugees who went through Toronto's shelter system have been settled into permanent housings in the last two years. And there are many more who can't find suitable housing. 
This website allows landlords to post housing listings aimed for refugees, with in depth specification of every listing, in addition to user reviews.

## Key Features
 * Described the key features in the application that the user can access
 * Provide a breakdown or detail for each feature that is most appropriate for your application
 * This section will be used to assess the value of the features built

#### Seperate Registration for Landlords and Refugees
In addition to basic user information, landlord and refugee registration has been seperated due to necessity of role specific questions which seek to improve transparency. Landlord registration includes qustions which assesss payment and credit history leniency, whereas refugees are asked to provide sponsor names. We felt it was pertinent to require these fields during registration due to the nature of our app, as a landlord's tolerance of missing credit history can often be a deal breaker during negotiations.

#### Profiles for Landlords and Refugees
Users can access their own profile and the profiles of other users. Landlord profiles display basic user information, role specific information, and displays all the landlord's listings if present. Refugee profiles follow a similar structure. User's can also edit their own profile, which is auto-filled with their current information. 

#### Add/Update Rental Listings
A feature which is only accessible to users that have the landlord role. Landlord's can add new rental postings. Once added, the listing is viewable by all users on the listings index. Only the landlord who created the post can edit the details of the rental posting.

#### Listings Index
Displays a preview of the nine most recently posted rental listings. Users can choose to click on any of the previews and be taken to a more detailed breakdown of the rental posting, where they can also leave a review, or visit the profile of the listing's author. The listings index page is paginated, and sorted by most to least recent by default.

#### Add listing reviews
The tenant can write a review about this listing and post it on the page of this listing. Tenants can delete their own reviews at any time. Review include star ratings, comments, and photos (optional).

#### Wish List
Tenants can add their favorite listings to their wish list, or remove a listing from the wish list.  Also if a listing is in the wish list, it will be marked in the list on the main page.

#### Search tab 
Landlords signup to post property listings with pictures and basic information like location, number of rooms, etc. 
Refugees can sign up to view housing, search through them by location, number of bedrooms, number of bathrooms, building type, landlord's name, reviews and other options. 
The search options come from all existing listing.

## Instructions
 * Clear instructions for how to use the application from the end-user's perspective
 * How do you access it? Are accounts pre-created or does a user register? Where do you start? etc. 
 * Provide clear steps for using each feature described above
 * This section is critical to testing your application and must be done carefully and thoughtfully

 #### General Instructions
 Unauthenticated user's are greeted with the same rental preview index page as authenticatd users. User's can choose to browse anonymously, and retain access to the listings index page, view an individual listings breakdown and use the search functionality. Users can choose to login by entering their details in the form found in the login tab from the navigation bar. Once authenticated, users are granted permissions to view other user profiles, which can be accessed by clicking on a username. 
 
 Authenticated users can also edit their own profile details, by clicking on the profile tab in the navigation bar, where they will be taken to a form that is pre-filled with their current details. The update and delete buttons function as implied. 

 Landlord Specifics:
 
 Refugee Specifics

 

 
 ## Development requirements
 * If a developer were to set this up on their machine or a remote server, what are the technical requirements (e.g. OS, libraries, etc.)?
 * Briefly describe instructions for setting up and running the application (think a true README).


 
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
