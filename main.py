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
    # from wordList.py import *
    # from models import Meme

    jinja_current_directory = jinja2.Environment(
        loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
        extensions = ['jinja2.ext.autoescape'],
        autoescape = True)
    #Creates the dictonaries that hold every word in the page.
    def getWordList(unfilteredText):
        wordList = unfilteredText.split()
        # researchDict = []
        # for x in range (0, len(wordList)):
        #     researchDict[x] = wordList[x]
        #     #reverseDict = {wordList[x] : x}
        #     #print researchDict
        return wordList
    def getHardWords(unfilteredText):
        wordList = unfilteredText.split()
        hardWordList = []
        for x in range (0,len(wordList)):
            if(len(wordList[x]) > 8):
                hardWordList.append(wordList[x])
        return hardWordList
    class WelcomePage(webapp2.RequestHandler):
        def get(self):
            welcome_template = \
                    jinja_current_directory.get_template('templates/demo.html')
            self.response.write(welcome_template.render())
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
