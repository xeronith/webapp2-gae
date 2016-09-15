import webapp2

class Root(webapp2.RequestHandler):
    def get(self):
        self.response.write('webapp2-gae')

app = webapp2.WSGIApplication([
    ('/', Root)
], debug = True)