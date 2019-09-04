import shutil
import os
from PIL import Image

IMAGE_WIDTH = 500
SOURCE_FOLDER = 'images/originals/'
DESTINATION_FOLDER = 'images/smalls/'

def copytree(src=SOURCE_FOLDER, dst=DESTINATION_FOLDER, symlinks=False, ignore=None):
    shutil.rmtree(DESTINATION_FOLDER)
    os.mkdir(DESTINATION_FOLDER)

    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)

def smallify_photo(pPath):
    img = Image.open(pPath)
    scaleFactor = IMAGE_WIDTH/float(img.size[0])
    horizontalSize = int((float(img.size[1])*float(scaleFactor)))
    img = img.resize((IMAGE_WIDTH,horizontalSize), Image.ANTIALIAS)
    img.save(pPath)
    print("Saved ",pPath)

def main():
    copytree()
    for r,d,f in os.walk(DESTINATION_FOLDER):
        for file in f:
            fullPath= os.path.join(r,file)
            if 'png' in fullPath or 'jpg' in fullPath or 'jpeg' in fullPath:
                smallify_photo(fullPath)



if __name__ == "__main__":
    main()