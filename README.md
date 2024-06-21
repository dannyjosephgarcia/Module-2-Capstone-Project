# Module-2-Capstone-Project
Welcome to the final capstone project for the API and Database Design module! This README file includes the written 
instructions on how to successfully complete the capstone project. For a detailed visual walkthrough, 
please watch the 'Lesson 21: Capstone Project Walkthrough' video in Module 2 of the course.

### Step 1: Create a New Virtual Environment
If you have not done so after cloning this repo, create a new virtual environment. A visual walkthrough is provided in
the Project Walkthrough video. To create a new venv, execute the following steps:
1. Navigate to the bottom right hand corner of your PyCharm IDE
2. Select the Python 3.10 Interpreter>Add New Interpreter>Add Local Interpreter
3. Select the 'Virtualenv Environment' option on the left sidebar
4. Select the 'New' option and locate your Python interpreter in your system using the drop-down (it should 
be located along the path 'C:\Python\Python310')

### Step 2: Add a new Configuration
To be able to successfully execute your code, a new configuration needs to be added. To add a new configuration, execute
the following steps:
1. Select the 'Current File' dropdown bar located in the top right corner of your screen (next to the 'Run' button)
2. Select 'Add new configuration'
3. Select the 'Python' configuration
4. In the dropdown bar under the word 'Run', select the virtual environment you created in Step 1
5. For the script tab, select the folder icon and navigate to the 'my_team.py' file located within the 'classes' folder 
of the project

### Step 3: Install all package dependencies within the requirements.txt file
In order to successfully complete this project, you'll need to import all packages contained within the 
`requirements.txt` file. To do this:
1. Select the `Terminal` icon in the lower left-hand corner of your screen
2. Ensure you are in the same working directory as the requirements.txt file (you can run `pwd` to check)
3. Execute the `pip install -r requirements.txt` command and press enter. All packages should install successfully
For further guidance, please refer to the `Lesson 21: Capston Project Walkthrough` video at the end of the 

### Step 3: Familiarize Yourself with the Code
There are 2 main objectives to this project: completing the code found in the `internal_routes.py` as well as the code
found in the `external_routes.py` files. The code in the `internal_routes.py` file queries the `sakila.actor` table in 
the MySQL Database set in Lesson 8. If you didn't install this, you'll need to open MySQL Workbench, create a new schema
called 'sakila' and run the SQL statement found in the `initialize-actor-table.sql` table

### Step 4: Follow the TODOs in the 'internal_rotes_model.py' file
There is a single TODO statement found inside this file. It should be VERY simple to implement.

### Step 5: Follow the TODOs in the 'internal_routes.py' file
In this file, you'll complete the route to return the expected results from the query to the `sakila.actor` table. 
Note that this will require you to alter both the `container.py` and `mysql_database_service.py` files.
View the project walkthrough video for hints...

### Step 6: Follow the TODOs in the 'test_internal_routes.py' file
After successfully completing the route found in `internal_routes.py`, you'll need to complete the unittests using the 
Flask app test_client() to allow them all to pass

### Step 7: Follow the TODOs in the 'external_routes.py' file
Shifting focus to the API within the `external_routes.py` file, this API actually commits a POST request to a 'dummy' 
website to retrieve a response. You're goal is to follow the logical trails of TODOs to obtain a successful 200 response

### Step 8: Follow the TODOs in the `test_external_routes.py` file
Upon completion of your API, you'll need to write tests that perform the following checks to ensure functionality
1. Raise a 500 if 
2. Return a 200 http status code for a successful execution of the API

If you have any questions, please email us at nextlevelcodingacademy@gmail.com for further assistance