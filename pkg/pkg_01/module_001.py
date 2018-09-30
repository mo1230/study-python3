"""
定义两个类，Person类  Teacher类
函数： say()

"""

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_money(self):
        print("i will make money")

class Teacher(Person):
    """
    继承于类Person
    """
    def __init__(self, name, age, high):
        self.__name = name
        self.__age = age

        self.high = high

    def test(self, work):
        print("i am testing because i am  {0}".format(work))
        super().make_money()

# 如果该模块作为主进程运行，则以下代码可被执行
if __name__ == '__main__':
    # 用户输入
    name = input("your name: ")
    age = input("age: ")
    high = input("high: ")
    work = input("your jobs: ")

    lady = Teacher(name, age, high)

    lady.test(work)
