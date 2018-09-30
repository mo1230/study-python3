### 模块
- 一个包含python代码的文件，可以调用这个模块
- 分工合作，将有一定功能的代码放在一个文件下
- 规范
    -函数
    - 类
    - 测试代码，方便别人引用你的模块时用测试代码进行测试代码的正确性
- 如何使用模块
    - 模块直接导入
            
            import moudle_name
    
            module_name.var   #调用另一个模块的变量
    
    - 模块文件名称尽量不要直接以数字命名，如果要用数字命名，需要使用：
    
            import importlib
        
            module1 = importlib.import_module("模块名")
        
            module1.var  # 调用模块的变量
            
     - 使用别名
            
            import module as m1
            
     - 只导入部分
            
            from module import name
            
     - 调用模块时，部分代码不执行，只有当该模块作为主进程运行时，该代码执行
            
            # 如果该模块作为主进程执行时，以下代码才执行
            if __name__ == "__main__":
                代码
                ...
                
                
- 模块的搜索路径
    - 即加载模块时，系统怎样找到模块
    - 怎样查看与添加
        - 查看
        
                import sys
                for p in sys.path:
                    print(p)
                    
         - 添加
         
                sys.path.append(路径)
    - 加载顺序
        1. 内存中已经加载好的模块
        2. python的内置模块
        3. sys.path路径
        
        
### 包
- 包简单来说就是文件夹
- 每个包，以及子包都要有一个__init__py模块，所以自定义包时要新建一个__init__.py
    - 直接导入包时,会直接调用__init__.py中的内容
        - form pkg import *
            - 这种方法也是调用的'__init__.py'
    - 导入包中的某个模块
    
            import pkg.module_name
            
            # 以下方法也可以           
            form pkg import module
            
    - 一般情况下__init__.py的内容为空，在__init__.py中设置‘__all__’的值，则导入包时就按照'__all__'的值加载包中指定的模块
            
            #在导入包时加载模块1和模块4,其他不导入
            __all__ = ["module1", "module4"]  