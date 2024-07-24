


## Future Implementations
 I would like to add more functionality to this app to allow users to set a deadline for tasks, arrange tasks in order of importance, and share tasks and collaborate with other users.

# Deployment & Local Development
## Deployment
The app was deployed to Heroku via the following steps:
1. Log in (or sign up) to Heroku
2. Click New on the top right
3. Choose create new app
4.  Choose name and region and click create app
5.  In the settings tab, click on Reveal Config Vars and add the key DISABLE_COLLECTSTATIC and the value 1
6. Add another key of DATABASE_URL and set the value as the url for the database
7. Add another key of SECRET_KEY and set the value as a secret key of your choice
8.   In the deploy tab, choose GitHub as deployment method and connect repository
9. In Manual deploy section, click Deploy Branch

## Local Development
### How to Fork
To fork the To-Do List repository:
1. Log in (or sign up) to Github
2. Go to the repository for this project
3. Click the Fork button in the top right corner

### How to Clone
To clone the To-Do List repository:
1. Log in (or sign up) to Github
2. Go to the repository for this project
3. Click on the code button, select whether you would like to clone with HTTPS, SSH or GitHub CLI
4. Copy the link shown
5. Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory
6. Type 'git clone' into the terminal 
7.  Paste the link you copied in step 3
8. Press enter

# Bugs
### Known Bugs
If a user knows the task id of another user's task, they are able to view and edit the task by changing the URL.

# Credits
* Django was learned from [Django Documentation](https://docs.djangoproject.com/en/5.0/)
* User authentication was learned from [Youtube](https://youtu.be/CTrVDi3tt8o?si=lLjQ6_be5Kg-AFyg)
* Fonts were sourced from [Google Fonts](https://fonts.google.com/)

# Acknowledgements
This app was designed and developed in conjunction with the Full Stack Software Developer Diploma course (ecommerce) at the Code Institute. I would like to thank my mentor, Matt, the Slack community, and Code Institute for all their support.