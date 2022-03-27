import os 
def make(filename):
    if not os.path.exists(filename):
        os.makedirs(filename)

def move(foldername,files):
    for file in files:
        os.replace(file,f"{foldername}\{file}")

if __name__=='__main__':
    
    files = os.listdir()
    files.remove("fileclatter.py")
    print(files)
    make("Medias")
    make("Images")
    make("Docs")
    make("Others")

    imgext=[".img",".jpg",".jpeg"]
    image=[file for file in files if os.path.splitext(file)[1] in imgext]
    print(image)

    docext=[".doc",".txt",".pdf",".org"]
    docs=[file for file in files if os.path.splitext(file)[1] in docext]
    print(docs)

    mediaext=[".mp3",".mp4"]
    media=[file for file in files if os.path.splitext(file)[1] in mediaext]
    print(media)

    other=[]
    for file in files:
        if file not in image and file not in docs and file not in media and os.path.isfile(file):
            other.append(file)

    print(other)        

    move("Medias",media)
    move("Docs",docs)
    move("Images",image)
    move("others",other)





