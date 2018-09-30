# 定义一个Student类

# 定义一个函数

class Student():

    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("hello, i am {0}".format(self.name))

def running():

    print("i am running")

# 如果该模块作为主进程运行，则以下代码可以执行
if __name__ == "__main__":
    print("=" * 40)
    print("module_01")
