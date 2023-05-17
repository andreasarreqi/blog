# [Welcome to Rap blog](https://rapblog.herokuapp.com/)

## Introduction

Welcome to my very own [Rap Blog](https://rapblog.herokuapp.com/).
I want to create a fun and responsive webiste about a genre of music i am a big fan of.
A web page where fans of rap music can share their own posts and have ufn doing it

## AGILE Methodology

### User Stories

All User Stories were successfully performed.
Each respective User Story was seperated in a milestone making for a more organised project and helping keeping track of tasks and functions planned to be implemented. Each milestone has a collection of issues that I thought would be helful towards finishing the project and i seperated them in either Fton-Ebd or Back-end.
You can access them [here](https://github.com/andreasarreqi/blog/milestones)

All projects were assigned to epics, prioritized under the labels, Must have, should have, could have. They were assigned to piriority levels "Low Priority" "Medium Priority" "high Priority" . "Must have" stories were completed first, "should haves", "could haves" and finally "Wont have". It was done this way to ensure that all core requirements were completed first to give the project a complete feel, with the nice to have features being added should there be capacity.

The Blog User Stories board was created using github projects and can be viewed to see more information on the project cards. All stories except the documentation tasks have a set of acceptance criteria in order to define the functionality that marks that story as complete.

#### Epics

The project had 5 main Epics (milestones):

EPIC 1 - Base Setup

The base setup epic is for all stories needed for the base set up of the application. Without the base setup, the app would not be possible so it was the first epic to be delivered as all other features depend on the completion of the base setup.

1. As a Developer, I need to set up the base structures of the project.

<details>
<summary> 1. Acceptance Criteria </summary

- Django installed
- Project created
- Environment variables set up
- Settings.py file modified to hide sensitive information and use environment variables

</details>

2. As a developer, I need to create static resources so that images, css and javascript work on the website

<details>
<summary> 2. Acceptance Criteria </summary>

- Create static folder and settings
- Create sub folders for images, css , media , images

</details>

3. As a developer, I want to create the base.html page and structure so the other pages can use the layout

<details>
<summary>3. Acceptance Criteria </summary>

- Create the templates
- Create the navbar
- Create the main content
- Create the footer
</details>

4. As a developer, I need to create a responsive navbar so that users can navigate the website from any device
<details>

<summary> 4. Acceptance Criteria </summary>

- Home - Shown for all users
- Register - Shown to non logged in users only
- Login - Shown to non logged in users only
- Logout - Shown to logged in users only
- My Posts - Shown to logged in users only
- Contact Us - Shown to all users
</details
>

5. As a developer, I need to create the footer with social media links and contact information

<details>
<summary> 5. Acceptance Criteria </summary>

- Footer created
- Social media link column
- Social media links open in a new tab
- Social media links navigate to the correct pages

</details>

6. As a developer, I need to create a error code handling page

<details>
<summary> Acceptance Criteria </summary>

- Create 403.html
- Create 404.html
- Create 500.html

</details>
EPIC 2 - Admin / Account
The Admin / Account epic is for all stories needed for the Admin or account related soories. It is also related to the functions that can be achieved in the back end perspective of the website such ass database, admin panel etc.

ADMIN / ACCOUNT - USER STORIES

As a Developer, I need to create a super user to serve as the application's manager
Acceptance Criteria

<details>
<summary> 1. Acceptance Criteria</summary>

- Create an Administrator to manage the website

</details>

As a Admin, I want to create a post on the admin panel

<details>

<summary> 2. Acceptance Criteria</summary>

- Musician model created with posting functionality
- Musician Admin panel created
- Admin can create a post and publish it
- </details>

As a developer, I need to implement allauth so that users can sign up and have access to the websites features

<details>
<summary> 3. Acceptance Criteria </summary>

- Allauth installed
- Users are able to sign up and log in

</details>

As a developer, I need to style the forms to look more appealing.

<details>
<summary> 4. Acceptance Criteria </summary>

- Style the forms
- </details>

As a Admin, I want to create comment sectionf for users to comment on

<details>
<summary> 5. Acceptance Criteria </summary>

- Create Comment Model
- Create Comment view
- Create Comment form
- </details>

EPIC 3 - Blog
The Blog epic is for all stories needed for the front end of the web page. Anything from the website that relates to the front end that the user actually sees and can interact with is located in this epic.

BLOG - USER STORIES

As a User, I like to view the posts on the web page

<details>
<summary> 1. Acceptance Criteria</summary>

- User can view posts

</details>

As a User, I want the page to look consistent and neat with posts

<details>
<summary> 2. Acceptance Criteria</summary>

- Main page is paginated by 6 per page

</details>

As a User, I want to be able to see the comments on the posts

<details>
<summary> 3. Acceptance Criteria</summary>

- User can view the comments in every post

</details>

As a User, I want to be able to like and unlike a post

<details>
<summary> 4. Acceptance Criteria</summary>

- Post like vew was created
- User can view likes and Like or Unlike a post

</details>

As a User, I want to create my own blog post

<details>
<summary> 5. Acceptance Criteria</summary>

- Form was created
- View was created
- Form Template was created
- User can add post

</details>

As a User, I want to delete a post that i have created

<details>
<summary> 6. Acceptance Criteria</summary>

- User can delete a post they've created

</details>

As a User, I want to see the posts I've created

<details>
<summary> 7. Acceptance Criteria</summary>
- User can view the posts the've created or create the first one

</details>

As a User, I want to be able to edit the posts I've created

<details>
<summary> 8. Acceptance Criteria</summary>

- User can edit a post they;ve created

</details>

As a user, I would like to be able to contact the restaurant so that I can have any queries answered

<details>
<summary> 9. Acceptance Criteria</summary>

- Users can contact the page admininstrator(s)
</details>

EPIC 4 - Deployment Epic

This epic is for all stories related to deploying the app to heroku so that the site is live for users.

DEPLOYEMENT - USER STORIES

As a developed, I need to deploy the project to heroku to be accessed by everyone

<details>
<summary> Acceptance Criteria </summary>

- Website can be run not only localy

- </details>

EPIC 5 - Documentation

This epic is for all document related stories and tasks that are needed to document the software development lifecycle of the application. It aims to deliver quality documentation, explaining all stages of development and necessary information on running, deploying and using the application.

DOCUMENTATION - USER STORIES

As a developer, I want to create a README file to document every step I took creating the project

<details>
<summary> Acceptance Criteria </summary>

- Anyone can see the procces of this page's development

</details>

### Features

<details>
<summary>Favicon</summary>

- The icon on the Browser tab next to the website name.
- There to help the user navigate easier through the browser tab.

![Alt text](static/media/favicon.ico)

</details>

<details>
<summary>Main Page</summary>

- Main page contains the nav bar
- Blog Posts
- Footer

![Alt text](static/images/front%20page.PNG)

</details>

<details>
<summary>Navigation Bar</summary

The nav bar (Home , Login , Register , Cio)

![Alt text](static/images/new%20nav.PNG)

</details>

<details>
<summary>Footer</summary>

- Footer contains the Social Media links that redirect to each respective link

![Alt text](static/images/footer.PNG)

</details>

<details>

<summary>Login Form</summary>

- Login form allows users to log into the website

![Alt text](static/images/login.PNG)

</details>

<details>
<summary>Logout Form</summary>

- Logout form allows user to log out of t he website

![Alt text](static/images/logout.PNG)

</details>

<details>
<summary>Register Form</summary>

- Register form allows user to create their own account

![Alt text](static/images/register.PNG)

</details>

<details>
<summary>Contact Us</summary>

- Contact form allows user to contatt the website's administrators.

![Alt text](static/images/contact%20form.PNG)

</details>

<details>
<summary>Add a post </summary>

- Allows the user to add a post

![Alt text](static/images/add%20post.PNG)

</details>

<details>

<summary>My posts/Add Post</summary>

- Allows users to view therir posts or add first/another post

![Alt text](static/images/logged%20in%20navbar.PNG)

![Alt text](static/images/post.PNG)

![Alt text](static/images/my%20posts.PNG)

</details>

<details>

<summary> Update/Delete Form</summary>

- Allows user to update or delete the forms they created

![Alt text](static/images/delete%20post.PNG)

![Alt text](static/images/update%20post.PNG)

</details>

<details>

<summary> Like/Comment a Post</summary>

- Allows users to Like or Comment a post

![Alt text](static/images/add%20comment.PNG)

![Alt text](static/images/likes.PNG)

</details>

<details>

<summary> Responsiveness</summary>

- Responsiveness was achieved using Bootstrap classes and CSS

![Alt text](static/images/responsive%20comment%20section%20%2B%20form.PNG)

![Alt text](static/images/responsive%20main%20page.PNG)

![Alt text](static/images/responsive%20post.PNG)

</details>

<details>

<summary> Error Pages </summary>
404.html error page

500.html error page

![Alt text](static/images/500%20error.PNG)

![Alt text](static/images/404%20error.PNG)

</details>

## Technologies used

- HTML (Templates)
- CSS (Style sheet)
- Python + Django (Programming language + Framework)
- Psycopg2 - ElephantSQL(Database)
- Cooloudinary (For storing images)
- Git (Version Control)
- Github (Respository)
- CodeAnywhere(Cloud IDE)
- Heroku (Live Application Host)

## Packages Installed

Packages were installed using "pip3 install (repackage)

Packages were frozen using "pip3 freeze --local > requirements.txt" so heroku know which packages to install in the project.

asgiref==3.6.0

cloudinary==1.32.0

dj-database-url==0.5.0

Django==3.2.19

django-allauth==0.54.0

django-cloudinary-storage==0.3.0

django-crispy-forms==1.14.0

django-summernote==0.8.20.0

env==0.1.0

gunicorn==20.1.0

oauthlib==3.2.2

psycopg2==2.9.6

PyJWT==2.6.0

python3-openid==3.2.0

pytz==2023.3

requests-oauthlib==1.3.1

sqlparse==0.4.4

urllib3==1.26.15

### Future Features

- Display a message when user Logs in or Logs out of the web page.
- Create My profile. Giving the user a change to view the posts they've liked or commented
- Adding group of posts based on music genre. When a genre is clicked upon, to be able to display posts in the respective genre.
- Email verification for registering new account.

## Testing

<details>

<summary> Rap Blog - Manual Testing </summary>

## Functionality

<table>
  <tr>
   <td>
<strong>Test Label</strong>
</li>
</ol>
   </td>
   <td><strong>Test Action</strong>
   </td>
   <td colspan="2" ><strong>Expected Outcome</strong>
   </td>
   <td><strong>Test Outcome </strong>
   </td>
  </tr>
  <tr>
   <td>Site loading
   </td>
   <td>Navigate the Home Page
   </td>
   <td colspan="2" >Nav bar with login/register buttons and posts user can interact with
   </td>
   <td>PASS
   </td>
  </tr>
  <tr>
   <td>Access Individual posts
   </td>
   <td>User is met with the name of the artist, short description,Comment area and leave a comment form(if logged in)
   </td>
   <td colspan="2" >Like/unlike button works and the comment form + submit button works(if logged in)
   </td>
   <td>PASS
   </td>
  </tr>
  <tr>
   <td>Login/Register buttons
   </td>
   <td>Clicking each button respectively and trying to interact with them.
   </td>
   <td colspan="2" > The user can register/login/logout of the web page
   </td>
   <td>PASS
   </td>
  </tr>
  <tr>
   <td>My Posts Button
   </td>
   <td>Clicking the My posts button
   </td>
   <td colspan="2" >The user gets redirected to a page that they can see the posts they've created, if they haven't done so yet a button is shwwn to help them do so.
   </td>
   <td>PASS
   </td>
  </tr>
  <tr>
   <td>Add Post button
   </td>
   <td>Click the add post button
   </td>
   <td colspan="2" >A form is displayed to a user helping them with neccessery fields to create a post of their own.
   </td>
   <td>PASS
   </td>
  </tr>
  <tr>
   <td>Update/Delete a post
   </td>
   <td>AClick the buttons on the cards shwon on My Posts page
   </td>
   <td colspan="2" > The user can Update/Delete the posts they've hreated. A form is displayed on the update page that they can add material or change it. A button is displayed on the delete pageg making sure the user really wants to delete a post of their making.
   </td>
   <td>PASS
   </td>
  </tr>
  <td>Contact Form
   </td>
   <td>Fill the form and click submit
   </td>
   <td colspan="2" > The form sends data to the admin panel
   </td>
   <td>PASS
   </td>
  </tr>
</table>
<ol>

## Browser Compatibility

The website works on different browsers: <strong>Chrome, Firefox and Edge.</strong>

### Responsiveness

- Responsiveness was tested using: Chrome Dev Tools.

- Mobile Devices.

</details>

## Validator Testing

<details>
<summary>HTML</summary>
HTML validator.
All the pages that get displayed are validated.

![Alt text](static/images/add%20post%20html%20validator.PNG)

![Alt text](static/images/delete%20post%20html%20validator.PNG)

![Alt text](static/images/index%20html%20validator.PNG)

![Alt text](static/images/login%20form%20html%20validator.PNG)

![Alt text](static/images/register%20html%20validator.PNG)

![Alt text](static/images/shared%20posts%20html%20validator.PNG)

![Alt text](static/images/update%20post%20html%20validator%20testing.PNG)

![Alt text](static/images/contact%20form%20HTML%20validator.PNG)

![Alt text](static/images/500%20%20error%20HTML%20validator.PNG)

![Alt text](static/images/error%20HTML%20validator.PNG)

</details>

<details>
<summary>CSS</summary>
CSS validator.
All CSS code is validated.

![Alt text](static/images/css%20validator.PNG)

</details>

<details>
<summary>Python Validator</summary>
PEP8 validator.
All Python code is validated.

- Models

![Alt text](static/images/models%20pep8.PNG)

- Views

![Alt text](static/images/views%20pep8%20validator.PNG)

- Forms

![Alt Text](static/images/forms%20validator%20pep8.PNG)

- Contact

![Alt text](static/images/contact%20view%20PEP8.PNG)

![Alt text](static/images/contact%20PEP8%20validator.PNG)

![Alt text](static/images/contact%20admin%20PEP8.PNG)

![Alt text](static/images/contact%20form%20PEP8.PNG)

</details>
<details>
<summary>Lighthouse</summary>
Lighthouse.

![Alt text](static/images/lighthouse.PNG)

</details>

<details>
<summary>WAVE</summary>
WAVE validator.

![Alt text](static/images/wave%20validator.PNG)

</details>

### Unfixed Bugs / Other

- A few errors accur in the HTML validator but the web application works fine. The errors maybe appear due to use of Django elemetts in the HTML templates.
- Posts cannot have the same name. Only one post can have a specific name(title/artist name)

## Deployment

- The site was deployed to Heroku. The steps to deploy are as follows:

  - In the Heroku profile, create a new project, name must be unique, location set to Europe
  - From the the project you have just created you can go to the setting page.
  - Once in the settings page, Add the right Configuration Variables to the project. SECRET_KEY DATABASE_URL and CLOUDINARY_URL.
  - Then from there you go to the Deploy page and link your GitHub repo to the project u intented to deploy.
  - Then you can scroll at the end of the page and click on the Deploy Branch
  - After Heroku starts compiling the files and creating your app , after 1 minute or so you'll have your delpyed app link.
  - The deployed app can be found [here](https://rapblog.herokuapp.com/)

## Credits

- [Code Institute](https://codeinstitute.net)
- For the great lessons (I think therefore blog)

- [Favicon](https://favicon.io)
- For the browser tab icon

- [StudyGyaan](https://studygyaan.com/django/how-to-create-a-unique-slug-in-django?utm_content=cmp-true)
- For the tutorial on Slugify

- [Font Awesome.](https://fontawesome.com/)
- For the Social MEdia icons , Like, Comment buttons

- [Bootstrap](https://bootstrap.com)
- Bootstrap was user to create a responsive desing on all platforms.

- [Pexels](https://pexels.com)
- Images were taken from Pexels.

- [<OrdinaryCoders>](https://ordinarycoders.com/blog/article/django-messages-framework)
- Django alert messages when post is added/edited/deleted and when contact form is submited

- [CoduBeta](https://www.codu.co/articles/securing-django-views-from-unauthorized-access-npyb3to_)
- UserPassestestmixin was taken from here.

- [Biograpy](https://www.biography.com/musicians/tupac-shaku)
- Biography of the Artists taken from Biography.

## Acknowledgements

- I would like to thank my mentor Daisy for guiding me.
