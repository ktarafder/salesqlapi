## How to Run

1. After cloning repo, run this command in console: pip install -r requirements.txt
2. Create a .env file (the file is literally called .env)
3. Get the API Key from the SalesQL dashboard. On the left siderbar, at the bottom there's a tab called Enrichment. Clicking on this should allow you to copy paste the API Key.
4. Once you have the key copied, create a varible within the .env file called API_KEY and set it equal to the key e.g. API_KEY = key
5. You can now run the program. Do [ python3 frontend.py ] in the console (make sure you're in the right directory) or run from VSCode

## Information

SalesQL utilizes a REST API which enocdes the response bodies in JSON. SalesQL has two different type API endpoints: Person API and Organization API
This program utilizes these APIs to allow us to programtically search for prospects. 

Issues: 
 - This API is quite janky, especially the person search. Right now, it doesn't work great and will often not find the person. 
   - If a person is actively working two jobs you must provide the organization they started working for most recently
 - Companies may have their organization name spelled slightly differently on LinkedIn, so organization name can be right but it has to match what it says on LinkedIn
 - If two organizations with the same name exist, I'm pretty sure it gets the one with the most members by default and doesn't show the other company
 - Cannot search people based off role or keywords within an organization

## Design

Backend:
 - Create one file that contains all the logic (api calls) to be made for application
   - One function to handle all searches regarding organization: either by org name or org domain
   - One function to handle search of person using full name and organization 

Frontend:
 - Develop a console based application that allows user to type in numbered options to navigate 
 TODO:
 - Translate this frontend menu logic into an UI using tkinter