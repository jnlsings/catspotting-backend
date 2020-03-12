# Catspotting
## An App for and by Cat Lovers

## API Overview

Our API is built with a PostgreSQL database, using Django Rest Framework with Python to structure our models and data and handle our HTTP requests. JSON data was hard coded and seeded using fixtures.

### Technologies used

*new to us

- Database
   - [PostgreSQL](https://www.postgresql.org/)
   
- Functionality
   - [Django/Django Rest Framework](https://www.django-rest-framework.org/)
   - Python 3.8.1
   - Pipenv
   
- Connection between back and front ends
   - [Cors](https://github.com/adamchainz/django-cors-headers)
 
- Authentication
   - *[Simple JWT](https://github.com/SimpleJWT/django-rest-framework-simplejwt)
   
- Debugging
  - *[Django Debug Toolbar](https://github.com/jazzband/django-debug-toolbar/)
  - *[Pympler](https://pympler.readthedocs.io/en/latest/)
  
 ## Code Samples
 
 ### Post JSON Data
 <img width="541" alt="PostJSONfixturedata" src="https://user-images.githubusercontent.com/57021062/76550149-a3bd8a00-645f-11ea-8e95-2adbe5b95f4c.png">
 
 ### Models
<img width="780" alt="ModelsUpdated" src="https://user-images.githubusercontent.com/57021062/76550697-889f4a00-6460-11ea-8045-c485c666fcf3.png">

 ### Serializer Examples
<img width="639" alt="UserSerializer" src="https://user-images.githubusercontent.com/57021062/76550443-2a726700-6460-11ea-800f-5ebe208b492d.png">
<img width="827" alt="PostSerializer" src="https://user-images.githubusercontent.com/57021062/76550456-2cd4c100-6460-11ea-8454-272298b9091a.png">
<img width="660" alt="CommentSerializer" src="https://user-images.githubusercontent.com/57021062/76553020-00ba3f80-6462-11ea-85c0-1c84c8b23ad6.png">


## Workflow and Responsibilities

The Catspotting team primarily used a centralized git workflow to build the API. The initial models/views/urls were built by both of us, but because the project was so large, and JWT in particular so complicated to learn, set up and troubleshoot, we naturally fell into a rhythm of Jaimie working on the back and Jordan on the front.

## Challenges, Bugs and Fixes

### Dependencies

During the initial creation of the app, we had issues installing psycopg2-binary on Jordan's cloned copy of the app. We discovered (with lots of help from Esin) that I was running a more recent version of Python, and that the Python version listed in the pipfile was not specific enough! Updating Python on Jordan's end fixed the dependency installation issue.  Lesson learned: make sure, if you are cloning this app, that you have the correct version of Python (3.8.1 at this time).

### JWT Tutorials

Originally when I built JWT auth in Django, I followed Stuart Leitch's [Hackernoon tutorial](https://hackernoon.com/110percent-complete-jwt-authentication-with-django-and-react-2020-iejq34ta) because it was 1. the most current one I could find and 2. used Simple JWT instead of the now-unmaintained JWT.  Although I was able to get JWT working fine on the back with this tutorial (using curl to test was an absolute time-consuming nightmare however), the front end was another story. Stuart's tutorial houses the React app *inside* his Django app - which is problematic in production due to both apps running on the same server.  Not to mention, best practice dictates we separate our concerns.  So, Jordan and I decided we would keep the apps separate.


Unfortunately, the extremely few examples of separate Django/React JWT builds we could find all used either Redux, or the unmaintained version of JWT. We attempted to use Dakota Lillie's [Medium Tutorial](https://medium.com/@dakota.lillie/django-react-jwt-authentication-5015ee00ef9a) as a scaffold for JWT in React, since he had separated his apps.  Unfortunately we encountered a host of issues including 1. Dakota's Django app used the outdated JWT and that may have conflicted with our back end and 2. Dakota stored the tokens in localstorage (browser storage) which isn't really ideal.


At this point, about halfway through the project, we decided to completely refactor the back end.  Thankfully, Jennifer Meade showed us a much simpler way to structure our API. Currently we have all functionality contained inside one app and were able to get JWT to work in React as well. I wish there had been one simple tutorial for this process, as it was incredibly time consuming and inefficient to hunt all over the web for an example of a Django-React build with separate apps, using Simple JWT.

### Seeding Data

After thoroughly reading the Django docs re: seeding data with data migration vs. fixtures, and other articles about how to seed data, I couldn't find a clear answer about seeding data when the models have a User model attached as owner.  This caused a lot of problems when I tried to accomplish it using data migration. I turned to fixtures and after some trial and error (and help from the lovely Skyler Bond) I was able to seed my data that way. To my knowledge, there isn't really a good step by step tutorial for seeding data using fixtures when you have a User model attached to your other models.

### Heroku Deployment

Upon deployment, Heroku wouldn't display the app and kept returning either a request timeout or a 500: internal server error. Originally, thinking the timeout was because of a memory leak(we had one on the front for a bit), I installed Django Debug Toolbar and used Muppy to try to find the source. With no luck, we once again went to Jen for help. We ended up having to add the Heroku config vars for the DB url into settings.py (a step I overlooked from one of the tutorials) as well as migrate and seed the data in Heroku. I felt frustrated that I was unable to find one comprehensize deployment tutorial with every step that I needed. Although migrating and seeding in particular might seem like common sense, for an entry level dev deploying Django to Heroku for the first time, they may not be.  It seems there is a need for a Django-Heroku deployment tutorial with babysteps!

## Future Additions

- Social authentication
- Restructure models and their relationships in order to more easily access their related data on the front end
- Possibly consider adding a space for cat name/id in Post model to facilitate future mapping/filtering by cat 
- Image upload instead of image urls
- Testing

## Contribution Guidelines

- Fork and clone this repo
- Open your terminal and go to the directory you want to store this application and ‘git clone’ it
- Make sure you have python 3.8.1 installed
- Run `$ pipenv shell` inside the root directory of the cloned app and check your python version with python -V
- Install dependencies `$ pipenv install requirements.txt`
- Make sure you have Postgres installed
- Inside your virtual environment, run `psql -U postgres -f settings.sql` to set up the database locally
- Create a super user `python3 manage.py createsuperuser`
- Migrate and seed your database:
  ```
  python3 manage.py migrate
  python3 manage.py loaddata catspotting_backend
  ```
- `python3 manage.py runserver` to see the code in action!
- Code away, and if you wish to add a new feature to the currently existing application [submit an issue to the back-end repo](https://github.com/jnlsings/catspotting-backend/issues) detailing your changes.

## Sources

### Database Media:
[Imgur](https://imgur.com/)

### Deploying to Heroku
[Sarah Panaligan's Tutorial](https://www.spiano.dev/djangoTutorial/#deploy)
<br />
[Harman Deep Singh's Tutorial](https://medium.com/@hdsingh13/deploying-django-app-on-heroku-with-postgres-as-backend-b2f3194e8a43)
<br />
[Heroku Git Deployment Docs](https://devcenter.heroku.com/articles/git)

### JWT
[Simple JWT](https://github.com/SimpleJWT/django-rest-framework-simplejwt)
<br />
[Esin Saribudak's Travelogue](https://github.com/esin87/travelogue_backend)
<br />
[Stuart Leitch's Tutorial](https://hackernoon.com/110percent-complete-jwt-authentication-with-django-and-react-2020-iejq34ta)
<br />
[Dakota Lillie's Tutorial](https://medium.com/@dakota.lillie/django-react-jwt-authentication-5015ee00ef9a)

### Seeding Data
[Justin Sung's Django Data Seeding](https://medium.com/ppl-selaw/a-simple-example-of-django-data-seeding-784f8224bbbd)
<br />
[Jaimie Lowe's Nostaldja App](https://git.generalassemb.ly/jnlsings/nostal-dja)
<br />
[Damian Hites' Data Migration Overview](https://kite.com/blog/python/django-database-migrations-overview/)
<br />
[Django Docs](https://docs.djangoproject.com/en/3.0/howto/initial-data/)

### Troubleshooting/Debugging
[Django-Debug-Toolbar](https://github.com/jazzband/django-debug-toolbar/)
<br />
[Pympler](https://pympler.readthedocs.io/en/latest/)
<br />
[Heroku error codes](https://devcenter.heroku.com/articles/error-codes#h12-request-timeout)
<br />
[Heroku Postgres](https://devcenter.heroku.com/articles/heroku-postgresql)

## Acknowledgements

Special thanks to:
- Jennifer Meade for her much simpler example of Simple JWT in django, and all her help with deploying to Heroku
- Esin Saribudak for helping us troubleshoot JWT on the back end, especially password hashing, and for her Travelogue repo which pointed me in the right direction so many times
- Skyler Bond for his help with seeding data and deploying to Heroku
