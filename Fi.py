class Person:
    def __init__(self, name, lastname, age, ID, mail):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.ID = ID
        self.mail = mail

def main():
    p1 = Person("Marianna", "Yessayan", "18", "12345678", "mail")
    print "Name:", p1.name, " Lastname:", p1.lastname, " Age:",  p1.age, " ID:",  p1.ID, p1.mail, "mail:"
    p2 = Person("Satenik", "Tovmasyan", "20", "34129876")
    print "Name:", p2.name, "Lastname:", p2.lastname, "Age:", p2.age, "ID:", p2.ID, p.mail, "mail:"
main()