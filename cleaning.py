import os
def createIfnotExist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
    
def movefiles(foldername,files):
    for file in files:
        os.replace(file,foldername+'/'+str(file))

files= os.listdir()
files.remove("main.py")
print(files)

createIfnotExist('Images')
createIfnotExist('docs')
createIfnotExist('Others')

imageExts=[".png",".jpg",".jpeg"]
docsExts=[".txt",".docs",".docx",".pdf"]
others=[]


images=[file for file in files if os.path.splitext(file)[1].lower() in imageExts]
docs=[file for file in files if os.path.splitext(file)[1].lower() in docsExts]
for file in files:
    ext=os.path.splitext(file)[1]
    if (ext not in imageExts) and (ext not in docsExts) and os.path.isfile(file):
        others.append(file)


movefiles("Images",images)
movefiles("docs",docs)
movefiles("Others",others)