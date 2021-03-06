# Project 3 Wine Database
# Table of contents
1. #### [Introduction](#introduction)
2. #### [User Stories](#userstories)
3. #### [UX](#UX)
4. #### [Features](#features)
5. #### [Technologies Used](#technology)
6. #### [Future Features to Implement](#implement)
7. #### [Testing](#testing)
8. #### [Deployment](#deployment)
9. #### [Credits](#credits)

<br>


## Introduction <a name="introduction"></a>
This project allowed a website to have four basic functions of persistent storage (CRUD). The four basic functions of CRUD are Ceate, Read, Update and Delete. <br> <br>
**Create:** Create or add new entries <br>
**Read:** Read, retrieve, search or view existing entries <br>
**Update:** Update or edit existing entries <br>
**Delete:** Delete, deactivate, or remove existing entries <br>

With CRUD function, a website is able to allow any user to contribute more information into the database. This website will showcase detail wine informations included pictures. The website can be found at this link:

Project link: [Project3 Wine Database](https://ysl-wine-database.herokuapp.com/)


![Thumbnail Image](https://github.com/YiShengLee/Project3-Wine-Database/raw/master/static/img/Website_layout.PNG)

## User Stories <a name="userstories"></a>
As a user, I had an interest in wine since young. So i want to create a website with database to allow any users who have the same interest as me to contribute to this website. Therefore, I want this website to be able to:
- Add wine information
- Display wine information
- Edit wine information
- Delete wine information [**If not valid**]
- Able to store wine pictures
- Able to learn more information about different types of wine

## UX <a name="UX"></a>
This project I started with mobile first design approach. I started creating mockups wireframe on paper for mobile only. The design of the site is fully design by myself, showcasing smooth layout and interactive for most devices. Milstones had to be set in order to finish this project Below are steps by steps of the journey that required to be achieved for this website.
1. I want to create a website to showcase about wine information
2. I link the website to a database (MongoDB)
3. I want to have a minimum display of 20 wine information
4. User are able to create the own wine information by filling in a form
5. User are able to view their created wine information
6. User are able to edit any wine information by editing the form information
7. User are able to delete any wine information
8. User are able to filter their search condition by wine type, wine cost and wine country origin
9. I want to display wine image
10. I want user to know more knowledge of different type of wine out in the world
11. I want the website to be mobile, notepad, laptop and large screen responsive
12. I want the website to look trendy, smooth and overall attractive and interactive

## Features <a name="features"></a>
The website has been designed to be display nicely on all form of devices (TV, laptop, tablet and mobile).

### Features on this website are:
- Add wine information in a nicely design form layout
- Display the wine information in smooth and interactive card format
- Edit wine information in a nicely design form layout
- Delete any wine information which is not **valid**
- Added accordion for wine description
- Filter function (Wine Type, Wine Cost & Wine Country Origin)
- Clear search function to remove all the filter
- Added modal function for delete button with conformation button
- Added counter for total number of wine information display in the website
- Clickable button to redirect to the desire page of the website

### TV and Desktop Version
- Wine information will be display in 4 data in one row
- Form layout will be 1140px

### Tablet Version
- Wine information will be display in 2 data in one row
- Form layout will be 720px

### Mobile Version
- Wine information will be display in 1 data in one row
- Form layout will be 85% of view width
- Font size will be roughly 20 - 30% smaller
- Image and icon will be reduce and display correctly

## Technologies Used <a name="technology"></a>
Below are a list of the programming languages, technologies and frameworks used for this website.
- [Heroku](https://www.heroku.com/home)
    - To deploy, manage, and scale modern apps 
- HTML5
- CSS3
- Script
- Markdown
    - Used to write the README file
- [Bootstrap 4.3.1 framework](https://getbootstrap.com/)
    - The website uses Bootstrap framework for its grid system, button styling, modal, accordion and responsive navbar 
- Javascript
    - To do a validation for form input 
- [AWS Cloud9](https://aws.amazon.com/cloud9/)
    - A cloud platform to code 
- [Google Fonts](https://fonts.google.com/)
    - Input different font styling 
- [GitHub](https://github.com/)
    - A Git repository hosting service 
- [Font Awesome](https://fontawesome.com/)
    - Create nice icon 
- [Favicon](https://www.favicon-generator.org/)
    - Generate website app icon
- Google Chrome Developer Tools

## Future Features to Implement <a name="implement"></a>
In the future, I would like to:
- Add a rating for each wine information
- A table to display which user contribute the most
- A button to add more wine categories

## Testing <a name="testing"></a>
This site is tested to be responsive on the following devices:
- iphone 6/7/8
- ipad
    - Safari
- Samsung Galaxy 8
    - Google Chrome
    - Samsung web browser
- Ubuntu 18.0
    - Google Chrome
- Window 10
    - Google Chrome
    - Firefox
    - Microsoft Edge
    - Internet Explorer 11
- Window 7
    - Google Chrome
    - Internet Explorer 11

Manual testing was conducted to ensure the user story objectives where achieved.
1. Create Wine Information
    - Ensure input first name characters **min is 2** and **max is 30** [Display message if condition is not met]
    - Ensure input last name characters **min is 2** and **max is 30** [Display message if condition is not met]
    - Ensure type of wine is being **selected** in the dropdown list [Display message if condition is not met]
    - Ensure wine country origin is being **selected** in the dropdown list [Display message if condition is not met]
    - Ensure wine label characters **max is 25** [Display message if condition is not met]
    - Ensure wine price input is **integar** and able to input **2 decimals** [Display message if condition is not met]
2. Read Wine Information
    - Ensure all the input information is being displayed correctly
    - Ensure the picture is display correctly
3. Edit & Update Wine Information
    - Same rules apply to create wine information
    - Ensure all information changed will be updated and displayed correctly
4. Delete Wine Information
    - Ensure information is being wipe clean and does not displayed
5. Icon Display
    - Ensure display the right icon and size
6. Image Display
    - Ensure display the right imgage and size
7. Button
    - Ensure all the button click to the correct link in the website

## Deployment <a name="deployment"></a>
The website was created using AWS Cloud9. Git was used for version control and pushed to a repository hosted on Github. <br>
The website is deployed using Heroku and the link is [Project3 Wine Database](https://ysl-wine-database.herokuapp.com/).

### How to deploy the code locally
If you wish to run this code locally then please follow the instructions below.
1.	Download the code from the Github repository at [https://github.com/YiShengLee/Project3-Wine-Database](https://github.com/YiShengLee/Project3-Wine-Database).
2.	Click on Clone or download then Download ZIP. This will download the code into a ZIP folder locally on your computer.
3.	Uncompress the ZIP folder.
4.	Copy all the file and load it into Visual Studio Code.
    - Download Link:[Visual Studio Code](https://code.visualstudio.com/)

## Credits <a name="credits"></a>
### Code
- [w3schools](https://www.w3schools.com/)
    - Grid Layout
    - Media Query

### Images
All images for this web site are being used under free commercial license from:
- [ShutterStock](https://www.google.com.sg/)
- [Unsplash](https://unsplash.com/)
    - [addwine](https://unsplash.com/photos/xcDrhb4mhLA)
    - [vineyard](https://unsplash.com/photos/2cRXSWyMHA8)
    - [grape](https://unsplash.com/photos/1gBUXhf0PtA)
- [Imgur](https://imgur.com/)
    - [WineType](http://i.imgur.com/VgWqHnq.png)
    - []()

### Icons
- [List Icon](https://fontawesome.com/icons/list-ul?style=solid)

- [User Icon](https://fontawesome.com/icons/user?style=solid)

- [Wine Glass](https://fontawesome.com/icons/wine-glass-alt?style=solid)

- [Flag Icon](https://fontawesome.com/icons/flag?style=solid)

- [Down Arrow](https://fontawesome.com/icons/sort-down?style=solid)

- [Shop Icon](https://fontawesome.com/icons/store-alt?style=solid)

### Fonts
- [BioRhyme](https://fonts.google.com/?query=BioRhyme)
- [DM Serif Text](https://fonts.google.com/?query=DM+Serif+Text)
- [EB Garamond](https://fonts.google.com/?query=EB+Garamond)
- [Lobster](https://fonts.google.com/?query=Lobster)
- [Permanent Marker](https://fonts.google.com/?query=Permanent+Marker)
- [Courgette](https://fonts.google.com/?query=Courgette)

### Others
- [Flash Message](https://www.tutorialspoint.com/flask/flask_message_flashing.htm)
- [Modal Bootstrap](https://getbootstrap.com/docs/4.0/components/modal/)
- [Bootstrap Validation](http://bootstrapvalidator.votintsev.ru/getting-started/)


