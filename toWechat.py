# encoding=utf8
#!/usr/bin/python
import requests
from bs4 import BeautifulSoup
import time
#pip install beautifulsoup4 requests

pushurl='https://zhuye.heliohost.org/work.php?msg='
login = 'https://www.hostloc.com/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&lssubmit=yes&inajax=1'
listurl = 'https://www.hostloc.com/forum.php?mod=forumdisplay&fid=45&filter=author&orderby=dateline'

headers = {'user-agent': 'Mozilla/5.0 (Android 9; Mobile; rv:68.0) Gecko/68.0 Firefox/68.0'}
data={"username":'wmw',"password":'Mjj123456'}

s = requests.session()
request = s.post(login, data = data,headers=headers)
cookie = request.cookies

def getposturl():
  r = s.get(listurl, headers=headers)
  soup = BeautifulSoup(r.text,'html.parser')
  pid = r.text[r.text.find('tid')+4:r.text.find('tid')+10]
  posturl = "https://www.hostloc.com/thread-{}-1-1.html".format(pid)
  return posturl

def getnewpost():
  r = s.get(posturl, headers=headers, cookies=cookie)
  soup = BeautifulSoup(r.text,'html.parser')
  title = soup.find(attrs={"name":"keywords"})['content']
  content = soup.find('div',class_='message').text.strip()
  return title,content

newpost = getposturl()

while True:
  time.sleep(30)
  posturl = getposturl()
  if posturl != newpost:
    newpost = posturl
    firstArr = getnewpost()
    title = firstArr[0]
    content = firstArr[1]
    finalUrl = pushurl + '&title=' + title + '&msg=' + content + '&url=' + posturl
    s.get(finalUrl)
    pass
  else:
    pass
