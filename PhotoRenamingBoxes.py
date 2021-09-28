# Created by Austin White
# May 24 2021
# For Granite Creek Copper


#To use, add photos from camera to a subdirectory called "Photos",
#ensure the core boxes in the photos are in acsending order and the photographs go dry - wet - dry -wet
#to run the program, run PhotoRenamingBoxes.exe and after finishing the photos will have the new corresponding name to the
# hole box and depth values.

#imports
import os
import time

#Varbiable Declaration
depthto=0
oldwet = ""
newwet = ""
olddry = ""
newdry = ""
wetordry = 0

print("Ensure the photos were taken in the following order:")
print("Box 1-2 Dry, Box 1-2 Wet, Box 3-4 Dry, Box 3-4 Wet, Box 5-6 Dry, Box 5-6 Wet, ...")
#Gather Starting Input
hole = input("Input Hole Name (ie: CRM21-006): ")
box = input("Input starting box number(Top Box of first Photo): ")
depthfrom = input("Input starting Depth(Starting Depth of top box of first photo) value in meters: ")

#path to folder with photos
cwd = os.getcwd()
cwd = cwd + "/photos"
filePath = cwd
arr = os.listdir(filePath)

#loop to change photo names
for  filedry in arr:
    #If Dry, get new Name
    if wetordry == 0:

        depthfromcpy = depthfrom
        newbox = box
        newbox2 = int(box)+1
        depthto = input("Input ending depth(m) value of box: "+ str(newbox2) + ": ")
        depthtocpy=depthto
        
        newNameDry = hole+"_Box_"+str(newbox)+"-"+str(newbox2)+"_("+str(depthfromcpy)+"-"+str(depthtocpy)+"m)_DRY.JPG"
        newNameWet = hole+"_Box_"+str(newbox)+"-"+str(newbox2)+"_("+str(depthfromcpy)+"-"+str(depthtocpy)+"m)_WET.JPG"
        olddry = filePath+"/"+filedry
        newdry = filePath+"/"+newNameDry
        newwet = filePath+"/"+newNameWet
        os.rename(olddry, newdry)
        depthfrom = depthto
        box=int(box)+2
        wetordry = 1
    #if Wet, get the dry name and change the suffix to WET
    else:
        oldwet = filePath+"/"+filedry
        os.rename(oldwet, newwet)
        wetordry = 0

print("Photos have been renamed, program will automatically close in 3 seconds")
time.sleep(3)
    
    #Photo Name Template
    #CRM21-006_Box_1-2_(1.30-13.95m)_DRY.JPG