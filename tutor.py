class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")

john = Person("smit patel")
print(john.name)
john.talk()

test = Person("this is test")
print(test.name)
test.talk()
