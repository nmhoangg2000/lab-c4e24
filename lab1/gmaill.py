from gmail import GMail, Message

sickness_list= ["thương hàn", "kiết lị","đau bung",]

#1 select a sickness randomly
from random import randint
a = randint(0, len(sickness_list)-1)
sickness = sickness_list[a]


html_template= '''
<p>ch&agrave;o sếp Long</p>
<p>y&ecirc;u h&agrave; đi</p>
<p>&nbsp;</p>
<p>S&aacute;ng nay thức dậy, em thấy m&igrave;nh bị {{sickness}}&nbsp;<img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-cool.gif" alt="cool" /></p>
'''

#2 sickness + html_template => html_content
#Hint: google: string replace
html_content = html_template.replace("sickness",sickness)



gmail = GMail("nmhoangxxi2000@gmail.com","minhhoang123")
msg = Message("dăm ba", to="c4e.techkidsvn@gmail.com",html=html_content)
gmail.send(msg)