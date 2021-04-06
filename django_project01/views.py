#created this file myself- Aditya
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    
    return render(request, 'index.html')

def analyze(request):
    # get the text
    input_text=request.POST.get('text','default')
    #check checkbox values
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    charcounter=request.POST.get('charcounter', 'off')
    

    # check which checkbox is on
    if removepunc=="on":
        punctuations='''!()-[]{};:'",<>./"\"|?@#$%^&*_~+='''
        analyzed=""

        for char in input_text:
            if char not in punctuations:
                analyzed=analyzed+ char

        params={"purpose":'Removed Punctuations', "analyzed_text": analyzed}
        input_text=analyzed
        

    if fullcaps=='on':
       analyzed=''
       for char in input_text:
           analyzed=analyzed+char.upper()

       params={"purpose":'Capitalize Letters', "analyzed_text": analyzed}
       input_text=analyzed
    

    if newlineremover=='on':
        analyzed=''
        for char in input_text:
            if char !="\n" and char!='\r':
                analyzed=analyzed+char

        params={"purpose":'Remove New Lines', "analyzed_text": analyzed}
        input_text=analyzed
        
    
    if extraspaceremover=='on':
        analyzed=''
        for index, char in enumerate(input_text):
            if not(input_text[index]==" " and input_text[index+1]==' '):
                analyzed=analyzed+char

        params={"purpose":'Remove Extra Spaces', "analyzed_text": analyzed}
        input_text=analyzed
     

    if charcounter=='on':
        analyzed=len(input_text)
        params={"purpose":"Counting Characters", 'analyzed_text':analyzed}
        


    if(removepunc!='on' and newlineremover!='on' and fullcaps!='on' and extraspaceremover!='on' and charcounter!='on'):
        return HttpResponse("Error")
    return render(request,'analyze.html', params)
