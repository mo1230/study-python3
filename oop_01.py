'''

以下的内容与类、对象有关

'''

class Student():
    name = None
    age = None

    def do_homework(self):
        print("i am doing homework !")

huanhuan = Student()

print(huanhuan.name)
print(huanhuan.age)

huanhuan.do_homework()

print("-" * 20)

huanhuan.name = input("what is your name:")
huanhuan.age = input("your ages:")

print(huanhuan.name.center(40, '-'))

