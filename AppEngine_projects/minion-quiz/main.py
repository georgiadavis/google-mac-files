import webapp2
import jinja2
from collections import Counter
import re

env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('index.html')
        self.response.write(template.render())
    def post(self):
    minion = {"Dave":0, "Stuart":0, "Jerry":0, "Jorge":0, "Tim":0, "Mark":0, "Phil":0, "Kevin":0}
    favoritethings= {
        "missiles":("Dave"),
        "laughing":("Stuart"),
        "BFF":("Jerry"),
        "bottom":("Jorge"),
        "boss":("Tim",),
        "sing":("Mark",),
        "kiss":("Phil",)}
    heights={
        "short":("Stuart","Phil","Kevin"),
        "medium":("Dave", "Jerry", "Jorge", "Mark"),
        "tall":("Tim")}
    hairstyles={
        "flat":("Dave", "Stuart", "Mark", "Phil", "Kevin"),
        "clump":("Tim"),
        "stick_straight":("Jorge"),
        "spikey_bald":("Jerry")}
    eyes={
        "one_eye":("Stuart", "Phil", "Kevin"),
        "two_eyes": ("Dave", "Jerry", "Jorge", "Tim", "Mark")}
    fav_selected = favoritethings[self.request.get("favoritething")]
    minion[fav_selected] += 1
    heights_selected = heights[self.request.get("heights")]
    for name in heights_selected
        minion[name] +=1
    eyes_selected = eyes[self.request.get("eyes")]
    for name in eyes_selected
        minion[name] +=1
    hair_selected = hairstyles[self.request.get("hairstyles")]
    for name in hair_selected
        minion[name] +=1
    #collection.Counter most_common method
     Counter(minion[name]).most_common(8)

    results = env.get_template('results.html')
    variables= {'favoritething':self.request.get("favoritething"),'hairstyle':self.request.get("hairstyle"),'height':self.request.get("height"),'eyes':self.request.get("eyes")}
    self.response.write(results.render(variables))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
], debug=True)
