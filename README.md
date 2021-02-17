## MIW Selenium Automation Exercise 

1 - Testing Google.com to verify that the web page loads correctly
User Story:  A Tester would like to create a test to browse to “http://www.google.com” and make sure the page is loaded correctly.
Acceptance Criteria:
●	The Test uses a browser to navigate to “http://www.google.com” 
●	Verify if the page is successfully loaded
2 – Preforming a search on Google.com 
User Story:  A Tester would like to create a test to browse to “http://www.google.com” and preform a search for “mobile integration workgroup”.
Acceptance Criteria:
●	The Test uses a browser to navigate to “http://www.google.com” 
●	Search for “mobile integration workgroup”
●	Verify the first result is a link to “www.miwtech.com” (Mobile Integration Workgroup)
3 - Testing Ritchie Bros. Auctioneers website
User Story:  A Tester would like to create a test to conduct a search on Ritchie Bros. Auctioneers website and retrieve some information from listings.
Note: You will have to create an account for Ritchie Bros. website (https://www.rbauction.com). You don't need to further verify your account for bidding once your email is verified.
Acceptance Criteria:
●	The search must be performed with your user logged in.
●	The search must be performed using the advanced search (from the drop-down beside the search bar).
●	Must perform a search with the following criteria:
o	an excavator in the Construction industry
o	that is at most 3 years old
o	and made by company CATERPILLAR
●	Must verify short form search results listing information for a particular listing
o	The Meter Reads and Details displayed in each of the search results which is displayed for search result listings (use the 3rd excavator listing for your test and print to console or logs)
o	Must verify the Add to Watchlist link in a listing's third_listing_details page works 
o	Verify by clicking the 2nd excavator listing to go to its third_listing_details page and use the Add to Watchlist link there. Do not use the Add to Watchlist button on the search results page. Remember to verify the correct listing is added to the watchlist
●	Must verify More items like this tab contains an At all upcoming auctions section and has at least one listing in it.
●	Must verify listings within the At all upcoming auctions section link back to its third_listing_details page (by click on the first listing and after the third_listing_details page loaded print out its Serial Number or VIN number)
●	Must log out of the website at the end of the test.

The collection of tests contains:
1) check_test_google_one
2) check_test_google_two
3) check_test_ritchie_one
4) check_test_ritchie_two

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

I assumed google and ritchie as two separate environments:  
Google as QA and Ritchie as UAT

 `pytest -s -v -m Google --environment=qa --browser=chrome`  
 `pytest -s -v -m Ritchie --environment=uat --browser=chrome`
 
 To run each test cases  
 
 `pytest -s -v -m GoogleFirstTest --environment=qa --browser=chrome`  
 `pytest -s -v -m GoogleSecondTest --environment=qa --browser=chrome`  
 `pytest -s -v -m RitchieFirstTest --environment=uat --browser=chrome`  
 `pytest -s -v -m RitchieSecondTest --environment=uat --browser=chrome`
 
 If you need to generate the test report as html add this argument  
`--html=htmlreport.html`

  

  








