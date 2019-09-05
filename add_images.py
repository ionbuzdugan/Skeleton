import shutil
import os
from PIL import Image
from bs4 import BeautifulSoup, NavigableString
import json
from create_ref_json import main as create_ref_json

IMAGE_WIDTH = 500
ORIGINAL_FOLDER = 'images/originals/'
SMALL_FOLDER = 'images/smalls/'
PAGES_FOLDER = 'pages/'
PHOTO_LIB = json.load(open('photo_ref.json'))
INDEX_TEMPLATE = open('index_template.txt')

# Copy source folder into images/ directory
def clear_dirs(symlinks=False, ignore=None):
    # Delete all files in destination
    shutil.rmtree(PAGES_FOLDER)
    os.mkdir(PAGES_FOLDER)
    shutil.rmtree(SMALL_FOLDER)
    os.mkdir(SMALL_FOLDER)

    # Copy all files and folders into smalls folder
    for item in os.listdir(ORIGINAL_FOLDER):
        s = os.path.join(ORIGINAL_FOLDER, item)
        d = os.path.join(SMALL_FOLDER, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)

# Resize and saved photo passed contained din pPath argument
def smallify_photo(pPath):
    img = Image.open(pPath)
    scaleFactor = IMAGE_WIDTH/float(img.size[0])
    horizontalSize = int((float(img.size[1])*float(scaleFactor)))
    img = img.resize((IMAGE_WIDTH,horizontalSize), Image.ANTIALIAS)
    img.save(pPath)
    print("Saved ",pPath)

# Walk through photo directory and resize photos
def convert_photos():
    for r,d,f in os.walk(SMALL_FOLDER):
        for file in f:
            fullPath= os.path.join(r,file)
            if 'png' in fullPath or 'jpg' in fullPath or 'jpeg' in fullPath:
                smallify_photo(fullPath)

# Add photo page link to index.html 
def add_links_to_index(name,link):
    with open("index.html","w") as fIndex:
        for line in INDEX_TEMPLATE:
            if 'END LINKS HERE' in line:
                
            fIndex.write(line)


def create_ref():
    d=DESTINATION_FOLDER
    subdirs = [o for o in os.listdir(d) if os.path.isdir(os.path.join(d,o))]
    with open(REFERENCE_FILE) as f:
        t = f.read()
        for folder in subdirs:
            folderName=folder.replace("_"," ")
            folderName = folderName.title()
            if folderName not in t:
                t=t+folderName+ " | DATE\n"
                t=t+folder+"\n"
    
    with open(REFERENCE_FILE,"w") as f:
        f.write(t)
                
def create_page(name,link):
    # imgs = [i for i in os.listdir('images/'+link+"/")] if not os.isdir(os.path.join(i,))
    with open(REFERENCE_FILE) as f:
        l = f.readlines()



def main():
    print(INDEX_TEMPLATE.read()[0:21])
    convert_photos()
    create_ref()
    remove_links_from_index()
    with open(REFERENCE_FILE,"r") as f:
        l = f.readlines()
        for i in range(0,len(l),2):
            name = l[i][0:-1]
            link = l[i+1][0:-1]
            add_links_to_index(name, link)
            create_page(name,link)



if __name__ == "__main__":
    main()