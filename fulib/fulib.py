from selenium.webdriver.chrome.options import Options
from selenium import webdriver
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome('./chromedriver')
import time
import urllib

def query(q,pages=1,detail=False):
    url="https://fu-berlin.hosted.exlibrisgroup.com/primo-explore/search?tab=fub&search_scope=FUB_ALL&vid=FUB&lang=en_US&offset=0&query=any,contains,"+urllib.parse.quote_plus(q)
    driver.get(url)
    time_out=10

    elemts_=[]
    def _wait_search():
        start_time = time.time()
        while True:
            elapsed_time = time.time() - start_time
            if (elapsed_time>time_out):
                print ("timeout")
                break
            if driver.find_elements_by_class_name("list-item-primary-content") and len(driver.find_elements_by_class_name("list-item-primary-content")) > len(elemts_):
                break


    def _wait_details():
        start_time = time.time()
        while True:
            elapsed_time = time.time() - start_time
            if (elapsed_time>time_out):
                print ("timeout")
                break
            if driver.find_elements_by_xpath("//div[@class='flex']") :
                break

    for p in range(pages):
        _wait_search()
        elems=driver.find_elements_by_class_name("list-item-primary-content") #Find your country in Google. (singular)
        elemts_=[]
        for e in elems:
            x={}
            x["title"]=e.find_element_by_class_name("item-title").text
            x["author"]=e.find_elements_by_class_name("item-detail")[0].text
            x["link"]=e.find_element_by_class_name("item-title").find_elements_by_tag_name("a")[0].get_attribute("href")
            x["publisher"]=e.find_elements_by_class_name("item-detail")[1].text
            elemts_.append(x)
        next=driver.find_elements_by_xpath("//button[@class='button-confirm button-large md-button md-primoExplore-theme md-ink-ripple'][.='Load more results']")

        if (next):
            #print (next[-1].text)
            next[-1].click()




    if detail:
        for e in elemts_:
            print (e["link"])
            #driver.get(e["link"])
            _wait_details()
            for row in driver.find_elements_by_xpath("//div[@layout='row']"):
                if (len(row.find_elements_by_class_name("flex"))>1):
                    key=row.find_elements_by_class_name("flex")[0].text
                    value=row.find_elements_by_class_name("flex")[1].text
                    e[key]=value

    driver.quit()
    print (len(elemts_))
    return elemts_




