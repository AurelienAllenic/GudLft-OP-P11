# gudlift-registration

1. Why

    This is a proof of concept (POC) project to show a light-weight version of our competition booking platform. The aim is the keep things as light as possible, and use feedback from the users to iterate.

2. Getting Started

    This project uses the following technologies:

    * Python v3.x+

    * [Flask](https://flask.palletsprojects.com/en/1.1.x/)

        Whereas Django does a lot of things for us out of the box, Flask allows us to add only what we need. 
     

    * [Virtual environment](https://virtualenv.pypa.io/en/stable/installation.html)

        This ensures you'll be able to install the correct packages without interfering with Python on your machine.

        Before you begin, please ensure you have this installed globally. 


3. Installation

    - After cloning, change into the directory and type <code>python -m venv env</code>. This will then set up a a virtual python environment within that directory.

    - Next, type <code> .env/Scripts/activate</code>. You should see that your command prompt has changed to the name of the folder. This means that you can install packages in here without affecting affecting files outside. To deactivate, type <code>deactivate</code>

    - Rather than hunting around for the packages you need, you can install in one step. Type <code>pip install -r requirements.txt</code>. This will install all the packages listed in the respective file. If you install a package, make sure others know by updating the requirements.txt file. An easy way to do this is <code>pip freeze > requirements.txt</code>

    - Flask requires that you set an environmental variable to the python file. However you do that, you'll want to set the file to be <code>server.py</code>. Check [here](https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application) for more details : execute <code>env:FLASK_APP = "server.py"</code> and <code>env:FLASK_APP</code> to check for your flask app configuration.

    - You should now be ready to test the application. In the directory, type either <code>flask run</code> or <code>python -m flask run</code>. The app should respond with an address you should be able to go to using your browser.

4. Current Setup

    The app is powered by [JSON files](https://www.tutorialspoint.com/json/json_quick_guide.htm). This is to get around having a DB until we actually need one. The main ones are:
     
    * competitions.json - list of competitions
    * clubs.json - list of clubs with relevant information. You can look here to see what email addresses the app will accept for login.

5. Testing

    I'm using pytest and flask-testing to test the app.
    Tests are divided into threee different folders inside our tests direcotry : unit_tests, functionnal_tests and performances tests.
    Two json files are here to mock the data : clubs_test.json & competitions_test.json.
    To set the app in test mode, make sure that variable is_testing  is equal to true inside server.py.
    To test a specific file go to it's location (from root it's <code>cd ./tests</code>, then for example <code>cd ./unit_tests</code>) and execute <code>pytest name_of_your_test_file.py</code> (for example here <code>pytest test_home.py</code>).
    To test the coverage of the tests in this app, just go to the root and execute <code>pytest --cov=./</code>.
    To test the perforrmances of the app, you can use locust. Just go to the location of the locust file (from root : <code>cd ./tests/performances_tests</code> and then execute <code>locust -f name_of_your_locust_file.py --host=://localhost:5000</code>)

