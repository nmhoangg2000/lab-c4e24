from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict
from youtube_dl import YoutubeDL
# part1
url = "https://www.apple.com/itunes/charts/songs"

conn = urlopen(url)

raw_data = conn.read()

page_content = raw_data.decode("utf8")

soup = BeautifulSoup(page_content, "html.parser")

section = soup.find("section", "section chart-grid")
div = section.find("div", "section-content")
ul = div.find("ul")
li_list = ul.find_all("li")
new_list=[]
for li in li_list:
    a= li.h3.a
    b= li.h4.a
    song = a.string
    chapteur = b.string
    song = OrderedDict ({
        "Song":song,
        "composer":chapteur 
    })
    new_list.append(song)
pyexcel.save_as(records= new_list , dest_file_name="itunes.xlsx")

#part2
c = new_list[1]
options = {
    'default_search': 'ytsearch', 
    'max_downloads': 1
}
dl = YoutubeDL(options)
dl.download(c)