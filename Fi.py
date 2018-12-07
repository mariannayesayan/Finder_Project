class User:
    def __init__(self, firstname, lastname, degree, jobtitle, organization):
        self.firstname = firstname
        self.lastname = lastname
        self.degree = degree
        self.jobtitle = jobtitle
        self.organization = organization
        self.next = None

class Finder:
    def __init__(self):
        self.users = None

    def append(self,user):
        if self.users is None:
            self.users = user
        else:
            temp = self.users
            while temp.next is not None:
                temp = temp.next
            temp.next = user

    def askfindinfo(self):
        print "here are the keywords: firstname, lastname, degree, jobtitle, organization"
        firstname = raw_input("please enter value for firstname or enter "" if there is no value")
        lastname = raw_input("please enter value for lastname or enter "" if there is no value")
        degree = raw_input("please enter value for degree or enter "" if there is no value")
        jobtitle = raw_input("please enter value for jobtitle or enter "" if there is no value")
        organization = raw_input("please enter value for organization or enter "" if there is no value")
        user = User(firstname, lastname, degree, jobtitle, organization)
        return user

    def displayuserinfo(self, user):
        print "firsname: ", user.firstname, "lastname: ", user.lastname, "degree: ", user.degree,\
            "jobtitle: ", user.jobtitle, "organization: ", user.organization
