#! python3
# create custom photo invites using a lost of photos
import os
from PIL import Image, ImageDraw, ImageFont

guestFile = open('guests.txt', 'r')
guests = guestFile.readlines()
flowerIm = Image.open('flower.jpg').convert('RGBA')
flowerIm = flowerIm.resize((200, 200))
flowerWidth, flowerHeight = flowerIm.size
for name in guests:
    print('creating invite...')
    im = Image.new('RGBA', (300, 360), 'black')
    imHeight, imWidth = im.size
    draw = ImageDraw.Draw(im)
    fontsFolder = 'C:\\Windows\\Fonts'
    arialFont = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 12)
    draw.text((50, 50), 'dear '+name.strip('\n')+' you are invited to our party', fill='gray', font=arialFont)
    im.paste(flowerIm, (70, 150), flowerIm)
    print('saving %s\'s invite...' % name.strip('\n'))
    im.save(os.path.join('imgur', '%s_Invite.png'%name.strip('\n')))