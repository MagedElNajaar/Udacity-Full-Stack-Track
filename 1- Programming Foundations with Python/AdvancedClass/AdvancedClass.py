class Parent():
    def __init__(self, last_name, eye_color):
        print("parent Constructor Called")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print("Last Name - "+self.last_name)
        print("Eye Color - "+self.eye_color)

class Chile(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print("Child Constructor Called")
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys

    def show_info(self):
        print("Last Name - "+self.last_name)
        print("Eye Color - "+self.eye_color)
        print("Number of Toys - "+str(self.number_of_toys))

billey_cyrus = Parent("Cyrus", "Blue")
billey_cyrus.show_info()
milley_cyrus = Chile("Cyrus", "Blue", 5)
milley_cyrus.show_info()
