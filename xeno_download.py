
# importing libraries

import os
import random as r
import time as t
import pathlib

# importing APIs 

import xenopy
from xenopy import Query

# defining variables

Generalist_Birds = ["greenfinch","jackdaw","kestrel","reed bunting","rook","woodpigeon","yellow wagtail"]
Specialist_Birds = ["corn bunting","goldfinch","grey partride","lapwing","linnet","starling","stock dove","skylark","tree sparrow","turtle dove","whitethroat","yellowhammer"]
Currently_On_Soundcloud = ["Sparrow","Goldfinch","Barn Swallow","Dunnock","White Wagtail","Wood Pigeon","Robin","Great Tit"]
Downloaded = [""]
Files = [""]
Songs = [" "]
MetaFiles = [""]

# defining Function

def Download_Data():
  for x in range(len(Generalist_Birds)):

    # defining Query  

    q = Query(name=Generalist_Birds[x-1],q_gt="C",cnt="England",rec="David M",type="song")

    # downloading

    q.retrieve_recordings(multiprocess=True,nproc=10,attempts=10,outdir="datasets/")
    Downloaded.append(Generalist_Birds[x-1])

    # meta data

    metafiles = q.retrieve_meta(verbose=True)
    meta_data = open("MetaData.txt","a")
    meta_data.write(metafiles+"| |"+Generalist_Birds[x-1]+"\n")
    meta_data.close()

    # renaming file with metadata

  for file in os.listdir():
    if file == "google_upload.py" or file == "main.py" or file == "xeno_download.py":
      continue
    if os.path.isfile(file):
      Files.append(file)

  for x in range(len(Files)):
    if pathlib.PurePosixPath(Files[x-1]).suffix == ".mp3" or pathlib.PurePosixPath(Files[x-1]).suffix == ".mp4":
      Songs.append(Files[x-1])
      Files.remove(Files[x-1])
    elif pathlib.PurePosixPath(Files[x-1]).suffix == ".WMF" or pathlib.PurePosixPath(Files[x-1]).suffix == ".EMF":
      MetaFiles.append(Files[x-1])
      Files.remove(Files[x-1])
    elif pathlib.PurePosixPath(Files[x-1]).suffix == ".txt":
      MetaFiles.append(Files[x-1])

  for x in range(len(Songs)):
       
