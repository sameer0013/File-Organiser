
import os
def isprograms(file,word):
    with open(file) as f:
        filecontent=f.read().lower()
        word=word.lower().strip(" ")
    if word in filecontent.lower():
        return True
    else:
        return False

if __name__=='__main__':
    directories=os.listdir()
    word=input("ENTER THE WORD YOU WANT TO SEARCH IN EXCISTING FILES: ")

    count=0
    for i in directories:
        if  i.endswith('.txt'):
            flag=isprograms(i,word)
            if (flag):
                count+=1
                print(f"***{word} is found in {i}")   #tell in which-which files word is found
            else:
                print(f"***{word} is not found in {i}")  #tell in which-which files word is not found 

    print("****program is detected in directories!!!!!!")
    print(f"{count} times program is founded")            #tell in how many files word is founded 

