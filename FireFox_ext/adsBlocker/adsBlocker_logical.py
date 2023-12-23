from bs4 import BeautifulSoup
import re
import json
import threading

adPatterns = ['ads', 'adv' 'ad_', '_ad', '-ad', 'ad-', 'adSlot', 'oa-', 'optad', 'banner', 'promo']

def block_ads_class(soup):
    elements = []
    def ads_class_threads(pattern):
        elements.extend(soup.find_all(class_=re.compile(pattern, flags=re.IGNORECASE)))
            
    threads = []
    for pattern in adPatterns:
        threads.append(threading.Thread(target=ads_class_threads, args=(pattern, )))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    return elements

def block_ads_id(soup):
    elements = []
    def ads_id_threads(pattern):
      elements.extend(soup.find_all(id=re.compile(pattern, flags=re.IGNORECASE)))
    
    threads = []
    for pattern in adPatterns:
        threads.append(threading.Thread(target=ads_id_threads, args=(pattern, )))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    return elements

def block_ads_src(soup):
    elements = []
    def ads_src_threads(pattern):
      elements.extend(soup.find_all(src=re.compile(pattern, flags=re.IGNORECASE)))

    threads = []
    for pattern in adPatterns:
        threads.append(threading.Thread(target=ads_src_threads, args=(pattern, )))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    return elements

def block_ads_href(soup):
    elements = []
    def ads_href_threads(pattern):
      elements.extend(soup.find_all(href=re.compile(pattern, flags=re.IGNORECASE)))

    threads = []
    for pattern in adPatterns:
        threads.append(threading.Thread(target=ads_href_threads, args=(pattern, )))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    return elements

def block_ads_data(soup):
    elements = []
    def ads_data_threads(pattern):
      elements.extend(soup.find_all(data=re.compile(pattern, flags=re.IGNORECASE)))

    threads = []
    for pattern in adPatterns:
        threads.append(threading.Thread(target=ads_data_threads, args=(pattern, )))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    return elements

def block_ads_tag(soup):
    elements = soup.find_all(re.compile(r'-ad-', flags=re.IGNORECASE))
    return elements

def makeJSONFromDict(html):
    dictOnloadJSON = {}
    soup = BeautifulSoup(html, "html.parser")
    dictOnloadJSON['Class'] = classLoadInDict(soup)
    dictOnloadJSON['ID'] = idLoadInDict(soup)
    dictOnloadJSON['SRC'] = srcLoadInDict(soup)
    dictOnloadJSON['Href'] = hrefLoadInDict(soup)
    dictOnloadJSON['Data'] = dataLoadInDict(soup)
    dictOnloadJSON['Tag'] = tagLoadInDict(soup)
        
    with open("findedAds.json", "w") as file:
        json.dump(dictOnloadJSON, file)

def classLoadInDict(soup):
    elements = block_ads_class(soup)
    classAdDict = {}
    for index, element in enumerate(elements):
          classAdDict[index] = element['class']
    return classAdDict

def idLoadInDict(soup):
    elements = block_ads_id(soup)
    idAdDict = {}
    for index, element in enumerate(elements):
        idAdDict[index] = element['id']
    return idAdDict

def srcLoadInDict(soup):
    elements = block_ads_src(soup)
    srcAdDict = {}
    for index, element in enumerate(elements):
        if not 'uploads' in element['src']:
            srcAdDict[index] = element['src']
    return srcAdDict

def hrefLoadInDict(soup):
    elements = block_ads_href(soup)
    hrefAdDict = {}
    for index, element in enumerate(elements):
        hrefAdDict[index] = element['href']
    return hrefAdDict

def dataLoadInDict(soup):
    elements = block_ads_data(soup)
    dataAdDict = {}
    for index, element in enumerate(elements):
        dataAdDict[index] = element['data']
    return dataAdDict

def tagLoadInDict(soup):
    elements = block_ads_tag(soup)
    tagAdDict = {}
    for index, element in enumerate(elements):
        tagAdDict[index] = element.name
    return tagAdDict