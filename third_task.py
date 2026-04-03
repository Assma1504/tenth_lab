from PIL import Image, ImageFont, ImageDraw

path = ("./images/birthDay2.jfif")
myImg = Image.open(path)
newImg = Image.new("RGBA", myImg.size)
imgDraw = ImageDraw.ImageDraw(newImg)
# personName = input("Who you want to congratulate: ")
personName = "Assma"
imageWidth = int(myImg.width / 2)
textCongratulation = (f"Congratulations {personName}")
font = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", size=30)
imgDraw.text((imageWidth,20), textCongratulation, font = font, fill = (255,00,00,255) )
myImg.paste(newImg, newImg)

myImg.show()