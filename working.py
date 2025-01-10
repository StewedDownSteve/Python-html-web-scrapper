import requests
from bs4 import BeautifulSoup
import warnings
warnings.filterwarnings("ignore", message=".*urllib3.*")



import requests
from bs4 import BeautifulSoup

# URL of the "Books to Scrape" website
url = 'http://books.toscrape.com/catalogue/category/books/classics_6/index.html'

# Send a request to the website
response = requests.get(url)

# Check if the request was successful (status code 200)
print(f"HTTP Status Code: {response.status_code}")

# If status code is 200, proceed to parse the content
if response.status_code == 200:
    # Parse the content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all books in the "Classics" category
    books = soup.find_all('li', class_='col-xs-6 col-sm-4 col-md-3')

    # Print the titles of all books in the "Classics" category
    for book in books:
        title_tag = book.find('h3')
        if title_tag:
            # Extract and print the title
            title = title_tag.find('a').get('title')
            print(title)
else:
    print("Failed to retrieve the page.")




# Look for the divs containing job cards
    # job_cards = soup.find_all('div', class_='cardOutline')
    # for card in job_cards:
        # Extract the job title
        # title_div = card.find('h2', class_='jobTitle')
        # if title_div:
        #     title = title_div.text.strip()
        #     print(f"Job Title: {title}")

     # Extract the company name
    #     company_div = card.find('span', {'data-testid': 'company-name'})
    #     if company_div:
    #         company = company_div.text.strip()
    #         print(f"Company: {company}")
    # print('-' * 40)







# Updated find_all to look for div elements with the class cardOutline.
# Extract Specific Details:
# Job titles are in an h2 element with class jobTitle.
# Company names use a span with data-testid='company-name'.
# Locations are in a div with data-testid='text-location'.



#  -----------------------------------------------
# Project Setup Notes:
# -----------------------------------------------
# 1. Install Python (using Homebrew on macOS):
#    - `brew install python`
#    - Confirm installation: `python3 --version`
#
# 2. Create a virtual environment:
#    - `python3 -m venv venv`
#    - Activate it: `source venv/bin/activate`
#
# 3. Install required libraries:
#    - `pip install requests beautifulsoup4`
#
# 4. Save dependencies (optional, but recommended):
#    - `pip freeze > requirements.txt`
#    - To reinstall dependencies: `pip install -r requirements.txt`
#
# 5. Run the script:
#    - Activate the virtual environment (if not already active).
#    - Execute: `python scraper.py`
#<div class="css-rzhvbl e37uo190">flex
# <h2 class="jobTitle css-1psdjh5 eu4oa1w0" tabindex="-1">
# <div class="css-rzhvbl e37uo190">flex