
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


# Acknowledgements
This app was designed and developed in conjunction with the Full Stack Software Developer Diploma course (ecommerce) at the Code Institute. I would like to thank my mentor, Matt, the Slack community, and Code Institute for all their support.