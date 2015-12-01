import jinja2
import webapp2

env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

class Email(object):
    def __init__(self, org_name, host_site, club_num):
        self.org_name=org_name
        self.host_site=host_site
        self.club_num=club_num

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('main.html')
        self.response.write(template.render())
    def post(self):
        results = env.get_template('results.html')
        template_variables= {'noun1':self.request.get("noun1"),'activity':self.request.get("activity"),'teacher':self.request.get("teacher"),'celebrity':self.request.get("celebrity"), 'show':self.request.get("show"), 'fun':self.request.get("fun")}
        self.response.write(results.render(template_variables))

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
