# CH4-CRM
## Customer Relationship Management System (CRM)   
This project was created as a result of the necessity to have a client database. It is used to manage and keep record of customer information, add new customers, update customer's history if changes are made and finally to delete inactive customer records. In other words, it is a CRUD application.

## Motivations
Having been an English teacher for more than 10 years, it was time for me to change my traditional way of keeping record of my students. So, I came up with a CRUD application adapted from John Elder's django CRM tutorial on Youtube. Apart from recently finishing from a python and django full stack developer bootcamp, it was time for me to start practicing my skills in a guided manner. So I thought reinventing the wheel of a project-based tutorial might be a good start.  

## Lessons Learned
This project being my first github project was an eye opener for me. I have been able to learn the following:      

- How to set up a project in django framework.
- How to structure a CRUD application
- How to set up mySQL workbench.
- Django user authentication
- Django form validation
- Django tags
- Connecting to mySQL using python
- mySQL configuration
- Bootstrap table

Some of the challenges I faced creating this application was getting stuck so many times. I had to find my way out by googling up information, using stack overflow and django documentation.     

## Installation
1 . Clone the repository
```bash
  git clone https://github.com/<username>/<forked-repo>.git
```
2 . Create your own virtual environment
```bash
  python3 -m venv venv
source venv/bin/activate
```
3 . Install your requirements
```bash
  pip install -r requirements.txt
```
4 . Create a new mySQL database
```bash
  CREATE DATABASE databasename
$ \connect databasename
```
5 . Generate a new secret key 

6 . Rename the Project

7 . Make your migrations. 

The only migrations that should appear in each of your app’s migrations folders are called ‘init.py’. As we have started a new database, we can delete any existing migrations and migrate from scratch.
```bash
   python manage.py makemigrations
$ python manage.py migrate
```
8 . Create a new superuser
```bash
 python manage.py createsuperuser 
 ```
9 . Start the development server and ensure everything is running without errors.
```bash
 python manage.py runserver
 ```
## Features
Login Users

Logout Users

Register Users

Delete Record

View Records

Add New Records

Update Records

## Tech Stack
Client: HTML, Bootstrap

Server: Python, Django

Database: mySQL
