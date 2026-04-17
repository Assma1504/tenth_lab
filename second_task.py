from PIL import Image

dictPostcard = {
    1:"./images/valentineDay.png",
    2: "./images/newYear.jfif",
    3:"./images/birtyhDay.webp",
}

holidayNumber = int(input("Please choose the holiday name from the list bellow (you can choose only the number): \n 1: Valentine's day \n 2: New year \n 3: Birth day \n"))
# match holidayName:
#     case 1:
#         myImg = Image.open(dictPostcard["valentineDay"])
#         myImg.show()
#     case 2:
#         myImg = Image.open(dictPostcard["newYear"])
#         myImg.show()
#     case 3:
#         myImg = Image.open(dictPostcard["birtyhDay"])
#         myImg.show()
#     case _:
#         print("Please choose the correct number")
if holidayNumber in dictPostcard.keys():
    myImg = Image.open(dictPostcard[holidayNumber])
    myImg.show()
else:
    print("Please choose a valid number from the list")





