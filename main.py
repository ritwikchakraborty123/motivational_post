from PIL import Image,ImageDraw,ImageFont

import json
import urllib.request
import bs4
import requests as rq
import datetime

image=Image.open("a2.jpg")
draw=ImageDraw.Draw(image)
font=ImageFont.truetype("arial.ttf",50)

origin=datetime.date(2020,12,15)
today=datetime.date.today()

url = "https://type.fit/api/quotes"
obj=rq.get(url);
jq=obj.json()

quote=jq[(origin-today).days]["text"]

today=""
length=len(quote)

for i in range(0,length):
	today+=quote[i]
	if(i%50==0 and i):
		if(quote[i]==' '):
			today+='\n'
		else:
			today+='-'
			today+='\n'

H=image.height
W=image.width
cod=235,347
draw.text(cod,today,"brown",font)
# image.save("abc.jpg")
image.show()

