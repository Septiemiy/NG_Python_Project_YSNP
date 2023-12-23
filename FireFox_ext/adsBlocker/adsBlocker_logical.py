from bs4 import BeautifulSoup
import re
import json

def block_ads_class(soup):
    elements = soup.find_all(class_=re.compile(r'ads', flags=re.IGNORECASE))
    return elements

def block_ads_id(soup):
    elements = soup.find_all(id=re.compile(r'ads', flags=re.IGNORECASE))
    return elements

def block_ads_src(soup):
    elements = soup.find_all(src=re.compile(r'ads', flags=re.IGNORECASE))
    return elements

def block_ads_href(soup):
    elements = soup.find_all(href=re.compile(r'ads', flags=re.IGNORECASE))
    return elements

def block_ads_data(soup):
    elements = soup.find_all(data=re.compile(r'banner', flags=re.IGNORECASE))
    return elements

async def makeJSONFromDict(html):
    dictOnloadJSON = {}
    soup = BeautifulSoup(html, "html.parser")
    dictOnloadJSON['Class'] = await classLoadInDict(soup)
    dictOnloadJSON['ID'] = await idLoadInDict(soup)
    dictOnloadJSON['SRC'] = await srcLoadInDict(soup)
    dictOnloadJSON['Href'] = await hrefLoadInDict(soup)
    dictOnloadJSON['Data'] = await dataLoadInDict(soup)
        
    with open("findedAds.json", "w") as file:
        json.dump(dictOnloadJSON, file)

async def classLoadInDict(soup):
    elements = block_ads_class(soup)
    classAdDict = {}
    for index, element in enumerate(elements):
        classAdDict[index] = element['class']
    return classAdDict

async def idLoadInDict(soup):
    elements = block_ads_id(soup)
    idAdDict = {}
    for index, element in enumerate(elements):
        idAdDict[index] = element['id']
    return idAdDict

async def srcLoadInDict(soup):
    elements = block_ads_src(soup)
    srcAdDict = {}
    for index, element in enumerate(elements):
        srcAdDict[index] = element['src']
    return srcAdDict

async def hrefLoadInDict(soup):
    elements = block_ads_href(soup)
    hrefAdDict = {}
    for index, element in enumerate(elements):
        hrefAdDict[index] = element['href']
    return hrefAdDict

async def dataLoadInDict(soup):
    elements = block_ads_data(soup)
    dataAdDict = {}
    for index, element in enumerate(elements):
        dataAdDict[index] = element['data']
    return dataAdDict