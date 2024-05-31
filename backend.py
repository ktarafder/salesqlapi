import requests
import os
from dotenv import load_dotenv

org_search_url = "https://api-public.salesql.com/v1/organizations/enrich"
person_search_url = "https://api-public.salesql.com/v1/persons/enrich"

load_dotenv('.env')
API_KEY = os.environ.get('API_KEY')

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {API_KEY}",
}

def getLinkedinOrg(org, option):
    if option == '1':
        url_with_org = f"{org_search_url}?organization_name={org}"
    elif option == '2':
        url_with_org = f"{org_search_url}?organization_domain={org}"   
    response = requests.get(url_with_org, headers=headers)

    if response.status_code == 200:
        data = response.json()
        name = data.get('name', 'N/A')
        linkedin_url = data.get('linkedin_url', 'N/A')
        location = data.get('location', 'N/A')
        number_of_employees = data.get('number_of_employees', 'N/A')
        website = data.get('website', 'N/A')

        res = f"Name: {name}\nURL: {linkedin_url}\nLocation: {location}\nEmployee Count: {number_of_employees}\nWebsite: {website}"
        return res

    return f"Error: {response.status_code} - {response.json()['detail']}"

def getLinkedinProfile(person, org):
    url_with_person = f"{person_search_url}?full_name={person}&organization_name={org}"
    response = requests.get(url_with_person, headers=headers)

    if response.status_code == 200:
        data = response.json()
        linkedin = data.get('linkedin_url', 'N/A')
        email = data.get('emails', 'N/A')
        number = data.get('phones', 'N/A')
        return f"Linkedin: {linkedin}\nEmail: {email}\nPhone: {number}"

    return f"Error: {response.status_code} - {response.json()['detail']}"



