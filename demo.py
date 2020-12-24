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

cnt=0;
# for total ouput do while True  
while (cnt<30):
	try:

		name="a"+str(random.randrange(1, 6))+".jpg"
		image=Image.open(name)
		image=image.resize((1024,1024));

		draw=ImageDraw.Draw(image)
		# C:\Windows\Fonts set there .ttf file
		font = ImageFont.truetype("Poppins-Black.ttf",30)
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
			draw.text((230,y),i,"white",font)
			y+=50
		image.save("output/a"+str(cnt)+".jpg")
	except:
		print(cnt + " motivational post created ... ")
		break

