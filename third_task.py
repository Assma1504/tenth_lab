from PIL import Image, ImageFont, ImageDraw

path = ("./images/birthDay2.jfif")
myImg = Image.open(path)
newImg = Image.new("RGBA", myImg.size)
imgDraw = ImageDraw.ImageDraw(newImg)
personName = input("Who you want to congratulate: ")
# personName = "Assma"
textCongratulation = (f"Congratulations {personName} !")
font = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", size=20)
textBbox = imgDraw.textbbox((0, 0), textCongratulation, font=font)
textWidth = textBbox[2] - textBbox[0]
textHeight = textBbox[3] - textBbox[1]
textLocation = (int(myImg.width/2  - textWidth/2 ),int( myImg.height / 2  - textHeight / 2 ))
imgDraw.text(textLocation, textCongratulation, font = font, fill = (255,00,00,255) )
myImg.paste(newImg, newImg)

# print(myImg.width)
# print(myImg.height)
# print(textWidth)
# print(textHeight)
# print(textLocation)

# myImg.show()
myImg.save("/images/watermark.png")