# CSC230-projects
CSC 230 project 

Brainstorm: https://docs.google.com/document/d/1qCk1xiKr5xYKn_v26dGEDQAfx3tw4ScFzL1ClkjgUIs/edit?usp=sharing

Software Requirements Sheet: https://github.com/GcalvinQ/CSC230-projects/blob/79f2d973c4c248d0f2eede7057799439fa60e8da/Software%20Requirements%20Template.pdf

Kan-Ban: https://trello.com/invite/b/jMTa9V4y/ATTIa5fd906fc4b99ccf1735309d801d4ffc11AB004B/kanban-makerspace


To access the website, you must first install django, a virtual environment and the files for the website.

##INSTALLING DJANGO

Open terminal/command prompt

Type pip3 install django

(If pip is not installed: type python get-pip.py for mac or py get-pip.py for windows)

Type pip3 instll python

To see if it installed correctly, type django-admin --version

##INSTALLING VIRTUAL ENVIRONMENT

Open terminal/command prompt

Type pip3 install virtualenv env

Type pip3 install virtualenvwrapper

Type source venv/bin/activate (Mac)

Type env\scripts\activate (Windows)

##CREATING AND INSTALLING THE DJANGO PROJECT

In the terminal/CMD make sure that you know what directory you are in

Type django-admin startproject inventoryproject

On github, download the repository in the form of a zip file by going to code -> download zip

Once the ZIP is downloaded, double click on the file to open it

Double click on the CSC230-projects folder

Double click on the inventory project folder

Open a new file explorer/finder window and open the inventoryproject folder in the same directory where you created the django app

Highlight the files in the CSC230-projects inventoryproject folder and copy and paste the folders to the django created inventoryproject folder

If a replace file diaglogue box appeares, click replace all

In terminal/cmd, make sure that the directory is the django inventory project folder and type python manage.py runserver

Control-Click/CMD-Click the http://127.0.0.1:8000 link

Enjoy the website!

##ACCESS ACCOUNTS

Untrained User: untrained/user1234

Admin: admin/adminuser1234

Trained Student: trained/usertrained1234

Student-Worker: worker/workeruser1234

