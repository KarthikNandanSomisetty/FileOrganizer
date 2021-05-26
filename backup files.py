import os
import shutil

source = input ("enter the source name : ")
destination = input ("enter the destination : ")
source = source + '/'
destination = destination + '/'
list_of_files = os.listdir(source)
for file in list_of_files :
    shutil.copy((source+file),destination)