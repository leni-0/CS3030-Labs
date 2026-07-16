import os

files = [f for f in os.listdir('.') if not f.startswith('.')]

oldNum = 8230
newNum = 0
newName = "Hawaii_trip_"


for f in files:
    oldNum += oldNum
    newNum +=newNum
    os.rename("IMG_" + str(oldNum) + ".jpg", newName + str(newNum) + ".jpg")
