FROM python:alpine
ENV TZ Asia/Hong_Kong

RUN apk add --no-cache tzdata && cp /usr/share/zoneinfo/Asia/Hong_Kong /etc/localtime && echo "Asia/Hong_Kong" > /etc/timezone && pip install beautifulsoup4 requests && wget https://raw.githubusercontent.com/loveqianool/locWechat2/master/toWechat.py

CMD ["python","/toWechat.py"]
