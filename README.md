# LAB - Class 28

## Project: Django Snacks Crud

### Author: Harper Foley

### Links and Resources

* [Django](https://www.djangoproject.com/)

#### Setup

* Clone repo to your local machine
  * `git clone gh repo clone hfoley2013/django-models`
* Install a virtual environment in you project folder
  * `python -m venv .venv`
  * NOTE: Replace `python` with the specific version of python you wish to run (e.g. `python3.11`)
* Install `requirements.txt` file
  * `pip install -r requirements.txt`
* The project is now ready to run

#### How to initialize/run your application (where applicable)

* To start the server, run the command `python manage.py runserver`
* This will launch the application in your `localhost:8000`
* You can now explore the snacks on the page

#### Tests

* Tests are conducted with Django's built-in test suite
* Tests include the following:
  1. Correct template used for `Home` page
  2. Correct template used for `Snacks List` page
  3. Status code `200` for home page
