from google.appengine.ext import ndb
class Meme(ndb.Model):
    line_1 = ndb.StringProperty(required=True)
    line_2 = ndb.StringProperty(required=True)
    meme_type = ndb.StringProperty()

    def getURL(self):
        return "../images/%s.jpg" % self.meme_type
