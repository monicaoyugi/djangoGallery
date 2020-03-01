## Gallery
Is a django application that allows users display their photos for others to see.

## LICENSE
[LICENSE](license)

## Requirements
Clone the the repository by running

 ```git clone https://github.com/monicaoyugi/djangoGallery.git
or download a zip file of the project from github then unzip.
```

Navigate to the project directory
## Create a virtual environment

Install Virtualenv

pip install virtual env
To create a virtual environment named virtual, run

virtualenv virtual
To activate the virtual environment we just created, run

source virtual/bin/activate

## Create a database
You'll need to create a new postgress database, Type the following command to access postgress

 $ psql
## Then run the following query to create a new database named picsgarage
create database gallery

## Install dependencies
To install the requirements from requirements.txt file,

pip install -r requirements.txt

## Create Database migrations
Making migrations on postgres using django
run 
```python3 manage.py makemigrations garage
then run the command below;

python3 manage.py migrate
```
## Run the app
To run the application on your development machine,

```python3 manage.py runserver
Running Tests
```

## To run tests
```python3 manage.py test
```

## Technologies Used
Django
Python
Html
Css
Javascript
Bootstrap
## User stories

As a user of the application I should be able to:

 - View different photos that interest me.
 - Click on a single photo  and also view the details of the photo. The photo details must appear on a modal within the      same route as the main page.
 - Search for different categories of photos. (e.g food, places)
 - Copy a link to the photo to share with my friends.
 - View photos based on the location they were taken.

## LICENSE
[LICENSE](license)


__Copyright (c) {2020} Monica Oyugi.__