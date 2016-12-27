from PIL import Image
import zbarlight

start=['','7ab7df3f4425f4c446ea4e5398da8847']
line=''
count=0
check=False
while count<11001 and check==False:
	try:
		current=start[1]
		image = Image.open('list/'+current+'.png')
		image.load()
		line=zbarlight.scan_codes('qrcode', image)[0]
	except:
		print ('File: '+start[0]+'.png | QR decode: '+line)
		check=True
	start[0]=current
	start[1]=line[(len(line)-32):]
	count+=1
