# -*- coding: utf-8 -*-
"""
Script to rename JPG/jpg file names according
to meta data (EXIF) date taken 

Need to specify topic variable
--------------------------------------------
Versions:
    V0 - 14.12.2018 - Basics
--------------------------------------------
Autor: meteo-martin
"""
import os
import shutil
import glob
import copy
import datetime
import PIL.Image

topic="Topic"

flend=".JPG"
fl1=glob.glob("*.JPG")
fl2=glob.glob("*.jpg")
fls=sorted(fl1+fl2)

def createflname(prefix,dtfn,flending):
    flnew1=prefix+"-"+dtfn+flending
    i=1
    while os.path.exists(flnew1+"\n"):
        print("test")
        flnew1=prefix+"-"+dtfn+"-"+str(i)+flending
        i=i+1
    return(flnew1)

stats=[]
for fl in fls: 
    img = PIL.Image.open(fl)
    exif_data = img._getexif()
    dateTaken=copy.copy(exif_data[306])
    img.close()
    dts=datetime.datetime.strptime(dateTaken,"%Y:%m:%d %H:%M:%S")
    dtf=dts.strftime("%Y%m%d_%H%M%S")
    flnew=createflname(topic,dtf,flend)
    try: 
        print("Renaming "+fl+" to "+flnew)
        shutil.copy2(fl,flnew)
    except FileNotFoundError:
        print("!!! File "+fl+" does not exist !!!")
        stats.append(fl)
                 
print("+++ Renaming Completed +++")

if len(stats)>0:
    print("!!! Some Files could not be renamed !!!")
    print(["File "+str(f) for f in stats])