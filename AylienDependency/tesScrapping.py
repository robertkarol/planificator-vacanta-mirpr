from bs4 import BeautifulSoup

import requests

url = "https://www.tripadvisor.com/Search?singleSearchBox=true&pid=3826&redirect=&startTime=1572885936551&uiOrigin=MASTHEAD&q=gamble%20warm%20volcano&supportedSearchTypes=find_near_stand_alone_query&enableNearPage=true&returnTo=__2F__ShowTopic__2D__g1__2D__i12105__2D__k3853337__2D__Search__5F__Reviews__5F__for__5F__specific__5F__words__2D__TripAdvisor__5F__Support__2E__html&searchSessionId=7CE6DCF9F5014C8AF73421C357458BCC1572885930902ssid&social_typeahead_2018_feature=true&sid=7CE6DCF9F5014C8AF73421C357458BCC1572888283077&blockRedirect=true&ssrc=h&geo=4&queryParsed=true"

r = requests.get(url)

data = r.text

soup = BeautifulSoup(data)

for link in soup.find_all('div'):
    if ".html" in str(link):
        print(link)
        break
'''
"\/UserReview-g608876-d3265056-Volcano_Huts_Thorsmork-Hvolsvollur_South_Region.html"
"https://www.tripadvisor.com/Hotel_Review-g608876-d3265056-Reviews-Volcano_Huts_Thorsmork-Hvolsvollur_South_Region.html"
'''