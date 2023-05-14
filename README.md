# Rap Blog

![Alt text])

[Live Web Application Link](https://rapblog.herokuapp.com/)

## Introduction

Welcome to my very own [Rap Blog](https://rapblog.herokuapp.com/).
I want to create a fun and responsive webiste about a genre of music i am a big fan of.
A web page where fans of rap music can share their own posts and have ufn doing it 


### Features

<details>
<summary>Favicon</summary>

- The icon on the Browser tab next to the website name.
- There to help the user navigate easier through the browser tab.

![Alt text](static/media/favicon.ico)

</details>

<details>
<summary>Main Page</summary>

![Alt text](static/images/front%20page.PNG)

</details>

<details>
<summary>Navigation Bar</summary>

![Alt text](static/images/navbar.PNG)

</details>

<details>
<summary>Footer</summary>

![Alt text](static/images/footer.PNG)

</details>

<details>
<summary>Login Form</summary>

![Alt text](static/images/login.PNG)

</details>

<details>
<summary>Logout Form</summary>

![Alt text](static/images/logout.PNG)

</details>

<details>
<summary>Register Frrm</summary>

![Alt text](static/images/register.PNG)

</details>

<details>
<summary>Add a post </summary>


![Alt text](static/images/add%20post.PNG)



</details>

<details>
<summary>My posts/Add Post</summary>

![Alt text](static/images/logged%20in%20navbar.PNG)


![Alt text](static/images/post.PNG)


![Alt text](static/images/my%20posts.PNG)



</details>

<details>
<summary> Update/Delete Form</summary>

![Alt text](static/images/delete%20post.PNG)


![Alt text](static/images/update%20post.PNG)
</details>



<details>
<summary> Like/Comment a Post</summary>

![Alt text](static/images/add%20comment.PNG)


![Alt text](static/images/likes.PNG)

</details>


<details>
<summary> Responsiveness</summary>


![Alt text](static/images/responsive%20comment%20section%20%2B%20form.PNG)


![Alt text](static/images/responsive%20main%20page.PNG)


![Alt text](static/images/responsive%20post.PNG)


</details>



## Technologies used

- HTML (Templates)
- CSS (Style sheet)
- Python + Django (Programming language + Framework)
- Git (Version Control)
- Github (Respository)
- CodeAnywhere(Cloud IDE)
- Heroku (Live Application Host)

### Future Features

- Display a message when user Logs in or Logs out of the web page.
- Create a Conatct Us page.
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
</table>
<ol>

## Browser Compatibility

The website works on different browsers: <strong>Chrome, Firefox and Edge.</strong>

### Responsiveness

- Responsiveness was tested using: Chrome Dev Tools.

- Mobile Devices.

## User Stories

All User Stories were successfully performed.
Each respective User Story was seperated in a milestone making for a more organised project and helping keeping track of tasks and functions planned to be implemented.
You can access them [here](https://github.com/andreasarreqi/blog/milestones)
</details>

## Validator Testing

<details>
<summary>HTML</summary>
HTML validator.

![Alt text](static/images/add%20post%20html%20validator.PNG)

![Alt text](static/images/update%20post%20html%20validator%20testing.PNG)


![Alt text](static/images/shared%20posts%20html%20validator.PNG)


![Alt text](static/images/register%20html%20validator.PNG)


![Alt text](static/images/login%20form%)

![Alt text](static/images/index%20html%20validator.PNG)


![Alt text](static/images/forms%20validator%20pep8.PNG)


![Alt text](static/images/delete%20post%20html%20validator.PNG)


![Alt text](README.md)

</details>

<details>
<summary>CSS</summary>
CSS validator.

![Alt text](static/images/css%20validator.PNG)

</details>

<details>
<summary>Python Validator</summary>
PEP8 validator.

- Models
- 
![Alt text](static/images/models%20pep8.PNG)

- Views
- 
![Alt text](static/images/views%20pep8%20validator.PNG)

</details>

<details>
<summary>Lighthouse</summary>
Lighthouse.

![Alt text](static/images/lighthouse.PNG)

</details>

<details>
<summary>WAVE</summary>
WAVE validator.

![Alt text]/static/images/wave.PNG)

</details>

### Unfixed Bugs / Other

- A few errors accur in the HTML validator but the web application works fine. The errors maybe appear due to use of Django elemetts in the HTML templates.

## Deployment

- The site was deployed to Heroku. The steps to deploy are as follows:
  - In the Heroku profile, create a new project, name must be unique, location set to Europe
  - 
  - From the the project you have just created you can go to the setting page.
  - Once in the settings page, Add the right Config Variables to the project. SECRET KEY DATABASE URL ets.
  - Then from there you go to the Deploy page and link your GitHub repo to the project u intented to deploy.
  - Then you can scroll at the end of the page and click on the Deploy Branch
  - After Heroku starts compiling the files and creating your app , after 1 minute or so you'll have your delpyed app link.
  - The deployed app can be found [here](https://rapblog.herokuapp.com/)

## Credits

- [Code Institute]()
- [Font Awesome.](https://fontawesome.com/)

![Alt text]()

- [Bootstrap](https://bootstrap.com)
- Bootstrap was user to create a responsive desing on all platforms.


- [Pexels](https://pexels.com)
- Images were taken from Pexels.



## Acknowledgements

- I would like to thank my mentor Daisy for guiding me.
