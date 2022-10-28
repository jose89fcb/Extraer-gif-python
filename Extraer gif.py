
from PIL import Image, ImageSequence
import os
import pathlib
 


NombreArchivoGif = input("Escribe el nombre del gif: ")
im = Image.open(f"{NombreArchivoGif}")
 

Carpeta= input("Escribe el nombre de la carpeta: ")
pathlib.Path(f"{Carpeta}").mkdir(parents=True, exist_ok=True)
os.chdir(os.path.join(os.getcwd(),f"{Carpeta}")) 


i =1




app = []

for fr in ImageSequence.Iterator(im):
    app.append(fr)
  
    fr.save("%d.gif"%i)
    print("imagen_%d.png"%i)
    
    i = i + 1
 
