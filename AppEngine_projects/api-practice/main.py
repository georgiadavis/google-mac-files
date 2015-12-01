# import google.appengine.api import urlfetch
import google.appengine.api import users
import webapp2
from google.appengine.ext import ndb

#datastore
class Student (ndb.Model):
    name= ndb.StringProperty(required=True)
    university= ndb.StringProperty(required=True)
    age=ndb.IntegerProperty()

#instance variable to store Jenna's information
x= Student(name= "Jenna Price", university="Stanford", age=20)
#Key to get the information back
key = ndb.Key(Student,5629499534213120)
x = key.get()
print x.name
#Add new instance variable to store Georgia's information
x = Student(name='Georgia Davis', university= "University of Maryland", id="georgiadavis@google.com")
x.put()
#Print student information
print Student.query().fetch()

# User API
# class MainHandler(webapp2.RequestHandler):
#     def get(self):
        # user = users.get_current_user() #returns the object with properties about a user
        # #if the user is not logged in
        #     if user is None:
        #         login_url = users.create_login_url('/')
        #         self.response.write('<a href="%s">Log In</a>' % login_url)
        #     #if the user is logged in
        #     else:
        #         logout_url = users.create_logout_url('/')
        #         self.response.write('<a href="%s">Log Out</a>' % logout_url)
        # self.response.write(user)
    
# URL FETCH
# class MainHandler(webapp2.RequestHandler):
#     def get(self):
        # url = "http://www.georgiadavis-mad-libs.appspot.com/"
        # response = urlfetch.fetch(url)
        # self.response.write(response.content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
