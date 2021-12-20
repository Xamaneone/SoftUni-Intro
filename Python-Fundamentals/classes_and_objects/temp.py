def say_hi(from_name):
    print(f"Saying hi, my name is {from_name}")

say_hi("Jordan")

class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print(f"Saying hi, my name is {self.name}")

    def say_bye(self):
        print(f"Saying bye, my name is {self.name}")


jordan = Person("Jordan")
jordan.say_hi()
jordan.say_bye()


ivan = Person("Ivan")
ivan.say_hi()
ivan.say_bye()


