# Uber Challenge Test

Doing uber code challenge (SF Film Locations) to learn basic technique for internship

# Setup Environment
Assuming you already have python(3.5), pip and homebrew installed on your computer. If any of the following commands fail to run, add sudo at the very beginning and try again. If it still doesn't work, please refer to official documentations.

1. Install Django

  inside your terminal do
  ```
  pip install django
  ```
  
2. Install MongoDB

  inside your terminal do
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

  First start the database in terminal(assume the path of the source code, i.e. the directory containing manage.py is /some/path/to/source/)
  ```
  mongod --dbpath /some/path/to/source/film/data/
  ```
  Next, if this is the first time you run the code, dump the data to your local database
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
  The FastSetup_Uber.scpt is a AppleScript that could start both server in two seperate terminal tabs and also dump data in the third tab in order to give you a free tab to do git commands. There is also a App version of the script. So if you are using Mac OS(Scirpt is written in El Captain), you could modify the path in the script and make use of it.
  
