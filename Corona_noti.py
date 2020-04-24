from plyer import notification
import requests
from bs4 import BeautifulSoup
import time

def notifyMe(title,message):
    notification.notify(
        title=title,
        message=message,
        app_icon="corona.ico",
        timeout=3
    )
def getData(url):
    r=requests.get(url)
    return r.text

if __name__=="__main__":
    #notifyMe("Ankit","Lets stop the spread of this virus together")
    while True:
        myHtmlData=getData('https://www.mohfw.gov.in//')
        soup = BeautifulSoup(myHtmlData, 'html.parser')
    #print(soup.prettify())
        myDataStr= ""
        for tr in soup.find_all('tbody')[9].find_all('tr'):
            myDataStr +=tr.get_text()
       # print(myDataStr)
        myDataStr=myDataStr[1:]
        itemList=myDataStr.split("\n\n")
    
        states=['West Bengal','Uttar Pradesh','Bihar','Delhi','Rajasthan','Madhya Pradesh','Haryana','Maharashtra','Gujarat','Punjab']
        for item in itemList[0:27]:
            dataList=item.split('\n')
            if dataList[1] in states:
                nTitle='Cases of Covid-19(Corona Virus)'
                nText=f"STATE {dataList[1]}\nIndian: {dataList[2]}\nForeign: {dataList[3]}\nCured: {dataList[4]}\nDeaths: {dataList[5]}"
                notifyMe(nTitle,nText)
                time.sleep(6)
                
        time.sleep(3600)
    

