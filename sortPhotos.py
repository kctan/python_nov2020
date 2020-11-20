import os
import shutil
from datetime import datetime

# Need to create a folder called sorted and a folder called unsorted_photos before running the script
# Place the python script in same folder as sorted and unsorted_photos folder
# This script will sort the photos in the sorted folder based on last mofified date and create folder yyyy_mm to sort the photos in

# change the directory name to the name of unsorted folder if your folder name is different
dirname = "unsorted_photos"
sortedDirName = "sorted" 

# list all the files
listOfFiles = os.listdir(dirname)
for i in listOfFiles:
    filename = dirname+"/"+i
    # get last modified time
    lastModified = os.path.getmtime(filename)

    # format datetime to yyyy_mm to identify folder to move file to
    dt_object = datetime.fromtimestamp(lastModified)
    folderName =dt_object.strftime("%Y_%m")
    
    print(i + "-> "+folderName)
    #create new folder if does not exist
    if (not (os.path.isdir(sortedDirName+"/"+folderName))):
        os.mkdir(sortedDirName+"/"+folderName)
    
    # move file to relevant folder based on year and mth
    newFileName = sortedDirName+"/"+folderName+"/"+i
    shutil.move(filename, newFileName)
    print("Moved: "+i)

        