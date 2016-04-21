# Uber Challenge Test

Doing uber code challenge (SF Film Locations) to learn basic technique for internship

# Setup Environment
All of the following tutorials are designed for Mac OS, for other platform, please refer to official documents for guidance. 

Assuming you already have python(3.5), pip and homebrew installed on your computer. If any of the following commands fail to run, add sudo at the very beginning and try again. If it still doesn't work, please refer to official documentations.

1. Install Django

  Inside your terminal do
  ```
  pip install django
  ```
  
2. Install MongoDB

  Inside your terminal do
  ```
  brew update
  brew install mongodb
  ```

3. Install dependencies

  You will need three python packages: PyMongo, MongoEngine and Requests, do it by command
  ```
  pip install pymongo
  pip install requests
  pip install mongoengine
  ```
4. Get source code

  Navigate to your desire directory in your terminal and do 
  ```
  git clone https://github.com/zwang180/uber_challenge_test.git
  ```
  Then make sure you have the latest version by
  ```
  git fetch
  git pull
  ```
5. Start the server and the database

  First start the database server, in terminal(assume the path of the source code, i.e. the directory containing manage.py is /some/path/to/source/), do
  ```
  mongod --dbpath /some/path/to/source/film/data/
  ```
  Next, if this is the first time you run the code, dump the data to your local database by running loadData.py
  ```
  python loadData.py
  ```
  Please make sure your MongoDB server is running while you run the above command
  
  Finally, run Django server in another terminal window/tab
  ```
  python manage.py runserver
  ```
  Then the website is ready to view at http://localhost:8000/film/ (by default)

# Other issues
  The FastSetup_Uber.scpt is an AppleScript that could start both servers in two seperate terminal tabs and also dump data in the third tab in order to give you a free tab to do git commands. There is also an App version of the script. So if you are using Mac OS(Scirpt was written in El Captain), you could modify the file path in the script and make use of it.
  
# To Do Next

1. Major Change
 
  1.1 Currently, because the Django does not offer direct fully support to MongoDB, the data is preload into the database by running loadData.py and thus no Django model is created inside models.py. The next step is to switch to customized Django models by finishing the new python script loadDataToModels.py.

  1.2 More cool features such as google map API.
2. Minor and Performance Change
  
  ~~2.1 Create a new serperate index page that have a search bar and a link to the full list.~~
  
  2.2 Add static files(especially CSS and Javascript) to beautify the website. !IMPORTANT!

  2.3 Implement more general search function(ignore space, case insensitive, search by other field) by regex and other tools.

  2.4 Deploy the website on AWS.
  
