cat > toWechat.py << EOF
# encoding=utf8
#!/usr/bin/python
#pip install beautifulsoup4 requests

import requests
from bs4 import BeautifulSoup
import time

pushurl='https://zhuye.heliohost.org/work.php?msg='
headers = {'user-agent': 'Mozilla/5.0 (Android 9; Mobile; rv:68.0) Gecko/68.0 Firefox/68.0'}
s = requests.session()

def getposturl():
  url = 'https://www.hostloc.com/forum.php?mod=forumdisplay&fid=45&filter=author&orderby=dateline'
  r = s.get(url, headers=headers)
  soup = BeautifulSoup(r.text,'html.parser')
  pid = r.text[r.text.find('tid')+4:r.text.find('tid')+10]
  post_url = "https://www.hostloc.com/thread-{}-1-1.html".format(pid)
  return post_url

def getnewpost():
  r = s.get(posturl, headers=headers)
  soup = BeautifulSoup(r.text,'html.parser')
  title = soup.find(attrs={"name":"keywords"})['content']
  content = soup.find('div',class_='message').text.strip()
  return title,content

posturl = getposturl()

while posturl != getposturl():
  posturl = getposturl()
  firstArr = getnewpost()
  title = firstArr[0]
  content = firstArr[1]
  finalUrl = pushurl + '&title=' + title + '&msg=' + content + '&url=' + posturl
  s.get(finalUrl)
  time.sleep(30)
