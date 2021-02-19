# Project Structure

Here you can find a short description of main directories and it's content

pages - there are sets of method for each test step  
tests - there are sets of tests for main functionalities of website  
reports - if you run tests with Allure, tests reports will be saved in this directory  
utils - this directory contains files responsible for configuration  
config - this directory contains config file  
base - this directory contains browser driver details  
data - this folder contains the test data file if you wish to have your test data comes from .csv file

# Project Features

framework follows page object pattern  
logger has been implemented 
tests can be run on popular browsers - Chrome, headless and Firefox  
the ability to easily generate legible test reports using HTML test reports


# Getting Started

Download the project or clone repository. You need to install packages using pip according to requirements.txt file. Run the command below in terminal:

`$ pip install -r requirements.txt`

# Run Automated Tests

To run selected test you need to set pytest as default test runner in Pycharm first  
Use the below commands to run the test cases

 `pytest -s -v -m Google --environment=qa --browser=chrome`  
 `pytest -s -v -m Ritchie --environment=uat --browser=chrome`
 
 To run each test cases  
 
 `pytest -s -v -m GoogleFirstTest --environment=qa --browser=chrome`  
 `pytest -s -v -m GoogleSecondTest --environment=qa --browser=chrome`  
 `pytest -s -v -m RitchieFirstTest --environment=uat --browser=chrome`  
 `pytest -s -v -m RitchieSecondTest --environment=uat --browser=chrome`
 
 If you need to generate the test report as html add this argument  
`--html=htmlreport.html`

  

  








