# harvester
The AI Harvest
## Generate migration files
`docker-compose run web python manage.py db migrate`
## Perform database migrations
`docker-compose run web python manage.py db upgrade`
## Run the test suite
`docker-compose run web python manage.py test`
## Run the API
`docker-compose run web python manage.py runserver`
