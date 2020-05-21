# Tastie!

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

Documentation - Photoshop, ...

Back-End - Django, Javascrip

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
    
#### Creating a new Django Project on Virtualenv

Create your project on Django:

    [server]$ cd $HOME/example.com
    [server]$ source $HOME/example.com/my_project/bin/activate
    (my_project) [server]$ python my_project/bin/django-admin.py startproject <projectname>
    
    import sys, os
    INTERP = "/home/<username>/local/bin/python"
    #INTERP is present twice so that the new python interpreter
    #knows the actual executable path
    if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)

    cwd = os.getcwd()
    sys.path.append(cwd)
    sys.path.append(cwd + '/djangoprojectname')  #You must add your project here

    sys.path.insert(0,cwd+'/my_project/bin')
    sys.path.insert(0,cwd+'/my_project/lib/python2.7/site-packages')

    os.environ['DJANGO_SETTINGS_MODULE'] = "djangoprojectname.settings"
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()

## Usage
The application is inteded to be used inside a default or mobile browser.

## Credits
Project done by notaguest404, Marcoafnunes and Mae1920, under the guidance of alina-trifan.

## License 
This project is a school project. You cannot modify or redistribute this code without explicit permission from the owners.
