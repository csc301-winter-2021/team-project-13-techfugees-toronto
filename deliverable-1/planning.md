# Techfugees Mobile App

> _Note:_ This document is meant to evolve throughout the planning phase of your project. That is, it makes sense for you commit regularly to this file while working on the project (especially edits/additions/deletions to the _Highlights_ section). Most importantly, it is a reflection of all the planning you work you've done in the first iteration.
> **This document will serve as a master plan between your team, your partner and your TA.**

## Product Details

#### Q1: What are you planning to build?

> Short (1 - 2 min' read)

Our team is working with Techfugees Totonto to build an Android mobile app for refugees that facilitates the housing search process for refugees and establishes a better mutual understanding and support between refugees, outreach workers, and housing providers.

In Toronto, only about half of refugees who have gone through the city’s shelter system in the past two years have been settled into permanent housing. Additionally, Toronto’s shelter system is operating at nearly 100% capacity. 40% of people staying in Toronto shelters are refugees.

The existing services that assist refugees in their housing services are limited due to chronic understaffing of outreach workers in the shelter system. Additionally, refugees are often subject to discrimiation by housing providers due to xenophobia or unfair cultural or social biases, so the search for a housing unit can be extremely time-consuming and demoralizing for refugees.

The goal of this app is to give refugees exposure to a network of supportive housing providers while maintaining accessibility such as ease of access (Android dominates the mobile OS market share) and offline features, such as GPS mapping.


A mock-up of the app can be seen [here](https://www.figma.com/file/5FJnnTRoEI6RslFVcAAJXs/Techfugees-Mobile-App?node-id=0%3A1).

#### Q2: Who are your target users?

> Short (1 - 2 min' read)


#### Refugees seeking Housing

Refugees seeking asylum, including government sponsored refugees. Their main goal is to get settled into permanent housing. One of the largest housing obstacles that refugees face is landlord discrimination due to lack of credit history and first/last month payment. Due to a lack of existing services, many refugees must rely on outreach workers and their local shelter system which are often understaffed and running at full capacity.

#### Outreach Workers

Outreach workers at settlement organizations, whose primary responsibility is to act as a liaison between the refugee community and their network of friendly landlords. The settlement organizations are often understaffed and outreach workers are often overworked and face a large volume of incoming requests, making it hard to connect all the refugees they handle with stable housing.

#### Landlords

Landlords in the Greater Toronto Area. Their primary goal is to rent out their property. Their biggest obstacle is finding tenants who they want to lease to. They may deny a tenant based on not having credit history, or those who are short on first and last month rent. This is because refugees are seen as high risk tenants due to their income class. This is even more pronounced because of the housing shortage in Toronto.

#### Friendly Landlords

Landlords in the Greater Toronto Area who are recognized by outreach workers as supportive towards refugees, such as leniency in credit checks, first and last month’s payment, and non-judgmental/discriminating towards refugees. Their primary goal is to rent out their property, however they would not reject a refugee as a tenant over a non-refugee.

#### Q3: Why would your users choose your product? What are they using today to solve their problem/need?

> Short (1 - 2 min' read)

Our app aims to solve the problems that refugees face when searching for housing. Refugees do not have the luxury of widespread acceptance by landlords, making their housing search difficult and time consuming. Since our app would build a network between refugees, outreach workers and housing providers, the primary feature of our app is to provide a vetted list of rental options posted by landlords who are flexible and supportive to refugees. This helps refugees save time and effort in their search for suitable rentals. Additionally, the app would have the basic features of a rental listing app, such as searching by location, landlord, number of bedrooms, bathrooms, type of building, etc. Our Partner's mission is to support the inclusion of displaced people. And through this app, help refugees specifically in finding better housing for themselves.


#### Q4: How will you build it?

> Short (1-2 min' read max)

We will be building an Android app. Presently, Android Studio is the official recommendation for development by Android, therefore we will be using Android Studio as our IDE and Flutter as our front-end technology, with Java as the back-end technology to complete the logic and database algorithms.

As for our database, we are still exploring our options between a SQL and no-SQL database as we have no conclusive details yet on implementation. For a SQL database, SQLite is a widely used database for Android app developers. The no-SQL databases that have caught our eye for this particular project are Mongo Realm and Couchbase Mobile, both great options for Android app development, and they also include data level encryption.

We will be making and running JUnit tests to test our code, and all code will be looked over by multiple team members during code reviews as needed to ensure we don't miss any edge cases or issues. Additionally, we have Android devices that we can use to test our app first-hand once we reach that stage of development.


#### Q5: What are the user stories that make up the MVP?

- At least 5 user stories concerning the main features of the application - note that this can broken down further
- You must follow proper user story format (as taught in lecture) `As a <user of the app>, I want to <do something in the app> in order to <accomplish some goal>`
- User stories must contain acceptance criteria. Examples of user stories with different formats can be found here: https://www.justinmind.com/blog/user-story-examples/. **It is important that you provide a link to an artifact containing your user stories**.
- If you have a partner, these must be reviewed and accepted by them

- As a Refugees seeking Housing, I want to find some friendly landlords in order to find a house that is more convenient for me.
- As a Landlords, I want to find reassuring tenants in order to keep my house clean and good.
- As a Friendly Landlords, I want to find good Refugees in order to help them and keep my house clean.
- As a Refugees, I want to find a house by the number of bedrooms in order to find a house that suits my family.
- As a Refugees, I want to find a place to live by type of build in order to find a place with economic price.

#### Display Management

** Landing Page: **
As a user that just opened the app, I want to be greeted with a landing page that has registration and login links so that I can login or register if I am a new user. 
- Acceptance criteria: Given the landing page, when the user clicks on the login or register links, then they are redirected to the appropriate page.

** Index Page: **
As a registered user, I want to view the available listings and sort by cost, distance, and date added when I first open the app. Additionally, I want to be able to filter the listings by my ideal criterias,such as number of bedrooms, bathrooms, and type of building. From the index page, I should be able to access the other pages from a menu, as well as access my account/profile, and create and update rental postings if I am a landlord.
- Acceptance criteria: Given the registered user opens the app and is presented with the index page, clicking on a listing will lead them to the listing’s page with details. The listings can be filtered and sorted by user-defined criteria.

** Rental Posting Details Page: **
Refugee: As a refugee who has registered and logged into the app, I want to be able to see the details regarding the rental posting as well as information about the landlord, so that I can make a more informed decision about my place of residence.

Landlord: As a landlord who has registered and logged into the app, I want to be able to see the details of my own rental postings and have the option to modify the details or delete the posting, as well as view details on other landlords’ postings on the app.
- Acceptance Criteria: 
Given a registered and logged in app user, when the user clicks on a rental posting, the page should then display relevant information about the property, as well as details on the landlord’s criterias for tenants.

#### Member Management
** Registration: **
Landlord: As an unregistered landlord, I want to be able to create an account so that I can post my rental openings.
Refugee: As an unregistered refugee seeking housing, I want to be able to create an account so that I can have a more personalized view of housing listings. 
- Acceptance criteria (landlord): Given the unregistered landlord arrives at the registration page, when the user fills out the required form fields, including: Full name, password, and landlord specific fields (TBD, i.e. questions about friendliness to refugees), then their information should be stored. If the landlord posts confirmation that they are recognized as friendly by an outreach worker, their account should have a “friendly” badge.

- Acceptance criteria (refugee): Given the unregistered refugee arrives at the registration page, when the user fills out the required form fields, including: Full name, password, email, phone number, then their information should be stored.

** Login: **
As a refugee seeking housing, I want to be able to login in order to view the rental postings index page with personalized filters applied.

As a landlord seeking to list property, I want to be able to login in order to view the rental postings index page and post listings on the app.

- Acceptance Criteria: Given the user arrives at the login page, when the user fills out a valid username and password, then they are logged in with the user's personalized settings applied as search filters.

** Profile Update: **
As a registered and logged in app user, I want to be able to update my profile information so that my search settings are accurate.

- Acceptance Criteria: Given the user arrives at the profile page, when the user clicks on the profile update button, then their personal information is updated to match the filled in form-fields.

#### Postings Management
** Rental Posting Creation: ** 
As a landlord, I want to be able to create a rental posting, so that I can advertise my listing to potential tenants.

- Acceptance Criteria: Given a logged in user registered as a landlord viewing the rental posting creation page, when I fill out the necessary form fields (relevant information about property including: Location, pet tolerance, rent, utility fees), then the posting should be added displayed on the rental index page.

** Rental Posting Update: **
As a landlord, I want to be able to visit the posting details page that I created, and be able to edit and update the information displayed to users. 

- Acceptance Criteria: Given a landlord arrives at the details page of a posting he created, when the user clicks on the posting update button, then the posting information is updated to match the filled in form-fields.

** Rental Comments: **
As a user viewing a rental posting, I want to be able to leave a comment so other users can see important information I'd like to share about the property.

- Acceptance Criteria: Given a registered and logged in user who clicks on the comments tab of a rental posting, when the user fills out the comment form field and clicks submit, then the comment is stored and added to the rental postings list of comments.

** Rental Ratings: **
As a user viewing a rental posting, I want to be able to leave a rating for the posting, so that other users can see my opinion of the property.

- Acceptance criteria:
Given a registered and logged in user who is on the page for a rental posting,
When the user selects a rating and clicks submit, then the rating is stored and the average rating displayed for the posting is updated to include the newly added rating.

---

## Intellectual Property Confidentiality Agreement

> Note this section is **not marked** but must be completed briefly if you have a partner. If you have any questions, please contact David and Adam.
>
> **By default, you own any work that you do as part of your coursework.** However, some partners may want you to keep the project confidential after the course is complete. As part of your first deliverable, you should discuss and agree upon an option with your partner. Examples include:

1. You can share the software and the code freely with anyone with or without a license, regardless of domain, for any use.
2. You can upload the code to GitHub or other similar publicly available domains.
3. You will only share the code under an open-source license with the partner but agree to not distribute it in any way to any other entity or individual.
4. You will share the code under an open-source license and distribute it as you wish but only the partner can access the system deployed during the course.

**Briefly describe which option you have agreed to. Your partner cannot ask you to sign any legally binding agreements or documents pertaining to non-disclosure, confidentiality, IP ownership, etc.**

---

## Process Details

#### Q6: What are the roles & responsibilities on the team?

Describe the different roles on the team and the responsibilities associated with each role.

- Roles should reflect the structure of your team and be appropriate for your project. Not necessarily one role to one team member.

List each team member and:

- A description of their role(s) and responsibilities including the components they'll work on and non-software related work
- 3 technical strengths and weaknesses each (e.g. languages, frameworks, libraries, development methodologies, etc.)

** Roles **
Meeting scribe: A role which rotates week to week, the scribe will record meeting minutes and send them to the team after the meeting. 

Code Reviewer: Will participate in team code review sessions, which are planned on a as needed basis. During code reviews members will explain the intended purpose of their code for context, afterwards the other members will read over the code, noting any questions or concerns that will be discussed with the rest of the group afterwards.

Meeting Host: Will go over the meeting agenda with the client, and lead the discussion. Will defer to other team members when discussing their specific deliverables

Front-end developer: Will be assigned tasks related to design and UI/UX.

Back-end developer: Will be assigned tasks relating to the backend.

** Team Members **
Andi Fan
- Roles: Meeting scribe, Code Reviewer, Front-end, Back-end
- Strengths: Full-stack web experience (node.js, express.js, Django, bootstrap), industry experience with RDBMS, some knowledge of software security and preventing OWASP top 10 vulnerabilities.
- Weaknesses: No prior Android app development experience, no experience with flutter, limited experience with noSQL databases

#### Q7: What operational events will you have as a team?

Describe meetings (and other events) you are planning to have.

- When and where? Recurring or ad hoc? In-person or online?
- What's the purpose of each meeting?
- Other events could be coding sessions, code reviews, quick weekly sync meeting online, etc.
- You must have at least 2 meetings with your project partner (if you have one) before D1 is due. Describe them here:
  - What did you discuss during the meetings?
  - What were the outcomes of each meeting?
  - You must provide meeting minutes.
  - You must have a regular meeting schedule established by the second meeting.

We will be using Discord for organizing any meetings. Any meetings will usually be ad-hoc unless a deadline is coming up, or something that needs more than just chatting. Everything will be online only.
Each meeting will have its own purpose. But in general, we'll have meetings to ensure everyone is on the same page, if that can't be done in writing, and also to make sure everything is in working order before presenting something to our partner or the instructors’ team.
We did two meetings. One after getting assigned to our partner, and one where we reviewed D1.
In the first meeting, which took roughly one hour from 1:00pm to 2:00pm on Sunday February 7th, we agreed that our app would mainly be on android, and it would be best if it could function as much as possible offline.


#### Q8: What artifacts will you use to self-organize?

List/describe the artifacts you will produce in order to organize your team.

- Artifacts can be To-Do lists, Task boards, schedule(s), meeting minutes, etc.
- We want to understand:
  - How do you keep track of what needs to get done?
  - **How do you prioritize tasks?**
  - How do tasks get assigned to team members?
  - How do you determine the status of work from inception to completion?

#### Trello

We will be using Trello as both a To-Do list, and to keep track of ongoing tasks. Tasks will have a priority level based on deadline and how dependant other features are on the task. Appropriate deadlines for tasks will be discussed amongst team during weekly bilats. Team members can self-assign to tasks they find interesting/align with their area of expertise in order of priority. If a team member is not assigned to an ongoing task, other members can request for additional help.

Trello has the option to create multiple task boards, where we can keep track of our backlog, to-do tasks, in-progress tasks, code-review, testing, and completed tasks.

Additionally, we will be sharing this task board with our client so they have an idea of our progress.

#### Discord

Our primary platform for communication between team members will be Discord. This is where we will host our weekly-bilats, and where we can post questions/provide resources to eachother. We will create channels for general chat, session-planning, tech resources, and meeting minutes.

#### Slack

We will be using Slack to communicate with the client.

#### Q9: What are the rules regarding how your team works?

Describe your team's working culture.

**Communications:**
Our team will meet weekly through zoom call on Sundays at 12:00 noon to discuss what we are working on. We will also have ongoing text communication through discord.

We will be hosting Bi-weekly zoom call with partner Sundays at 1:00pm, to discuss what we’ve worked on and receive feedback. Additionally there will be ongoing communication through slack for quick clarification questions, and to send any relevant information prior to Sunday meetings.

**Meetings:**
Our team will prioritize communication, members should alert the team during weekly zoom calls if an action plan can’t be completed on time, and when they think they’d be able to complete it, extra members will be added to the task as needed on a voluntary basis.

Every week a different member will be responsible for meeting minutes. Members who miss meetings will be sent the document, and clarification can be provided over text through discord. If a team member misses two weeks of meetings without any communication, they will be categorized as a non-responsive team member and dealt with as such. Members will be held accountable through the final peer review at end of the course

**Conflict Resolution:**
For non-responsive team members, if the rest of the team agrees during the weekly calls, we will contact TA for further enforcement action.

When dealing with tech related indecisions, we will first ask our partner’s main tech contact from CanSettle for advice. Higher level indecisions that can't be resolved through our partners input will also be discussed during zoom calls, or over discord and will be decided by a majority vote.

In the event that a team member completes a task but fails to meet the acceptance criteria, discussion will be held during weekly zoom calls clarifying the criteria. The team member can also clarify why the acceptance criteria might not be feasible. Team members can be added to the incomplete task as needed on a voluntary basis.




---

## Highlights

Specify 3 - 5 key decisions and/or insights that came up during your meetings
and/or collaborative process.

- Short (5 min' read max)
- Decisions can be related to the product and/or the team process.
  - Mention which alternatives you were considering.
  - Present the arguments for each alternative.
  - Explain why the option you decided on makes the most sense for your team/product/users.
- Essentially, we want to understand how (and why) you ended up with your current product and process plan.
- This section is useful for important information regarding your decision making process that may not necessarily fit in other sections.

We first decided whether we want to make a mobile app or a web app. Most of our team members have experience in making web apps, therefore we tend to make a responsive website at the beginning, which can be run on a computer or on a mobile phone. However, our partner stated that this proposal may need to support offline operation, so the website may not meet this requirement. Hence, we decided to make an Android mobile app. This is also a great learning experience for our members who have not yet explored this realm of software development.

Additionally, our partner mentioned putting us in contact with the product owner and sole developer of Cansettle, another application catered to refugees in Canada. Our partner mentioned Cansettle leveraging Flutter for its front-end. Considering the advice we could receive from Cansettle’s owner, we decided to use similar technologies and chose Flutter for the front-end of our app.

During our second meeting with our partner, we consolidated our understanding of the application's unique identity. A refugee’s search for housing is an arduous process, frequently met with un-accommodating landlords that don’t respond. Our application seeks to make the process easier and less discriminatory for the refugees. Initially we had planned to allow all landlords to post rental openings, hoping to expose refugees to as many housing options as possible. Upon further discussion with our partner, we decided in an effort to save the refugee time and effort, we would only allow refugee friendly landlords to make rental postings.
