from PIL import Image

path=("./images/BD.jfif")
myImg = Image.open(path)
# myImg.show()
#left top right bottom
boxCrop=(100,100,200,200)

croppedImage = myImg.crop(boxCrop)
# croppedImage.show()
croppedImage.save("./images/croppedImage.jfif")