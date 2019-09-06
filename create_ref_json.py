import json
import os

DIR = 'images/originals/'

def main():
    jsonList = {}
    jsonList=[]
    currentRef = json.load(open('photo_ref.json'))
    for r,d,f in os.walk(DIR):
        for dir in d:
            date = 'DATE'
            for tDir in currentRef:
                if tDir['name'] == dir:
                    date = tDir['date']
            folder={}
            folder['name'] = dir
            folder['text'] = dir.replace("_"," ").title()
            folder['date'] = date
            folder['link'] = "pages/" + dir + ".html"
            folder['photos']=[]
            for r1,d2,f2 in os.walk(os.path.join(DIR,str(dir))):
                for file in f2:
                    photo={}
                    photo['link-small']=str(os.path.join(DIR,dir,file)).replace("\\","/").replace('originals','smalls')
                    photo['link-original']=str(os.path.join(DIR,dir,file)).replace("\\","/")
                    folder['photos'].append(photo)
            jsonList.append(folder)
    with open('photo_ref.json','w') as f:
        json.dump(jsonList,f,indent=4)
