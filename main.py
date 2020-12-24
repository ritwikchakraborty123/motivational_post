from PIL import Image,ImageDraw,ImageFont

import json
import urllib.request
import bs4
import requests as rq
import datetime
import random
url = "https://type.fit/api/quotes"
obj=rq.get(url);
jq=obj.json()
print(jq)
cnt=0;
while True:
	try:

		name="a"+str(random.randrange(1, 6))+".jpg"
		image=Image.open(name)
		image=image.resize((1024,1024));

		draw=ImageDraw.Draw(image)
		# C:\Windows\Fonts set there .ttf file
		font = ImageFont.truetype("Poppins-Black.ttf",30)


		# origin=datetime.date(2020,12,23)
		# today=datetime.date.today()


		# quote=jq[(origin-today).days]["text"]

		quote=jq[cnt]["text"]
		cnt+=1
		today=""

		li=[]
		li=quote.split(" ")
		total=0
		limit=30
		lii=[]
		for i in li:
			if(len(i)+total<=limit):
				today+=i
				today+=' '
				total+=len(i)+1
			else:
				lii.append(today)
				today=""
				today+=i
				today+=' '
				limit+=30
				total+=len(i)+1
		lii.append(today)
		x=image.width/2
		y=image.height/2-100
		# print(today)
		for i in lii:
			z,h = draw.textsize(i)
			draw.text((image.width-image.width/2-z/2-150,y),i,"white",font)
			y+=50
		# image.save("output/a"+str(cnt)+".jpg")
	except:
		print(cnt + " motivational post created ... ")
		break
# image.show()

