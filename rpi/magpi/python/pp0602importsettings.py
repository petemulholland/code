# Import Settings
# By Jaseman - 22nd September 2012

# create setting file with this text:
#screen width:1024
#screen height:600
#window caption:Fading Titles
#text size:100
#title 1:Jaseman Presents...
#title 2:A Python Pit Production
#title 3:FADING TITLE DEMO

f = open('settings.txt', 'r') # Opens a text file to read settings from (r)
settings = [] # Create a variable array to hold the settings

for line in f: # Loop to get each line of the file into the array
	settings.append(line)

f.close() # Close the file

# This part splits each line at the colon (:) and defines variables
screenx=settings[0].split(':'); 
screeny=settings[1].split(':')
windowcaption=settings[2].split(':'); 
textsize=settings[3].split(':')
title1=settings[4].split(':'); 
title2=settings[5].split(':')
title3=settings[6].split(':')

import os,pygame; 
from pygame.locals import *; 
pygame.init()

os.environ['SDL_VIDEO_WINDOW_POS'] = 'center'
pygame.display.set_caption(windowcaption[1].strip())
screen=pygame.display.set_mode([int(screenx[1]),int(screeny[1])],0,32)
fadesurf=pygame.Surface((int(screenx[1]),int(screeny[1])))
titlesurf=pygame.Surface((int(screenx[1]),int(screeny[1])))
nexttitle=1;run=1

while run==1:
	# Print the next title
	font = pygame.font.Font(None,int(textsize[1]))
	if nexttitle==1:
		text = font.render(title1[1].strip(),True,(255,255,255))
	if nexttitle==2:
		text = font.render(title2[1].strip(),True,(255,255,255))
	if nexttitle==3:
		text = font.render(title3[1].strip(),True,(255,255,255))
	tgr=text.get_rect
	tp=tgr(centerx=screen.get_width()/2,centery=screen.get_height()/2)
	titlesurf.blit(text,tp)

	# Increase the transparency of fadesurf
	for t in range(255,0,-20):
		fadesurf.set_alpha(t); screen.blit(titlesurf,(0,0))
		screen.blit(fadesurf,(0,0)); pygame.display.update()

	# Decrease the transparency of fadesurf
	for t in range(0,256,20):
		fadesurf.set_alpha(t); screen.blit(titlesurf,(0,0))
		screen.blit(fadesurf,(0,0)); pygame.display.update()

	titlesurf.fill((0,0,0)); screen.blit(fadesurf,(0,0))
	pygame.display.update()
	nexttitle+=1
	if nexttitle>=4:
		nexttitle=1