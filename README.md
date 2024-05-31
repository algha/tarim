## Welcome to Tarim!

Hi! Tarim is free open source flask admin page. but it is more than admin page.  currently, it is completed only admin page. so I call it as admin page temporary.  

## one of the screenshoots
more screen shoots below.  
![ScreenShot](https://raw.github.com/algha/tarim/master/screens/toolbox.png)   

### Features:
 - admin
	 - login
	 - CRUD
	 - attaching admin role
- admin permission management
	- actions - CRUD
	- permissions - CRUD, attaching actions
	- role - CRUD, attaching permission
- content builder
	- content type - CRUD
	- fields - CRUD, attaching to the type
- Content - CRUD
	- the fields listed by  current content type. for example, tagging, media, category... 
- Category - CRUD
- Tag Management
- Media - CRUD

## About the repository
the repository include all tarim source code, docker files and sql file.

## Install and run

### with docker

Tarim is dockerized. so you should have installed Docker on your local machine.  
 clone the repository, and run:  

    docker-compose up --build
   
it will create all tarim needed.   
after successfully build, to access the system, open the link the url: [http://localhost:5000/dashboard/login](http://localhost:5000/dashboard/login)  
login information:  
email: tarim@test.com  
password: tarim  
  
to access the database,  open the link the url: [http://localhost:8000](http://localhost:8000)  
database information is written on the docker file.  


### Without docker
first of all, create a database.  
the database is provided at folder: **tarim/docker/db/sql/**  
 and use python environment.  
 reference this official tutorial: [https://flask.palletsprojects.com/en/1.1.x/installation/](https://flask.palletsprojects.com/en/1.1.x/installation/)  
 
### Some Screenshoots
| ![ScreenShot](https://raw.github.com/algha/tarim/master/screens/login.png) | ![ScreenShot](https://raw.github.com/algha/tarim/master/screens/content-type.png) |
|--|--|
| ![ScreenShot](https://raw.github.com/algha/tarim/master/screens/toolbox.png) | ![ScreenShot](https://raw.github.com/algha/tarim/master/screens/actions.png) |


  
 
