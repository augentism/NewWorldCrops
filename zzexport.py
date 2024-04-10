import os
import zipfile
import io
import shutil
cwd = os.getcwd()
#print(cwd)
zip_name = "NewWorldCrops"
directory_name = "assets"
fullpath = os.path.join(cwd,directory_name)
#print(fullpath)
if os.path.isfile("./" + zip_name +".zip"):
    print("found zip, deleting...")
    os.remove("./" + zip_name +".zip")


shutil.make_archive(zip_name, 'zip', fullpath)

with zipfile.ZipFile("NewWorldCrops.zip", mode='a') as zf:
    zf.write("./modinfo.json")

if os.path.isfile("C:\\Users\\Calvin\\AppData\\Roaming\\Vintagestory\\Mods\\" + zip_name + ".zip"):
    os.remove("C:\\Users\\Calvin\\AppData\\Roaming\\Vintagestory\\Mods\\" + zip_name + ".zip")

shutil.copy("./" + zip_name +".zip", "C:\\Users\\Calvin\\AppData\\Roaming\\Vintagestory\\Mods\\")