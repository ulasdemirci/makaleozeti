# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 11:31:11 2017

@author: Berceste
"""
import re , urllib
import logging
from gensim.summarization import summarize


logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
text=u""
website=urllib.urlopen("https://www.dunya.com/ara/haber?q=fevzi%20y%C4%B1lmaz".encode("utf-8"))
htmltext=website.read()
getinspect='<a href="/gundem/(.+?)title="'
pattern=re.compile(getinspect)
link=re.findall(pattern,htmltext)

for i in link:
    i= i.replace('"',"")
    test = "https://www.dunya.com/gundem/"+str(i)
    website2=urllib.urlopen(test)
    htmltext2= website2.read()
    getinspectmakale='<span style="line-height: 1.6em;">(.+?)</span>'
    pattern=re.compile(getinspectmakale,re.UNICODE)
    makale=re.findall(pattern,htmltext2)
    
    for j in makale:
         text =j
         if len(text) != 0:
            print ('Input text:')
            print (text)
             
            print ('Summary:')
            print (summarize(text))
             
            print ('Summary: ratio=0.5')
            print (summarize(text, ratio=0.5))
             
            print ('Summary: ratio=0.25')
            print (summarize(text, ratio=0.25))
             
            print ('Summary: word_count=50')
            print (summarize(text, word_count=50))
             
            from gensim.summarization import keywords
             
            print ('Keywords:')
            print (keywords(text))
                            
       