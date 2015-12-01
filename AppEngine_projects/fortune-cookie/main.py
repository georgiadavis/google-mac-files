import jinja2
import webapp2
import random

env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('main.html')
        sayings= ["You learn from your mistakes... You will learn a lot today", "If you have something good in your life, don't let it go!","Your shoes will make you happy today.","Meeting adversity well is the source of your strength."]
        self.response.write(template.render({"fortune":random.choice(sayings)}))

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
