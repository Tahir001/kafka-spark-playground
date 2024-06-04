# Hi this is a comment
class Human(object):

    def __init__(self, name:str, age:int, occupation:str, alive=True, health=100) -> None:
        self.name = name
        self.age = age
        self.occupation = occupation
        self.alive = alive
        self.health = health

    def say_hi(self) -> str:
        return "Hello!"

    def say_bye(self) -> str:
        return "Bye bye!"

    def introduce_yourself(self) -> str:
        return "Hello my name is {} and I am {} years old, and I do {}".format(self.name, self.age, self.occupation)

    def its_my_birthday(self) -> None:
        self.age += 1
        print("Its my Birthday!!")

    def check_health(self) -> None:
        print(f"I am {self.health}% healthy!")

Tahir = Human(name="Tahir", age=27, occupation="Engineer", health=95)
print(Tahir.say_hi())
print(Tahir.introduce_yourself())
Tahir.its_my_birthday()
Tahir.check_health()
print(Tahir.say_bye())
