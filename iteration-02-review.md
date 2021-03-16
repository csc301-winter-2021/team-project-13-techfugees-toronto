# YOUR PRODUCT/TEAM NAME

 > _Note:_ This document is meant to be written during (or shortly after) your review meeting, which should happen fairly close to the due date.
 >
 > _Suggestion:_ Have your review meeting a day or two before the due date. This way you will have some time to go over (and edit) this document, and all team members should have a chance to make their contribution.


## Iteration XX - Review & Retrospect

 * When: March 14, 2021, 1:00 PM - 1:30 PM
 * Where: Zoom Meeting

## Process - Reflection


#### Q1. Decisions that turned out well

List **process-related** (i.e. team organization and how you work) decisions that, in retrospect, turned out to be successful.

 ##### Switching from mobile application to web application
 * With approval from our client, we initially made this decision based on overall lack of familiarity with mobile development with time constraints taken into account. The decision allowed our group to circumvent many of the roadblocks associated with learning a new technology. We believe this resulted in a more refined prototype for deliverable 2. Additionally, having key functionality already implemented facilitated a discussion which was more end-user focused, allowing us to further polish the product with the client's business objectives in mind.

##### Following collaborative development protocols
 * We followed proper protocol for collaborative development, where every new feature was implemented in its own branch. Upon completion of a feature, we would merge it into another branch for testing purposes and resolving merge conflicts. As features are completed and tested, we merge them into the `main` branch, ensuring that `main` only contains working code. Following proper protocol helped isolate new changes and potential bugs, which made everything easier to test and fix.

##### Trello as a project management platform
 * Our use of the Trello board is a convenient and efficient way to keep track of the progess made on the product. As we continue to develop the product, we recognize a feature that would need to be implemented, which we then add as a task into the "To-Do" board on Trello. Team members are able to create tasks and claim them, or leave them unclaimed for others to claim as well, if they are currently busy with another task. Team members are able to pick and choose which features they are comfortable implementing, which also creates full transparency between members as to who is working on what as well as provides a clearer roadmap for our work. Our Trello board is linked [here](https://trello.com/invite/b/zwpPl1od/f6f6ed4cf6e12f27508b6ccb7b0f8093/techfugees-app-development).


#### Q2. Decisions that did not turn out as well as we hoped

List **process-related** (i.e. team organization and how you work) decisions that, in retrospect, were not as successful as you thought they would be.

 ##### Merging and pushing to Github
 * We forgot to update the `.gitignore` file to include unnecessary files generated from local development, such as `pycache` files and `database.db`. Some team members were unaware that those files were being pushed to the repository when they added their changes for committing, so often times we would have to manually delete the unnecessary files. We made sure to fix this issue and added the files to `.gitignore`, followed by running `git clean -fX` to remove the ignored files from the repository. Additionally, we ran into merge conflicts due to some branches not being up to date with main.

 ##### Code reviews by the entire team
 * We initially planned for all code to be reviewed by *every* team member prior to merging it to the `main` branch. This did not work out as planned, since our schedules as students made it difficult for everyone to get a chance to review a feature in a timely manner. Some features build on others, and we did not want to delay the development progress by keeping a newly implemented feature on hold. Instead, we made sure that every completed feature was reviewed by at least two other team members prior to merging.

#### Q3. Planned changes

List any **process-related** (i.e. team organization and how you work) changes you are planning to make (if there are any)

 * Ordered from most to least important.
 * Explain why you are making a change.


## Product - Review

#### Q4. How was your product demo?
 * How did you prepare your demo?

 We pre-populated our database with placeholder users and added sample listings. We ran our application on a local development server, and demoed the product through screen-sharing in the Zoom meeting with our partner.

 * What did you manage to demo to your partner?

 Key features of our app, including login/registration, profile viewing/updating, rental listing creation, listing updates, adding items to wishlist, and search functionality, with emphasis on a sperate user experience for tenants and landlords.

 * Did your partner accept the features?

 As a rental app, many key features were collectively determined and agreed upon at the time deliverable 1. These features were accepted by our partner with minor modifications requested. The wishlist functionality was an additional feature, which the client liked and accepted. In our last meeting, the client expressed that the reviews feature was not as important as the other features, however, we had that functionality completed regardless. The client reiterated their priorities in our latest meeting.

 * Were there change requests?

 The client brought our attention to langauge sensitivity and suggested we refer to refugees as tenants. The client also proposed the inclusion of an admin role, which would be used by refugee settlement organizations. The admin users would have the ability to delete users, posts, and reviews. Additionally, based on the vulnerability of some end users, the client requested that the names of tenants be obscured to unauthenticated users. Lastly, after hearing our client's feedback regarding the reviews feature, we will be reassessing our priorities and focus more on making changes that the client requested instead of polishing up the reviews feature.

 * What did you learn from the demo from either a process or product perspective?

 When the client brought up the language choice (i.e. "Tenant" instead of "Refugee"), we realized and agreed that it was much more appropriate to use the term "Tenant". We were initially focused entirely on implementing the features required for deliverable 2, but understand now that the user experience is not only affected by the app functionality but also the presentation of materials.

 We also have a better understanding of time constraints and will focus on implementing the most important features first.