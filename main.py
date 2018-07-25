# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import webapp2
import jinja2
import os
import re
from wordlist import *
from google.appengine.api import urlfetch
import ast

# from models import Meme

jinja_current_directory = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = ['jinja2.ext.autoescape'],
    autoescape = True)
#Creates the dictonaries that hold every word in the page.

def get_definition():
    app_id = '2d63d4c2'
    app_key = '7cc6f918e6a883687fb992d834cf018e'
    language = 'en'
    word_id = 'hello'

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

def findHardWord(unfilteredText):
    wordList = unfilteredText.split()
    # researchDict = []
    # for x in range (0, len(wordList)):
    #     researchDict[x] = wordList[x]
    #     #reverseDict = {wordList[x] : x}
    #     #print researchDict
    return wordList
class WelcomePage(webapp2.RequestHandler):
    def get(self):
        welcome_template = \
                jinja_current_directory.get_template('templates/demo.html')
        self.response.write(welcome_template.render())
        print ("about to print definition")
        print get_definition()
    def post(self):
        researchText = self.request.get('researchPaste')
        #researchDic = {"everything" : researchText}
        populationDict = {"wordList" :findHardWord(researchText)}
        #print(populationDict)
        #populationDict = findHardWord(researchText)
        welcome_template = jinja_current_directory.get_template('templates/demo2.html')
        #self.response.write(welcome_template.render(researchDic))
        self.response.write(welcome_template.render(populationDict))





# class MemeResultPage(webapp2.RequestHandler):
#     def post(self):
#         result_template = \
#                 jinja_current_directory.get_template('templates/result.html')
#
#         line_1 = self.request.get('user-first-ln')
#         line_2 = self.request.get('user-second-ln')
#         meme_type = self.request.get('meme-type')
#
#         template_dict = {
#             'line1': line_1,
#             'line2': line_2,
#             # Find a good image url for the meme_type
#             'image_url': getImageForMemeType(meme_type)
#         }
#
#         self.response.write(result_template.render(template_dict))
#         memeNew = Meme(line_1 = line_1, line_2 = line_2, meme_type = meme_type)
#         memeNew.meme_type = memeNew.getURL()
#         memeNew.put()


app = webapp2.WSGIApplication([
    ('/', WelcomePage),
], debug=True)
