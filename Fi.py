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
            list = ["match by:"]
            if temp.firstname == user.firstname:
                list.append("firstname")
            if temp.lastname == user.lastname:
                list.append("lastname")
            if temp.degree == user.degree:
                list.append("degree")
            if temp.jobtitle == user.jobtitle:
                list.append("jobtitle")
            if temp.organization == user.organization:
                list.append("organization")
            if temp.firstname == user.firstname or temp.lastname == user.lastname\
                or temp.degree == user.degree or temp.jobtitle == user.jobtitle or temp.organization == user.organization:
                for i in range(len(list)):
                    print list[i],
                print ""
                self.displayuserinfo(temp)
            temp = temp.next

def main():
    finder = Finder()
    u1 = User("Artak", "Melkonyan", "PHD", "Lecturer", "University")
    u2 = User("Armen", "Hakobyan", "Masters", "Lecturer", "University")
    u3 = User("Lusine", "Melkonyan", "MBA", "Lecturer", "University")
    u4 = User("Artak", "Levonyan", "PHD", "Lecturer", "University")
    finder.append(u1)
    finder.append(u2)
    finder.append(u3)
    finder.append(u4)
    finder.findmatches()
main()


