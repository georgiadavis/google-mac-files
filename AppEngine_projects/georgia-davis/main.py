import webapp2 #import webapp2
import jinja2 #import jinja2
import datetime #import datetime provides current date and time
from google.appengine.ext import ndb #allows you to access ndb to store persistent data

#a library that allows us to use methods for our templates
env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

class MainHandler(webapp2.RequestHandler):#this handles the default url and render index.html
    def get(self):
        template = env.get_template('index.html')
        self.response.write(template.render())

class Post(ndb.Model): #creating a model(a structure that holds a amount of commands) called Post
    title = ndb.StringProperty(required=True)
    content = ndb.StringProperty(required=True)#in this case, 3
    timestamp = ndb.DateTimeProperty(required=True)

class BlogHandler(webapp2.RequestHandler):#requesthandler: where you process the request, manipulate data, and issues a response
    def get(self):
        post = Post.query().fetch() #Getting content from datastore
        template = env.get_template('index.html')
        template_variable= {"posts": post}
        self.response.write(template.render(template_variable))
    def post(self): # Take user input, turns it into a post, and adds it to the
                    # database
        title = self.request.get('title')
        content = self.request.get('content')
        post = Post(title=title,
                        content=content,
                        timestamp=datetime.datetime.now())
        post.put()#DO NOT PUT UR PUTS UNDER REDIRECT
        self.redirect("/")

# class Comment (ndb.Model):
#     content = ndb.TextProperty()
#     post_key=ndb.KeyProperty()

# class PostHandler(webapp2.RequestHandler):
#     def get(self):
#         #1 Read the request
#         urlsafe_post_key=self.request.get('key')
#         #2. Logic/interaact with the DB
#         post_key=self.response.write('Hello world!')
#         post = post_key.get()
#         #3 Render a response
#         variables= {'post':post}
#         template = env.get_template('post.html')
#         self.response.write(template.render(variables))
#     def post(self):
#         urlsafe_post_key=self.request.get('post_key')
#         content = self.request.get('content')
#
#         post_key = ndb.Key(urlsafe=urlsafe_post_key)
#         comment = Comment(content=content, post_key=post_key)
#         comment.put()
#
#         self.redirect('/post?key=%s' % urlsafe_post_key)

app = webapp2.WSGIApplication([
    # ('/', MainHandler)
    ('/', BlogHandler)
    # ('/post', PostHandler)
], debug=True)
