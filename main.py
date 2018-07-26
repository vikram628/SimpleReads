import webapp2
import jinja2
import os
import re
    # from wordList.py import *
    # from models import Meme
from google.appengine.api import urlfetch
import ast

jinja_current_directory = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = ['jinja2.ext.autoescape'],
    autoescape = True)
def get_rootword(str1):
    app_id = '2d63d4c2'
    app_key = '7cc6f918e6a883687fb992d834cf018e'

    language = 'en'
    word_id = str1
    rootword = ""

    url = 'https://od-api.oxforddictionaries.com:443/api/v1/inflections/' + language + '/' + word_id.lower()

    r= urlfetch.fetch(url, headers = {'app_id': app_id, 'app_key': app_key})

    if r.status_code == 200:
        rootword= ast.literal_eval(r.content)
    else:
        print "ERROR fetching URL:", r.status_code

    return rootword['results'][0]['lexicalEntries'][0]['inflectionOf'][0]['id']
def get_definition(str1):
    app_id = '2d63d4c2'
    app_key = '7cc6f918e6a883687fb992d834cf018e'
    language = 'en'
    word_id = get_rootword(str1)

    url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower() + "/definitions"
    #r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})
    #definition= r.json()["results"][0]["lexicalEntries"][0]["entries"][0]['senses'][0]["definitions"][0]

    r= urlfetch.fetch(url, headers = {'app_id': app_id, 'app_key': app_key})
    definition = ""
    if r.status_code == 200:
         definition= ast.literal_eval(r.content)
    else:
         print "ERROR fetching URL:", r.status_code
    return definition["results"][0]["lexicalEntries"][0]["entries"][0]['senses'][0]["definitions"][0]

#Creates the dictonaries that hold every word in the page.
def getWordList(unfilteredText):
    wordList = unfilteredText.split()
    return wordList
def getHardWords(unfilteredText):
    wordList = unfilteredText.split()
    hardWordList = []
    for x in range (0,len(wordList)):
        if(len(wordList[x]) > 8):
            try:
                wordList[x] = wordList[x] + "\n Definition: " + get_definition(wordList[x])
                hardWordList.append(wordList[x])
            except:
                print{"No def"}
    return hardWordList
class WelcomePage(webapp2.RequestHandler):
    def get(self):
        welcome_template = jinja_current_directory.get_template('templates/welcome.html')
        self.response.write(welcome_template.render())
        print ("about to print definition")
        print get_definition()
    def post(self):
        researchText = self.request.get('researchPaste')
        #researchDic = {"everything" : researchText}
        populationDict = {"wordList" :getWordList(researchText), "hardWordList": getHardWords(researchText)}
        print(populationDict)
        # hardPopulationDict = {"hardWordList" : getHardWords(researchText) }
        # print(hardPopulationDict)
        #populationDict = findHardWord(researchText)
        welcome_template = jinja_current_directory.get_template('templates/resultPage.html')
        #self.response.write(welcome_template.render(researchDic))
        self.response.write(welcome_template.render(populationDict))
        wlist = ['helpful']
        print('#param1',get_rootword('changes'))
        # wlist[0] = wlist[0] + "/n Definiton: " + get_definition(wlist[0])
        # print wlist[0]

app = webapp2.WSGIApplication([
    ('/', WelcomePage),
], debug=True)
