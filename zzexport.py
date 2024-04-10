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
if os.path.isfile("./" + zip_name):
    print("found zip, deleting...")
    os.remove("./NewWorldCrops.zip")


shutil.make_archive(zip_name, 'zip', fullpath)

with zipfile.ZipFile("NewWorldCrops.zip", mode='a') as zf:
    zf.write("./modinfo.json")