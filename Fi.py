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
        self.head = None

    def append(self,user):
        if self.head is None:
            self.head = user
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = user

    def askfindinfo(self):
        print "here are the keywords: firstname, lastname, degree, jobtitle, organization"
        print "Enter the values for the keywords above to fin matches"
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


    def findmatches(self):
        user = self.askfindinfo()
        temp = self.head
        while temp is not None:
            if temp.firstname == user.firstname:
                print "match by firstname"
                self.displayuserinfo(temp)
            elif temp.lastname == user.lastname:
                print "match by lastname"
                self.displayuserinfo(temp)
            elif temp.degree == user.degree:
                print "match by degree"
                self.displayuserinfo(temp)
            elif temp.jobtitle == user.jobtitle:
                print "match by jobtitle"
                self.displayuserinfo(temp)
            elif temp.organization == user.organization:
                print "match by organization"
                self.displayuserinfo(temp)
            temp = temp.next

def main():
    finder = Finder()
    u1 = User("1", "2", "3", "4", "5")
    u2 = User("6", "7", "8", "9", "10")
    u3 = User("2", "6", "2", "5", "5")
    u4 = User("8", "2", "5", "7", "5")
    finder.append(u1)
    finder.append(u2)
    finder.append(u3)
    finder.append(u4)
    finder.findmatches()
main()