class Facebook(object):
    def __init__ (self , name, username, relationship_status): #All classes have this. Self is object itself
        self.name = name
        self.username = username
        self.relationship_status = relationship_status

    def description(self): #Takes a description
        print "Hey, my name is {0}. My username is {1}. My relationship status is {2}." .format(self.name, self.username, self.relationship_status)

# Georgia = Facebook('Georgia','georgiadavis', 'Married')
# Georgia.description()
