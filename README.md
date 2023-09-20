# Handshake Career Fair Web Scraper

This python based web scraper prints out a list of important information about all the employers that are present in a Career Fair event.
This was only tested on the University of South Florida's Handshake, as well as using my own cookies, so your mileage may vary.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Beautiful Soup.

```bash
pip install beautifulsoup4
python3 main.py
```

## Usage
Firstly, you should locate your career fair event on Handshake by going to the "Events" tab.

Then when you see an event that you would like to web scrape, enter the page for that specific event.

Look for the tab called "All Employers" and click on it. 

Right now, the url should look something like: `https://usf.joinhandshake.com/career_fairs/42906/employers_list`. Copy this url because you will need it for the python script.

When you run the python script, you will be met with this prompt:
```
Example: https://usf.joinhandshake.com/career_fairs/42906/employers_list
        Paste Handshake Career Fair URL and press enter: 
```
Enter the url in the terminal and then press enter. The spreadsheet generated should be in the parent directory of the python script.