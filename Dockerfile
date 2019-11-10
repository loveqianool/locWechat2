docker run --rm --name test -p 6666:6666 --network z -dit python:2.7-alpine && \
docker exec -it test /bin/sh

apk add --no-cache tzdata
cp /usr/share/zoneinfo/Asia/Hong_Kong /etc/localtime
echo "Asia/Hong_Kong" > /etc/timezone
pip install beautifulsoup4 js2py request requests

wget https://raw.githubusercontent.com/loveqianool/locWechat2/master/toWechat.py
