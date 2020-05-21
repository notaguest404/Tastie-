![](https://i.imgur.com/QgOr6B5.png)


Tastie! is a website about Recipes &amp; Food Appreciation. The objective of the Recipe site is to help the user manage recipes in a way that will make them easy to follow.

Our Approach:

    Turn the CookBook concept into a social web application.
    Recipes will be seen as a post, that could be shared and liked.
    The application will be designed to resemble food and everything related to it.
    Tag mechanism for recipes, to ease up the search algorithm.
    Make the experience as personalized as possible.
    Focus the content of recipes.
    Implement social media mechanism, such as: profile picture, bios ...


## Architecture
Front-End - Bootstrasp, Javascript, CSS.

Documentation - Photoshop, Github, .docx Files

Back-End - Django, Javascrip

## Requirements

- Browser
- Text Editor
- Python
- Virtualenv
- Django

There's no specific hardware requirements.


## Installation
Before installing **Django**, it’s recommended to install **Virtualenv**.
Use pip3 to install Virtualenv:

    [server]$ pip3 install virtualenv
    Collecting virtualenv
      Downloading virtualenv-15.1.0-py2.py3-none-any.whl (1.8MB)
      100% |████████████████████████████████| 1.8MB 367kB/s
    Installing collected packages: virtualenv
    Successfully installed virtualenv-15.1.0


    [server]$ which virtualenv
    /home/username/opt/python-3.6.2/bin/virtualenv


Create a new isolated environment with custom Python version

    [server]$ which python3
    /home/username/opt/python-3.6.2/bin/python

    [server]$ cd ~/example.com

After creating your virtual environment, don’t forget to specify the Python version you want to use.

    [server]$ virtualenv ~/example.com/my_project -p /home/example_username/opt/python-3.6.2/bin/python3

    Running virtualenv with interpreter /home/example_username/opt/python-3.6.2/bin/python3
    Using base prefix '/home/example_username/opt/python-3.6.2'
    New python executable in /home/example_username/example.com/env/bin/python3
    Also creating executable in /home/example_username/example.com/env/bin/python
    Installing setuptools, pip, wheel...done.
    
Activate your virtual environment by typing:

    [server]$ source my_project/bin/activate
    (my_project) [server]$
 
 
#### Installing Django on Virtualenv

    sudo apt-get install python-pip python-dev
    sudo pip install -upgrade pip
    (my_project) [server]$ pip3 install Django
    (my_project) [server]$ pip3 install mysqlclient

Generate the requirements of your projects:

    pip freeze > requirements.txt
    
Create and activate your virtual environment:

    virtualenv <environment_name>
    source ./<environment_name>/bin/activate
    (<environment_name>) $
    
Move your project details to the virtualenv directory:

    pip install requirements.txt
  
#### To Finish you should...

- Clone Repository
- Extract tastie folder to your virtual enviroment

        python manage.py makemigrations
        python manage.py migrate
        python manage.py runserver

- After runserver open localhost port in browser

To see a more complete tutorial, click [here] (https://hostadvice.com/how-to/how-to-create-a-virtual-environment-for-your-django-projects-using-virtualenv/).

## Usage

The application is intended to be used inside a default or mobile browser.

## Credits
Project done by notaguest404 (Bruno Matos A035468), Marcoafnunes (Marco Nunes A035335) and Mae1920 (Ema Silva A027823), under the guidance of alina-trifan.

## License 
This project is a school project. You cannot modify or redistribute this code without explicit permission from the owners.
