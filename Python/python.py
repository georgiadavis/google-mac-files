#
# def go_get_dinner(student):
#   print "hey," + student
#   print "Close Computer"
#   print "Stand up"
#   print "Walk out the door"
#
# go_get_dinner("Jeff")
# go_get_dinner("Casey")
# go_get_dinner("Tamlyn")
#
# milk_type = "skim milk" #global variable
# def is_whole_milk():
#     if (milk_type == "whole milk"):
#         return True
#     else:
#         return False
#
# def milk_the_cow():
#     bessy_cow = "milked" #local variable
#     return bessy_cow
#
# print milk_the_cow
#
# Object Orientation

class Musician(object):
    def __init__ (self , name, genre, fav_album): #All classes have this. Self is object itself
        self.name = name
        self.genre = genre
        self.fav_album = fav_album

    def description(self): #Takes a description
        print "Hey, my name is {0}. I make {1} music. Check out my album {2}." .format(self.name, self.genre, self.fav_album)

    def is_in_studio(self):
        if self.recording:
            print "Yo, I'm in the studio recording my mixtape it's fire!"
        else:
            print "Hoping to get in the studio soon!"


kanye = Musician('Kanye','Rap', 'Yeezus', False)
kanye.description()
kanye.is_in_studio()

# class Facebook(object):
#     def __init__ (self , name, username, relationship_status): #All classes have this. Self is object itself
#         self.name = name
#         self.username = username
#         self.relationship_status = relationship_status
#
#     def description(self): #Takes a description
#         print "Hey, my name is {0}. My username is {1}. My relationship status is {2}." .format(self.name, self.username, self.relationship_status)
#
# Georgia = Facebook('Georgia','georgiadavis', 'Married')
# Georgia.description()
