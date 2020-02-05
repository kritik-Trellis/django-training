from django.http import HttpResponse
from django.shortcuts import render
import operator
def Home(request):
    return render(request,'home.html')

def countfile(request):
    worddict={}
    if request.method=="POST":
        uploadFile=request.FILES['myfile']
        file_name=uploadFile.name
        file_size=uploadFile.size
        txt=uploadFile.read().decode('utf-8')
        nline=0

        for word in txt.split():
            if word in worddict:
                worddict[word] +=1
            else:
                worddict[word] =1
        # with open(uploadFile,"rb") as fhand:
        #     for line in fhand:
        #         nline+=1
            sortedword=sorted(worddict.items(),key=operator.itemgetter(1),reverse=True)
        return render(request,'countfile.html',{'Text':txt,'FILE_NAME':file_name,'len':len(txt.split()),'worddict':sortedword,'lines':nline,'test':txt})



def count(request):
    worddict={}
    fulltext=request.GET['fulltext']
    wordList=fulltext.split()

    for word in wordList:
        if word in worddict:
            worddict[word] +=1
        else:
            worddict[word] =1
    sortedword=sorted(worddict.items(),key=operator.itemgetter(1),reverse=True)


    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordList),'worddict':sortedword})

def about(request):
    return render(request,'about.html')
