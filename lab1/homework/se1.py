from gmail import GMail, Message
import datetime

html_content = '''
<p>Ch&agrave;o sếp</p>
<p>H&ocirc;m nay em thấy trong người mmetj mỏi c&oacute; lẽ bị kiết lị, sếp cho e xon nghỉ h&ocirc;m nay nh&eacute;</p>
<p>Em cảm ơn!!&nbsp;<img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-tongue-out.gif" alt="tongue-out" /></p>
'''
gmail = GMail("nmhoangxxi2000@gmail.com","minhhoang123")
msg = Message("đơn xin nghỉ việc", to="c4e.techkidsvn@gmail.com",html=html_content)
now = datetime.datetime.now()
if now.hour >= 7:
    gmail.send(msg)
else:
    print("After 7AM")