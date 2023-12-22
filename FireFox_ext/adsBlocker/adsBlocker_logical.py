from bs4 import BeautifulSoup
import requests
import re

def block_ads(html):
    print(html)
    print("\n\n\n")
    #soup = BeautifulSoup(getPage.text, "html.parser")
    #for div in soup.select('.branding-wrapp'):
    #    div.decompose()
    
    #print(soup.select('.branding-wrapp'))

    #print(soup.find_all(id=re.compile("oa-360")))
    #for div in soup.find_all(id=re.compile("oa-360")):
    #    div.decompose()
    
    #print(soup.select('#oa-360-1702968155185_j8n6yg553'))
    #return soup.prettify()