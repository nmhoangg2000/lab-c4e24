from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict
#1 download trang
url = "https://dantri.com.vn"
#1.1 open a connection to server
conn = urlopen(url)
#1.2 read data
raw_data = conn.read()
#1.3 decode data
page_content = raw_data.decode("utf8")

# print(page_content)

# f= open("dantri.html","wb")
# f.write(raw_data)
# f.close()


#2 extract ROI
soup = BeautifulSoup(page_content, "html.parser")

ul = soup.find("ul", "ul1 ulnew") #id="ul1 ulnew"
#3 extract data
li_list = ul.find_all("li")

# for li in li_list:
#     print(li.prettify())

news_list = []
for li in li_list:
    a=li.h4.a
    title = a.string
    link = url + a["href"]
    print(title)
    print(link)
    news = OrderedDict({
        "Title":title,
        "Link": link
    })
    news_list.append(news)
print(news_list)    
#4 save data to excel

pyexcel.save_as(records= news_list, dest_file_name ="newlist.xlsx" )

