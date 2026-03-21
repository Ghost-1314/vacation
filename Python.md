# 字典（`dict`）
列表用`[]`，字典用`{}`
如果`{}`里没有`:`，则不是字典，而是**集合**
字典用于储存键值对——键：值，每一个键值对中间记得用 `,` 隔开
单独输出键值对可以用索引
获取某个键的值，字典名[键名]，注意：键的类型需是不能改变的，列表属于可变类型，就不能作为键，而字符串、整数、浮点数都可以
如果说要创建一个通讯录，通讯录里面存在同名的情况，要根据年龄等其他条件进行对电话号码的获取（键值对），这个时候不能够用列表因为列表可变，不能作为键，应该用[[元组]]
字典和列表一样都是可变的，所以可以添加和删除键值对
比如说如果要在通讯录里面添加某个人的电话号码：`字典名[键名]="18088888888"`
如果说添加的人在原通讯录已存在，那么进行的操作会覆盖原号码
如果要知道某个键是否存在：“键 in 字典名”会返回一个布尔类型，例如：`print("小明" in list)`
删除某个键值对，`del 字典名[键名]`，例如：`del list["小明"]`，但是如果键本身不存在的话就会报错
想知道字典里面有多少键值对，`len(字典名)`
字典有三个[[方法]]：`字典名.keys()`表示所有键；`字典名.values()`表示所有值；`字典名.items`表示所有键值对

# 字符串

- 对字符串进行所有操作字符串本身都不会改变，需要将操作后的结果赋值给新的变量
# `for`
结构：for 变量名 in 可迭代对象:
         对每个变量做的事情（变量会被依次赋值为可迭代对象中的各个值）

用for迭代字典时，for后面要有两个变量，变量被赋值为键和值组成的元组，把元组的第一个元素赋值给第一个变量，第二个元素赋值给第二个变量

用for循环print时，每一次print都会换行，因为print()中有个隐藏的参数end，默认值是"\n"，如果不想换行，可以在括号里第二个参数改变end的值。
# `range`
`range`用来表示整数序列，结构是：`range(数字,数字)`，第一个数字表示起始值，第二个数字表示结束值，左闭右开，可以在第二个数字后逗号隔开加第三个数字表示步长（跨度），不指明的时候默认为1。
如果`range`括号里只放入一个值，则默认起始值为0，结束值为放入的值

# `while`
结构：
```python
while 条件A:
     行动B
```
当条件A为True时执行行动B直到条件A为假
在条件何时结束未知的情况下（即循环次数未知的情况下），while比for好用，但是很多情况下两者可以相互转换


# `format`
结构：
内容`.format(替换对象1,替换对象2)`
替换对象可以是变量，根据内容里的从{0}、{1}......依次按顺序替换
也可以是指定替换对象，此时format括号里就没有顺序之别。例如内容中包含{user_year}
`format(user_name=year,替换对象2,...)`
format括号里，等号前面对应的是关键字，对应内容里花括号里面的关键字，等号后面是参数值

例如：
```python
year=1998
month=12
day=22
print("面包的生日是{0}年{1}月{2}日".format(year,month,day))
```
输出：
`面包的生日是1998年12月22日`

也可以是：
```python
print("面包的生日是{year}年{month}月{day}日".format(month=12,year=1998,day=22))
```
也会输出：
`面包的生日是1998年12月22日`

# f-字符串
在字符串前加前缀f，花括号里的内容会被直接求值并添加到字符串内

例如：
```python
year=1998
month=12
day=22
print(f"面包的生日是{year}年{month}月{day}日")
```
输出：
面包的生日是1998年12月22日

另外可以用“:.Xf”来表示保留几位小数
如：
```python
name="小云"
number=4.975
print(f"{name}的绩点是{number:.2f}")
```
会输出：
小云的绩点是4.97
（format也是如此）


# 函数
定义函数：
```python
def 函数名(参数...):
     内容
     return X
```
如果没写return，默认返回None，即返回空值


# 模块
模块是 Python 里 “功能包” 的概念
引入模块的方法：
1.完整导入（推荐）
例如：
import math
在后续使用时需要加模块名前缀，例如print(math.pi)

2.导入特定函数 / 常量
只导入需要的部分（多个用逗号隔开），使用时不用加模块名前缀
例如：
```python
from math import pi, sqrt
print(pi)
print(sqrt(16))
```

3.导入所有内容（不推荐）
容易和自己定义的变量 / 函数重名，导致冲突
例如：
```python
from math import *
print(pi)
```
如果要引入第三方模块（不是Python标准库里的模块），要先进行安装


# 类
和定义普通变量不同，Python在定义类名的过程中用的是Pascal风格特点是用首字母大写来分隔单词，例如：`UserAccount`
类有一个特殊的[[方法]]叫做构造函数，作用是定义实例对象的属性，它必须要被命名为`__init__`，注意前后各有两个下划线，括号里可以放任意数量的参数，但是第一个参数永远是被占用的，用于表示对象自身，叫做`self`，它能帮你把属性的值绑定到实例对象上，但是注意self并不需要我们手动传入。比如：`self.name="mimi"`。如果写成`name="mimi"`，Python会觉得只是在给普通变量`name`赋值，就不会把这个值看成对象的属性
`self.XXX`是对象的属性，在同一个类的不同方法中都可以被使用
示例：定义一个猫咪属性的类
```python
class CuteCat:
     def  __init__(self,cat_name,cat_age,cat_color):
        self.name=cat_name
        self.age=cat_age
        self.color=cat_color
cat1=CuteCat("mimi",2,"粉色")
print(f"小猫{cat1.name}的年龄是{cat1.age}岁，花色是{cat1.color}")
```

类除了可以定义属性，即“对象有什么性质”之外，还可以定义方法，即“对象能做什么”。
例如定义一个类，储存学生的名字和学号两个属性，定义两个方法用于设置语数英成绩以及打印各科成绩
代码如下：
```python
class Student:  
    def __init__(self, name, student_id):  
        self.name = name  
        self.student_id = student_id  
        self.score={"语文":0,"数学":0,"英语":0}  
    def set_score(self, course,score):  
        if course in self.score:  
            self.score[course]=score  
    def print_score(self):  
        print(f"学生{self.name}（学号{self.student_id}）的成绩为：")  
        for course in self.score:  
            print(f"{course}:{self.score[course]}分")  
huang=Student("面包",19981222)  
zhou=Student("周星星",19920929)  
huang.set_score("语文",99)  
huang.set_score("数学",98)  
huang.set_score("英语",99)  
zhou.set_score("语文",98)  
zhou.set_score("英语",99)  
huang.print_score()  
zhou.print_score()
```
输出：
学生面包（学号19981222）的成绩为：
语文:99分
数学:98分
英语:99分
学生周星星（学号19920929）的成绩为：
语文:98分
数学:0分
英语:99分


# 类继承
类继承即创建有层次的类，有子类和父类之分，子类会继承父类的属性和方法
例如：人类和猫咪都是哺乳类动物，都有两只眼睛，都会呼吸。但是人类会阅读，而猫咪会抓沙发
因此，可以创建一个哺乳类动物的类`mammal`，把共同属性挪进去，然后人类和猫咪继承这个类
具体写法是在类名后面加上括号，写上父类名字
如果子类自己没有构造函数，就会调用父类的构造函数，让实例具备父类的属性。调用方法时，优先看所属类有没有该方法，没有的话，往上找父类的同名方法用。
如果两个子类有不同的属性，例如人类和猫咪的`has_tail属性`不同，人类没有尾巴，猫咪有尾巴，就不能只写在父类里，但如果在子类里写`__init__方法`，那么创建子类实例时就会优先调用子类的构造函数，导致实例只有has_tail属性。而如果在子类`__init__方法`里把name，sex等属性写上，又会造成重复代码。
解决方法：在子类`__init__方法`里用`super方法`，`super`会返回当前类的父类，所以在子类的构造函数里写`super().__ init__()`，就会调用父类的构造函数，此时子类也会拥有父类的属性了。

什么时候用类继承？
当A和B两个东西可以说成A是B的时候，那么A就可以写成B的子类。
比如说：面包是歌手，那么面包就可以写成歌手的子类；新能源汽车是车，那么新能源汽车可以写成车的子类

示例：如果要写一个名为歌手的父类，包含面包和周星星和快乐小狗三个歌手，定义一些他们相同或不同的属性和方法。
代码如下：
```python
class singer:  
    def __init__(self, name,sex,birthday):  
        self.name = name  
        self.sex=sex  
        self.birthday=birthday  
    def singing(self):  
        print(self.name+"在唱歌")  
  
class huang(singer):  
    def __init__(self,name,sex,birthday):  
        super().__init__(name,sex,birthday)  
        self.has_Dolphin=True  
    def eat(self):  
        print(self.name+"今天在吃面包")  
  
class zhou(singer):  
    def __init__(self,name,sex,birthday):  
        super().__init__(name,sex,birthday)  
        self.has_Dolphin=True  
    def sleeping(self):  
        print(self.name+"今天在睡觉")  
  
class song(singer):  
    def __init__(self,name,sex,birthday):  
        super().__init__(name,sex,birthday)  
        self.has_Dolphin=False  
    def dance(self):  
        print(self.name+"今天在跳舞")  
  
xiaoyun=huang("面包","女","1998.12.22")  
shen=zhou("周星星","男","1992.09.29")  
yuqi=song("快乐小狗","女","1999.09.23")  
  
print(f"{xiaoyun.name}({xiaoyun.sex})的生日是{xiaoyun.birthday}")  
print(f"{xiaoyun.name}会唱海豚音吗？答案是{xiaoyun.has_Dolphin}")  
xiaoyun.eat()  
  
print(f"{shen.name}({shen.sex})的生日是{shen.birthday}")  
print(f"{shen.name}会唱海豚音吗？答案是{shen.has_Dolphin}")  
shen.sleeping()  
  
print(f"{yuqi.name}({yuqi.sex})的生日是{yuqi.birthday}")  
print(f"{yuqi.name}会唱海豚音吗？答案是{yuqi.has_Dolphin}")  
yuqi.dance()  
  
xiaoyun.singing()  
shen.singing()  
yuqi.singing()

输出：
面包(女)的生日是1998.12.22
面包会唱海豚音吗？答案是True
面包今天在吃面包
周星星(男)的生日是1992.09.29
周星星会唱海豚音吗？答案是True
周星星今天在睡觉
快乐小狗(女)的生日是1999.09.23
快乐小狗会唱海豚音吗？答案是False
快乐小狗今天在跳舞
面包在唱歌
周星星在唱歌
快乐小狗在唱歌
```

# 文件操作
相对路径和绝对路径，Windows用\进行分隔
用`open()函数`对文件进行打开
模式（第二个参数）：
模式是一个字符串，常见的模式包括：
"r"：读取模式（只读）
"w"：写入模式（只写）
模式也可以不写，默认为读取模式
在读取模式下，如果找不到你传入的文件名，就会报错，提示文件不存在
`open()函数`还有个可选参数叫encoding，表示编码方式现在文件的编码方式一般都是utf-8

若`open()函数`执行成功，会返回一个文件对象，我们可以后续对它进行读取或写入操作。
针对读文件，文件对象有个`read()方法`，调用后会一次性读取文件里面的所有内容，并以字符串形式进行返回。
注意：如果调用完`read()`后再次调用，返回的结果为空，因为程序会记录文件读到哪个位置了。第一次读取已经读到末尾，第二次读取后面已经没有内容了，所以返回空字符串。
在文件很大的情况下最好不要用`read()`，因为读出来的内容会占用很大内存。若不想一次性读完整个文件，可以给read传一个数字表示读多少字节。
例如：
```python
f=open(".\data.txt","r",encoding="utf-8")
print(f.read(10))
print(f.read(10))
```
第一次调用`read()`时读取1~10个字节的文件内容，第二次调用时读取11~20个字节的文件内容

读文件的方法：
`read`：返回全部文件内容的字符串
`readline`：返回一行文件内容的字符串
`readlines`：返回全部文件内容组成的列表

关闭文件：
文件对象有一个叫做close的方法，调用后该文件对象就会释放系统资源，每次完成读写文件操作后都应该关闭文件。
例如：
```python
f=open(".\data.txt","r",encoding="utf-8")
print(f.read())
f.close()
```
有时我们会忘记调用close，另一种方法是用with关键字。with后面跟上open函数的调用，as，后面跟上文件对象的命名，冒号，缩进放上对文件的操作。这样在缩进的内容执行完毕后文件会被自动关闭。
例如：
```python
with open(".\data.txt","r",encoding="utf-8") as f:
     print(f.read())
```

写文件：
打开文件，第二个参数用"w"。
在读文件时，如果传入的文件名不存在，系统会报错，但是写文件不存在此情况。当传入的文件名不存在时，系统会自动创建一个名为传入文件名的文件。
注意：如果用"w"打开文件进行写入，如果文件存在，原本的文件内容会被清空。
针对写文件，文件对象有个write方法。
例如：
```python
with open("./data.txt","w",encoding="utf-8") as f:
     f.write("Hello! 面包")
```

此时文件data.txt里就会出现一句"Hello! 面包"
但是如果再调用一次write，写入文件时并不会自动换行，写入的内容会跟在上一次写入的内容后面。如果要换行，需要自己手动加上换行符。
如：
```python
with open("./data.txt","w",encoding="utf-8") as f:
     f.write("Hello! 面包\n")
     f.write("Hello! 深深\n")
     f.write("Hello! 雨琦\n")
```

如果在写文件时不想清空原内容，只想在后面追加内容，不能使用"w"作为模式参数，而是应该用"a"表示附加内容，而不是清空重写。
注意："a"也不会自动换行，需要自己手动加上换行符。并且若传入的文件名不存在，会直接创建一个名为传入文件名的新文件，和"w"一样。另外，无论是"w"模式还是"a"模式，都无法读取文件里原本的内容，如果直接调用read，程序会报错。如果需要先读取文件再进行写入的话，需要在"a"模式后面加一个加号，就可以同时支持读写文件，此时打开文件后调用read和write都不会报错了。并且调用write后，会在文件后面追加新内容，而不会清空原文件。也可以用"r+"，但是要先读取再写入，才会变成追加模式，否则光标会在最前面覆盖原内容。
如：
```python
with open("./data.txt","a+",encoding="utf-8") as f:
     f.write("Hello! 深深\n")
     f.write("Hello! 雨琦\n")
```

# 异常处理
针对程序炸，也就是程序报错，可能是写的代码有问题，也可能是用户输入的数据不符合要求，比如说要求输入整数，用户却输入字符串。当程序在某一行报错后，后面的程序都不会被运行。所以我们需要对程序进行预判和捕捉错误。
错误类型：
IndexRrror(索引错误)
ZeroDivisionError(除零错误)
FileNotFoundError(找不到文件错误)
TypeError(类型错误)
……
我们可以通过`try/except`来捕捉异常。
`try`，冒号，换行缩进后放上感觉可能会报错的代码；接着在except后面，跟上想捕捉的错误类型名字，冒号，换行缩进后放上指定类型错误发生后想相应执行的操作。
例如一个计算身体BMI的程序：
```python
try: 
    user_weight = float(input("请输入您的体重（单位：kg）：")) 
    user_height = float(input("请输入您的身高（单位：m）：")) 
    user_BMI = user_weight / user_height ** 2 
except ValueError: 
    print("输入不为合理数字，请重新运行程序，并输入正确的数字。")
except ZeroDivisionError: 
    print("身高不能为零，请重新运行程序，并输入正确的数字。")
```
但是有时候我们并不能预判错误类型。如果希望程序无论出现什么类型的错误时都不要炸，直接写except，会捕捉所有错误类型。
注意：try/except语句在捕捉错误类型时从上往下运行，若第一个except就捕捉到了对应错误，那后面的except语句都不会执行了，即只有第一个符合条件的分支会运行。

在except后面还可以再跟上两个语句，分别是else和finally。
else，冒号，缩进，放上当try 里面的语句没有任何错误时要执行的语句。
finally，冒号，缩进，放上无论错误发生与否都会被执行的语句。无论如何finally里面的代码最终都会被执行。
例如在以上BMI程序中进行改进：
```python
try: 
    user_weight = float(input("请输入您的体重（单位：kg）：")) 
    user_height = float(input("请输入您的身高（单位：m）：")) 
    user_BMI = user_weight / user_height ** 2 
except ValueError: 
    print("输入不为合理数字，请重新运行程序，并输入正确的数字。") 
except ZeroDivisionError: 
    print("身高不能为零，请重新运行程序，并输入正确的数字。") 
except: 
    print("发生了未知错误，请重新运行程序。") 
else: print("您的BMI值为：" + str(user_BMI)) 
finally: 
    print("程序结束运行。")
```


# 测试
`assert`语句：
`assert`后面可以跟上任何布尔表达式（值为True或False）。测试时，我们在`assert`后面跟上我们认为应该True的表达式。如果assert后面的表达式最终结果为True，则无事发生，继续运行后面的代码。但如果求值出来为False，就会产生"AssertionError"（断言错误）。
例如：
```python
assert len("Hi") == 2 
assert 1 + 2 > 6 
assert "a" in ["b","c"]
```

但是一旦出现断言错误，程序直接终止，后面的代码不会再被运行，所以并不能知道剩下的代码里有哪些问题。

为了解决上述问题，一般我们会使用专门做测试的库，它们能一次性跑多个测试用例，并且能直观地展示哪些测试用例通过了，哪些没有。
unittest便是一个很常用的Python单元测试库。单元测试，即对软件中的最小可测试单元进行验证，比如验证某函数某方面表现是否符合预期。unittest库是Python自带的，不需要额外安装。

另外，一般把测试代码放到独立文件里，而不是与要测试的功能混在一起，这样能更清晰地划分实现代码和测试代码。
为了要调用测试的功能，要在测试文件里，把要测试的函数或类引入进来。如果测试文件和被测试文件位于同一文件夹下，引入的语法：
import unittest
from 文件名 import 函数名/类名

接下来就可以正式写测试了。创建一个类，名字可以以Test开头，表明这是一个用来测试的类，这个类要是unittest.TestCase的子类，这样就可以使用那些继承自unittest.TestCase的各种测试功能。（unittest是一个库，TestCase是里面自带的一个类，创建它的子类以便用它的属性和方法）
在这个类下面，可以定义不同的测试用例，每一个测试用例都是类下面的一个[[方法]]，名字必须以“test_”开头，因为unittest这个库会自动搜索以“test_”开头的方法，并且只把“test_”开头的当成测试用例。
如果我们要写一个程序用于验证两个值是否相等，写测试我们会用`assert`。但是由于出现"AssertionError"时程序会中断，所以我们可以用unittest库里的TestCase类的assertEqual方法（用于验证两个值是否相等）。由于测试类已经继承自unittest.TestCase，所以可以直接通过self调用父类方法。传入的第一个参数和第二个参数如果相等，显示测试通过，否则显示测试不通过，但程序也不会炸。

写好测试用例后，只需在编辑器的终端（Alt+F12），输入“python -m unittest”，表示运行unittest，这个库就会自动搜寻所有继承了unittest库里TestCase类的子类，运行它们所有以“test_”开头的方法，然后展示测试结果。它会告诉你共运行了几个测试，上方的每个“·”都代表一个测试通过。如果其中有一个测试没有通过，其中有一个“·”就会变成“F”。unittest还会详细告诉你是哪个文件下面的哪个方法造成了测试失败以及为什么失败，一体化提供所有和测试结果有关的信息。

eg：
实现代码（my_calculator.py）：
```python
def my_adder(x, y): 
    return x + y
```


测试代码（test_my_calculator.py）：
```python
import unittest 
from my_calculator import my_adder 
class TestMyAdder(unittest.TestCase): 
    def test_positive_with_positive(self): 
        self.assertEqual(my_adder(5, 3), 8) 
    def test_negative_with_positive(self): 
        ...
```

# `set`

#### 作用
1. 快速去重
2. 高效判断元素是否存在：
     - 判断一个元素是否在容器中时，`x in set` 比 `x in list` 快得多（尤其是数据量大时）
     - list 判断是**顺序遍历**，数据越多越慢；
     - set 判断是**哈希查找**，无论数据量多大，耗时基本固定。
3. 便捷的集合运算：直接支持数学中的**交集、并集、差集、对称差集**，不用手动写循环对比，适合处理两个数据集的关系（比如找共同元素、找独有元素）。


#### 特征

1. **无序
2. **无重复
3. **元素不可变：集合中的元素必须是**可哈希对象（比如数字、字符串、元组），不能放列表、字典、集合（这些是不可哈希的），否则会报错；
4. **可变
5. 返回一个**集合

# `replace`

-  语法：`字符串.replace(A,B,C)`，A，B，C是三个参数，表示用B替换字符串里的A。C表示替换个数，可以不写，不写时默认替换所有。

# 切片（`slicing`）

- 切片操作：语法：`序列[起始索引:结束索引:步长]`，默认步长1.
- 左闭右开
- 步长为负数时，表示从右往左截取

```python
s = "abcdefgh" 
lst = [10,20,30,40,50,60]

print(s[:4]) # 输出：abcd（从0到4，取0-3） 
print(lst[:3]) # 输出：[10,20,30]（从0到3，取0-2）

print(s[5:]) # 输出：fgh（从5到末尾，取5-7） 
print(lst[2:]) # 输出：[30,40,50,60]（从2到末尾，取2-5）

print(s[2:6]) # 输出：cdef（取2、3、4、5） 
print(lst[1:4])# 输出：[20,30,40]（取1、2、3）

print(s[:]) # 输出：abcdefgh（复制整个字符串） 
print(lst[:]) # 输出：[10,20,30,40,50,60]（复制整个列表）

print(s[10:20])# 输出：""（空字符串，超出范围，无元素可取） 
print(lst[8:]) # 输出：[]（空列表，超出范围） print(s[:100]) # 输出：abcdefgh（自动到末尾）

print(s[::2]) # 输出：aceg（0,2,4,6） 
print(lst[1:5:2])# 输出：[20,40]
print(s[0:7:3]) # 输出：adg（0,3,6） 
print(lst[::3]) # 输出：[10,40]（0,3）

print(s[::-1]) # 输出：hgfedcba
print(lst[::-1]) # 输出：[60,50,40,30,20,10]（列表反转）

print(s[::-2]) # 输出：hfdb（7,5,3,1） # 起始=6，结束=1，步长=-2：从索引6(g)到1(b)，反向跳2步（6→4→2） 
print(s[6:1:-2]) # 输出：gec
```

# 元组（`tuple`）

- 用`()`
- 不可变
- 支持**索引**和**切片**（语法和列表、字符串一直）一致
- 元素类型可混合（数字、字符串、列表等）
- 常用于存储不修改的数据


# 集合

- 无序
- 不支持切片和索引
- 可以用`list(集合)`将集合转成列表，就可以进行切片和索引

# `strip`

- 删除字符串首尾的符号
- `str.strip()` 的默认参数为 `None`，删除字符串首尾的所有空白字符（包括空格、制表符 `\t`、换行符 `\n`、回车符 `\r` 等），而不仅仅是空格。
- 如果传入了 `chars` 参数，则会移除首尾在 `chars` **集合**中的字符，且不会修改原字符串，而是返回一个新字符串。
- 括号里可以写多个字符，写字符串的话会被**拆分**成多个单个字符，然后在首尾进行删除
- 只要首尾有字符在所写的集合里，都会被删除
- 只删首尾
- `t.strip(要删的字符)`，t是字符串
- 括号里面没内容时默认删除首尾空白字符
- 返回新字符串。原字符串不变，因为不可变

# `append`、`extend`

- 共性
    - 都是**列表**（list）中的专属内置方法
	- 都是直接修改原列表，返回值为**None
	- 往末尾添加

- 区别
- append:
	- `列表名.append(元素)`
	- 参数可以是**任意类型的值**（数字、字符串、列表、字典等）
	- 添加单个元素（无论参数是单个值还是一个列表 / 元组，都会被当作**一个整体元素**添加到列表末尾）
	- 等价替代：`lst = lst + [元素]`（生成新列表）

- extend:
	- `列表名.extend(可迭代对象)`
	- 参数必须是**可迭代对象**（列表、字符串、元组、集合、字典等）
	- 添加 “可迭代对象的所有元素”（会把参数（可迭代对象）里的元素**逐个拆解**，依次添加到列表末尾）
	- 等价替代：`lst = lst + 可迭代对象`（生成新列表）

总结
- `append()` 是 “追加单个元素”，参数可以是任意值，哪怕是列表 / 元组，也会被当作一个元素；
- `extend()` 是 “批量追加元素”，参数必须是可迭代对象，会把对象里的元素逐个添加；
- 两者都修改原列表、返回 `None`（不要用 `new_lst = lst.append(...)`）。

# 列表推导式

概念：
- 列表推导式的核心是**用一行代码完成列表的创建和元素处理**，它把循环、条件判断和元素生成整合在一起，语法更简洁，执行效率也更高。


基本语法
- 基础格式：`[表达式 for 变量 in 可迭代对象]`
- 带条件过滤的格式：`[表达式 for 变量 in 可迭代对象 if 条件]`


示例（对比传统写法）
比如要创建一个包含 1-5 平方的列表：

```python
# 传统for循环写法 
squares = [] 
for i in range(1, 6): 
	squares.append(i **2) 
print(squares) # 输出: [1, 4, 9, 16, 25] 

# 列表推导式写法 
squares = [i** 2 for i in range(1, 6)] 
print(squares) # 输出: [1, 4, 9, 16, 25]
```


# `lambda`（匿名函数）

- 匿名，简化版的临时函数
- 没有正式的函数名
- 适合定义简单、只用一次的小功能
- 不用像`def`那样写完整的函数结构
- 临时使用、用完即弃
- 一般`lambda`都写在 `sort()`/`map()`/`filter()` 等函数的参数括号里，作为临时规则使用，而不会单独写出来并赋值给变量。（不如`def`）

1. 语法：`lambda 参数列表: 表达式`
	- **lambda**：定义匿名函数的关键字（类似`def`）；
	- **参数列表**：可以是 0 个、1 个或多个参数（和普通函数一样）；
	- **:**  ：分隔参数和表达式；
	- **表达式**：只能有**一个**（不能写多行代码、循环、if-else 块，但可以写三元表达式），表达式的结果就是这个匿名函数的**返回值**（不用写`return`）。 
	- 相比普通函数，不用写函数名和return。

2. 示例
- 无参
	```python
	# 无参数，返回固定字符串 
	hello = lambda: "Hello, Python!" 
	print(hello()) # 输出: Hello, Python! 
	
	# 无参数，返回计算结果 
	get_pi = lambda: 3.1415926 
	print(get_pi()) # 输出: 3.1415926
	```
	
- 单参
	```python
	# 计算一个数的平方 
	square = lambda x: x **2 
	print(square(5)) # 输出: 25 
	
	# 把字符串转成大写 
	to_upper = lambda s: s.upper() 
	print(to_upper("hello")) # 输出: HELLO
	```


- 多参
```python
# 计算三个数的平均值 
avg = lambda a, b, c: (a + b + c) / 3 
print(avg(1, 2, 3)) # 输出: 2.0 

# 拼接两个字符串（带分隔符） 
join_str = lambda s1, s2, sep: s1 + sep + s2 
print(join_str("Hello", "World", "-")) # 输出: Hello-World
```


- 带三元表达式
```python
# 判断一个数是奇数还是偶数 
check_odd_even = lambda x: "偶数" if x % 2 == 0 else "奇数" print(check_odd_even(6)) # 输出: 偶数 
print(check_odd_even(7)) # 输出: 奇数 

# 取两个数中的较大值 
max_num = lambda a, b: a if a > b else b 
print(max_num(10, 20)) # 输出: 20
```


- 配合内置函数使用

	- 列表按自定义规则排序。比如对列表里的元组，按元组的第二个元素排序：
	```python
	# 原始列表：[(姓名, 年龄), ...] 
	people = [("小明", 18), ("小红", 16), ("小李", 20)] 
	
	# 按年龄升序排序（用lambda指定排序依据：元组的第二个元素） 
	people.sort(key=lambda x: x[1]) 
	print(people) # 输出: [('小红', 16), ('小明', 18), ('小李', 20)]
	```


	- 用 map () 批量处理列表元素。`map(函数, 可迭代对象)` 会把函数应用到每个元素上，用 lambda 不用单独定义函数：
	```python
	# 把列表里的每个数乘以2 
	nums = [1, 2, 3, 4] 
	new_nums = list(map(lambda x: x * 2, nums)) 
	print(new_nums) # 输出: [2, 4, 6, 8]
	```


	- 用 filter () 过滤列表元素：`filter(函数, 可迭代对象)` 会筛选出满足条件的元素，lambda 定义过滤规则：
	```python
	# 筛选出列表里的偶数 
	nums = [1, 2, 3, 4, 5, 6] 
	even_nums = list(filter(lambda x: x % 2 == 0, nums)) 
	print(even_nums) # 输出: [2, 4, 6]
	```


# `map`

- `map(function, iterable, ...)`
- 函数和可迭代参数对象必须有

|     参数     | 要求/说明                                                     |
| :--------: | --------------------------------------------------------- |
| `function` | 必选，要应用到每个元素的函数（可以是 Python 内置函数、自定义普通函数，不能省略）              |
| `iterable` | 必选，可迭代对象（列表、元组、字符串、集合、字典等）                                |
|    ...     | 可选，多个可迭代对象（数量必须和 `function` 的参数个数匹配）                      |
|    返回值     | `map` 对象（迭代器），**需用 `list()`/`tuple()` 等转换为列表 / 元组才能查看结果** |

总结：
- `map()` 核心语法：`map(函数, 可迭代对象[, 多个可迭代对象])`，返回 map 迭代器；
- 多个可迭代对象的参数数量，必须和函数的参数个数匹配；
- 关键：返回的迭代器需用 `list()`/`tuple()` 转换才能查看具体结果。


# `filter`

- **按指定规则过滤可迭代对象中的元素**，只保留符合条件的元素，返回一个迭代器
- 语法：`filter(function, iterable)`

|     参数     |                                                                    要求/说明                                                                     |
| :--------: | :------------------------------------------------------------------------------------------------------------------------------------------: |
| `funtion`  | 可选（可以传 `None`），用于判断的函数：<br><br>✅ 传函数时：函数返回 `True`/`False`，`filter` 保留返回 `True` 的元素；<br><br>✅ 传 `None` 时：默认判断元素本身是否为 `True`（非空 / 非 0 即 True）。 |
| `iterable` |                                                         必选，要过滤的可迭代对象（列表、元组、字符串、集合等）。                                                         |
|    返回值     |                                              `filter` 对象（迭代器），需用 `list()`/`tuple()` 转换才能看到具体结果。                                              |

示例：
- 过滤出列表中的偶数
```python
# 第一步：定义判断函数（返回True/False） 
def is_even(x): 
	# 判断x是否是偶数，是则返回True，否则返回False 
	return x % 2 == 0 
	
# 第二步：准备要过滤的可迭代对象（列表） 
nums = [1, 2, 3, 4, 5, 6] 

# 第三步：用filter过滤——只保留is_even返回True的元素 
result = filter(is_even, nums) 

# 第四步：转换为列表查看结果（和map一样，迭代器需转换） 
print(list(result)) # 输出: [2, 4, 6]
```


- 传`None`，过滤**空值/0值**，保留本身为`Ture`的元素，（非空字符串、非 0 数字、非空列表等）
```python
# 要过滤的列表（包含0、空字符串、None、非0数字、非空字符串） 
mixed = [0, "", None, 5, "hello", [], 8] 

# 传None，过滤掉“为False”的元素 
result = filter(None, mixed) 

print(list(result)) # 输出: [5, 'hello', 8]
```


```python
nums = [1, 2, 3, 4, 5, 6] 
# lambda x: x>3 → 判断x是否大于3，返回True/False 
result = filter(lambda x: x > 3, nums) 

print(list(result)) # 输出: [4, 5, 6]
```


总结：
- `filter()`用于过滤元素，筛选符合要求的元素（`Ture`的元素）
- 和`map()`一样，返回的是迭代器，最后需用 `list()`/`tuple()` 转换才能看到具体结果


# `isdigit()`

- `isdigit()` 是字符串的内置方法，**只有当字符串全部由数字组成时返回`True`**，否则返回`False`
- 语法：`字符串.isdigit()`
- **注意**：如果字符串是负数字符串，如`"-123"`，也会返回`False`


# `NumPy`库


`import numpy as np`

- `np.arange()`
	- 语法：`np.arange(start, stop, step, dtype=None)`
	- `np.arange()` 的作用是生成一个**一维的、连续的数值序列数组**
	- 左闭右开
	- 常见写法：`np.arange(stop)`、`np.arange(start, stop)`、`np.arange(start, stop, step)`

|   参数    | 是否可选 |             含义             |  默认值   |
| :-----: | :--: | :------------------------: | :----: |
| `start` |  可选  |         序列的**起始值**         |   0    |
| `stop`  |  必选  |   序列的**终止值**（⚠️ 不包含在结果里）   |   无    |
| `step`  |  可选  |   序列中数值的**步长**（相邻两个数的差值）   |   1    |
| `dtype` |  可选  | 生成数组的数据类型（如 int32、float64） | `None` |

---

- `reshape()`
	- 作用：在不改变数组元素和元素顺序及个数的前提下，调整数组的维度 / 形状
	- 新形状的元素个数必须**等于**原数组的形状个数，否则会报错
	- 可以直接更改形状。例如原数组是3×4，可以：`新数组=原数组.reshape((4,3))`
	- 语法：
		- `新数组 = 原数组.reshape(形状参数)`
		- `新数组 = np.reshape(原数组, 形状参数)`
	- 形状参数格式：
		- 二维：`(行,列)`
		- 三维：`(深/页,行,列)`
	- `-1`的用法：
		- 用于自动计算**某一**维度(**注意**：一次`reshape`只能用一次`-1`，因为一次只能计算一个维度)
		- 用于展平多维数组：`新数组=原数组.reshape(-1)`


		```python
		import numpy as np 
		
		# 原数组：0-11（24个元素） 
		arr = np.arange(24) 
		
		# 已知列数=4，自动算行数（24÷4=6） 
		arr_2d_1 = arr.reshape(-1, 4) 
		print("指定列数，自动算行数：", arr_2d_1.shape) # (6, 4) 
		
		# 已知行数=3、列数=4，自动算页数（24÷3÷4=2） 
		arr_3d_1 = arr.reshape(-1, 3, 4) 
		print("指定行列，自动算页数：", arr_3d_1.shape) # (2, 3, 4)
		```

---

- `np.array()`：
`np.array()`是Python的`numpy`库提供的**多维数组对象**，可以理解成一个“升级版的列表”—— 专门用来高效存储和操作数值型数据（整数、浮点数等），是科学计算、数据分析、绘图的核心数据结构。


`np.array()`和普通列表的区别：

|  特性   |    普通Python列表     |    `np.array()`    |
| :---: | :---------------: | :----------------: |
| 数据类型  | 可混合（int/str/list） |     必须统一（仅数值型）     |
| 批量运算  |       需手动循环       |    支持直接运算（向量化）     |
| 维度支持  |     嵌套列表（不直观）     |  原生支持一维 / 二维 / 多维  |
|  速度   |         慢         |         快          |
| 绘图适配性 |     部分支持但效率低      | `matplotlib`首选数据格式 |

示例：
- 运算方式：支持 “向量化运算”，无需手动循环（最核心区别）
```python
import numpy as np 

# 普通列表：批量运算必须写循环/列表推导式 
lst = [1, 2, 3, 4] 
lst_plus_2 = [x + 2 for x in lst] # [3,4,5,6] 
lst_multiply_3 = [x * 3 for x in lst] # [3,6,9,12] 


# numpy array：直接运算，无需循环 
arr = np.array([1, 2, 3, 4]) 
arr_plus_2 = arr + 2 # array([3,4,5,6]) 
arr_multiply_3 = arr * 3 # array([3,6,9,12]) 
arr_square = arr **2 # array([1,4,9,16]) 
arr_sin = np.sin(arr) # 直接对每个元素求正弦值
```


- 维度操作：原生支持多维数组，且操作更便捷
```python
import numpy as np 

# 普通列表模拟二维 
lst_2d = [[1, 2, 3], [4, 5, 6]] 
# 想转置（行变列），需要手动写循环，非常麻烦 
lst_transpose = [[row[i] for row in lst_2d] for i in range(3)] # [[1,4],[2,5],[3,6]] 

# numpy array二维操作 
arr_2d = np.array([[1, 2, 3], [4, 5, 6]]) 
arr_transpose = arr_2d.T # 直接用.T转置，array([[1,4],[2,5],[3,6]]) 
arr_flatten = arr_2d.flatten() # 快速降维为一维：array([1,2,3,4,5,6]) 
arr_reshape = arr_2d.reshape(3, 2) # 重塑维度为3行2列：array([[1,2],[3,4],[5,6]])
```


- 内存与速度：更节省内存，运算速度远超列表
```python
import numpy as np 
import time 

# 生成100万个数据 
size = 1000000 
lst = list(range(size)) 
arr = np.array(lst) 

# 列表计算平方（列表推导式） 
start = time.time() 
lst_square = [x**2 for x in lst] 
print(f"列表耗时：{time.time() - start:.4f}秒") # 约0.08秒（视电脑配置） 

# array计算平方（向量化） 
start = time.time() 
arr_square = arr**2 
print(f"array耗时：{time.time() - start:.4f}秒") # 约0.001秒，快80倍以上
```


- 内置数值计算功能：自带统计 / 数学方法
```python
import numpy as np 

arr = np.array([1, 2, 3, 4, 5]) 
lst = [1, 2, 3, 4, 5] 

# 列表：仅支持基础统计 
print(sum(lst)) # 15（求和） 
print(max(lst)) # 5（最大值） 
# 想算均值/标准差，需要手动写公式或用额外库 
lst_mean = sum(lst) / len(lst) # 3.0 

# array：内置丰富统计方法 
print(arr.sum()) # 15（求和） 
print(arr.mean()) # 3.0（均值） 
print(arr.std()) # 1.4142（标准差） 
print(arr.max()) # 5（最大值） 
print(arr.min()) # 1（最小值） 
print(arr.argmax()) # 4（最大值的索引）
```


- 索引 / 切片：支持更灵活的 “花式索引”
```python
import numpy as np 

arr = np.array([1, 2, 3, 4, 5, 6]) 
lst = [1, 2, 3, 4, 5, 6] 

# 普通列表：仅基础索引/切片 
print(lst[2:5]) # [3,4,5] 

# array：花式索引 
# 1. 布尔索引：筛选大于3的元素 
mask = arr > 3 
print(arr[mask]) # array([4,5,6]) 

# 2. 整数数组索引：取索引1、3、5的元素 
print(arr[[1, 3, 5]]) # array([2,4,6]) 

# 3. 二维array的行列切片（绘图时选数据常用） 
arr_2d = np.array([[1,2],[3,4],[5,6]]) 
print(arr_2d[:, 1]) # 取所有行的第2列：array([2,4,6])
```

总结：
- `array`除了类型统一，核心优势是**向量化运算、高效的多维操作、更快的速度和更丰富的数值功能**，这也是绘图 / 数据分析优先用它的原因；
- 列表适合 “通用存储”（比如存不同类型的数据），而`array`适合 “数值计算”（比如绘图时生成数据、批量计算坐标）；
- 记住用`np.array()`/`np.linspace()`生成数据，既能简化代码，又能提升效率。

---

数组属性：
- `shape`：数组的**形状 / 维度大小**（元组），比如 `(2,3)` 表示 2 行 3 列；
- `dtype`：数组元素的**数据类型**（`int64`（默认整数）、`float64`（默认浮点数）、`str_`（字符串）等），决定元素的存储格式；
- `ndim`：数组的**维度数**（整数），比如 1 = 一维、2 = 二维、3 = 三维。

**注意**：`shape`返回的是元组而不是单纯的数字，故展平后，对于**一维数组**，维度数是 1，所以需要表示成 “只有 1 个元素的元组”，而 Python 中定义单元素元组必须加逗号 ——例如：`(24)` 会被识别成整数 24，`(24,)` 才是真正的单元素元组。

---
其它：
- `tolist()`:`numpy`库中数组对象的方法，核心是把`numpy`数组转换成`Python`原生列表的方法，**转换后可以使用`Python`列表的所有原生操作**

	语法：`numpy_array.tolist()`
	返回值：`Python`原生列表

---
- `np.linalg.norm()`： 是 `NumPy` 库中用于计算向量 / 矩阵的范数（`Norm`） 的核心函数。范数可以简单理解为向量的模或是矩阵的大小。
- `x`必须是`NumPy`数组 / 可转数组的序列（如列表），输入非数组会报错。

---
- `item()`：核心作用是把单元素的数组 / 标量对象转换成 Python 原生的标量（比如 `int、float`），而非列表 / 数组。
- 语法：`numpy_array.item(index)`
- 仅能对包含且仅包含一个元素的 `NumPy` 数组（或 `pandas` 标量）调用；如果数组有多个元素，直接调用会报错
- `index`为可选参数，单元素数组可省略；若数组是多维单元素（如 [[5]]），也可通过索引（如 `item(0)`）提取。
- 返回值是`Python`原生的标量类型

---
- `np.linalg.det()`:是`NumPy`库中用于计算方阵的行列式的核心函数，常用于判断矩阵是否可逆、求解线性方程组等场景。
- 语法：`np.linalg.det(a)`
- `a`：必填，输入的方阵（`NumPy`数组 / 可转换为方阵的序列，如列表）；非方阵会报错；仅用于计算方阵
- 行列式返回值为浮点型，值为 0 表示矩阵不可逆，非 0 表示可逆

---
- `np.linalg.matrix_rank()`：是`NumPy`库中用于计算矩阵秩（Matrix Rank） 的核心函数
- 语法：`np.linalg.matrix_rank(M, tol=None, hermitian=False)`
- `M`必填，输入的矩阵（`NumPy`数组 / 可转换为矩阵的序列，如嵌套列表），支持非方阵
- `tol`，可选，秩计算的容差阈值（浮点精度控制）不指定时，NumPy 自动计算阈值；手动指定（如 1e-9）可控制 “是否将极小值视为 0”。默认值`None`
- `hermitian`，可选，是否假设矩阵是埃尔米特矩阵（实矩阵即对称矩阵），默认值`False`
	- `True`：优化计算（更快）
 	- `False`：通用计算
- 当方阵可逆时，秩等于阶数、维度（行或列）

---
- `np.linalg.inv()`：是`NumPy`中计算方阵逆矩阵的核心函数
- 语法：`np.linalg.inv(a)`
- `a`必填，输入的可逆方阵（NumPy 数组 / 可转换为方阵的序列，如嵌套列表）。非方阵 / 不可逆方阵都会报错
- 返回一个和输入方阵同维度的`NumPy`数组，数据类型为浮点型（numpy.float64），即输入方阵的逆矩阵

# `pandas`库

`pandas`是Python中用于**数据处理和分析**的核心库

### 一、读取数据核心语法

| 语法                                            | 用途                    | 关键说明                                  |
| --------------------------------------------- | --------------------- | ------------------------------------- |
| `pd.read_csv('文件路径')`                         | 读取csv文件               | 最常用，文件路径可写绝对路径（如`C:/data.csv`）或相对路径   |
| `pd.read_excel('文件路径', sheet_name='工作表名/序号')` | 读取Excel文件             | `sheet_name=0`表示第一个工作表，需提前装`openpyxl` |
| `df.head(n)`                                  | 查看数据前n行               | 默认n=5，快速预览数据                          |
| `df.info()`                                   | 查看数据基本信息              | 显示列名、数据类型、非空值数量（清洗前必看）                |
| `df.shape`                                    | 查看数据形状                | 返回元组`(行数, 列数)`                        |

- 读取文件会自动生成`DataFrame`对象

---

### 二、数据清洗核心语法

#### 1. 空值（缺失值）处理

| 语法                                | 用途       | 关键说明                                      |
| --------------------------------- | -------- | ----------------------------------------- |
| `df.isnull().sum()`               | 统计每列空值数量 | 先定位空值位置                                   |
| `df.dropna()`                     | 删除含空值的行  | 默认删除任何有缺失值的行，也可加`subset=['列名']`只删指定列空值    |
| `df.fillna(值)`                    | 填充所有空值   | 如`df.fillna(0)`将所有空值填0                    |
| `df.fillna({'列1': 值1, '列2': 值2})` | 按列填充空值   | 更精准，如`df.fillna({'数学': df['数学'].mean()})` |

- `df.isnull()`的核心作用是**逐单元格判断 “是否是空值”**，并返回一个和原数据框形状完全一致的布尔矩阵：
	- 如果某个单元格是空值（`NaN`）→ 标记为 `True`；
	- 如果不是空值 → 标记为 `False`。
- `sum()`会遍历这个布尔矩阵的每一列，把`True`当成`1`、`False`当成`0`求和
- 因此，`df.isnull().sum()`会返回空值的个数。

---

#### 2. 重复行处理

| 语法                      | 用途      | 关键说明                         |
| ----------------------- | ------- | ---------------------------- |
| `df.duplicated().sum()` | 统计重复行数量 | 返回重复行的个数                     |
| `df.drop_duplicates()`  | 删除重复行   | 默认保留第一行，加`keep='last'`保留最后一行 |

- `df.duplicated()`会对重复行进行判断，如果该行是唯一行，则为`False`，否则为`True`。默认情况下（`keep='first'`）会保留重复的第一行，只对后面重复的判断为`True`。如果设置 `keep=False`，所有重复行都会被标记为 `True`。（`df.duplicated(keep=False)`）

---

#### 3. 异常值/条件筛选

|语法|用途|关键说明|
|---|---|---|
|`df[df['列名'] 条件]`|按条件筛选行|如`df[df['语文']<=100]`保留语文≤100的行，支持`>`, `<`, `>=`, `<=`, `==`|
|`df[(df['列1']>值) & (df['列2']<值)]`|多条件筛选|多条件用`&`（且）、`|

---

#### 4. 列名处理

| 语法                                  | 用途   | 关键说明                                                        |
| ----------------------------------- | ---- | ----------------------------------------------------------- |
| `df.rename(columns={'旧列名': '新列名'})` | 重命名列 | 可同时改多个列，如`df.rename(columns={'语文':'Chinese', '数学':'Math'})` |

---

- `df.fillna ()`基础语法结构
`fillna()`是 pandas 中处理缺失值（`NaN`/ 空值）的核心方法，完整语法如下：

```python
df.fillna( 
	value=None, # 要填充的值（数字/字符串/字典/Series等） 
	method=None, # 填充方式（ffill/bfill等，和value二选一） 
	axis=None, # 填充轴（0=按行，1=按列，默认0） 
	inplace=False, # 是否直接修改原数据（默认False，返回新数据框） 
	limit=None, # 最多填充多少个空值（可选） 
	downcast=None # 自动降低数据类型（节省内存，可选） 
)
```


- 核心参数讲解

|    参数     |                   作用                   |            常用值/示例             |
| :-------: | :------------------------------------: | :---------------------------: |
|  `value`  |              指定填充的值（最核心）               | 0、"未知"、`{'列1':80, '列2':'缺考'}` |
| `method`  |          按规则填充（和`value`不能同时用）          |   'ffill'（向前填）、'bfill'（向后填）   |
| `inplace` | 是否修改原数据（`False`= 返回新数据，`True`= 直接改原数据） |     默认`False`（推荐）、`True`      |
|  `limit`  |         限制填充的空值数量（比如只填前 2 个空值）         |              常数               |
- 注意：无论`inplace`是`True`还是`False`，都不会修改原来的文件，如果是`True`，修改的是读到的数据。
- `fillna`按参数顺序传值，如果顺序一样，就可以不用写参数名。


```python
import pandas as pd  
df = pd.read_csv(r"C:\Users\Lenovo\Desktop\加州房价数据集.csv")  
# 1. 查看前5行数据（快速预览）  
print("=== 数据前5行 ===")  
print(df.head())  
  
# 2. 查看数据基本信息（列名、数据类型、非空值数量）  
print("\n=== 数据基本信息 ===")  
print(df.info())  
  
# 3. 查看数据形状（行数, 列数）  
print("\n=== 数据形状（行, 列）===")  
print(df.shape)  
  
# 4. 查看数据的统计摘要（数值列的均值、最值等，可选）  
print("\n=== 数值列统计信息 ===")  
print(df.describe())  
  
print("=== 每列空值数量 ===")  
null_count = df.isnull().sum()  
print(null_count)  
  
dup_count = df.duplicated().sum()  
print(f"\n=== 重复行数量：{dup_count} ===")  
df_clean=df.fillna(0)  
print(df_clean.head())
```


# `matplotlib`库

- `pyplot`是`matplotlib`库中最核心、最常用的**子模块**，专门提供一套**面向用户的、简洁的函数接口**，让你能快速绘制各种图表，不用深入底层复杂的对象操作。

`pyplot`常用核心函数：

|函数|作用|
|---|---|
|`plt.figure()`|创建画布，设置大小/分辨率|
|`plt.plot()`|绘制直线图/曲线图|
|`plt.scatter()`|绘制散点图|
|`plt.bar()`|绘制条形图|
|`plt.pie()`|绘制扇形图|
|`plt.title()`|添加图表标题|
|`plt.xlabel()`/`plt.ylabel()`|添加X/Y轴标签|
|`plt.legend()`|添加图例|
|`plt.grid()`|显示网格线|
|`plt.show()`|显示图表|
|`plt.savefig()`|保存图表到文件|

---

- `matplotlib`绘图的核心逻辑是：先创建画布 / 坐标系，再绘制具体图形，最后添加标签、标题等装饰并显示 / 保存。
- `matplotlib`绘图时，**优先推荐用**`np.array()`而非普通列表，原因有 2 个：
	- 支持批量运算，快速生成绘图所需的连续数据（比如 0 到 10 的 100 个均匀点）；
	- `matplotlib`对`array`的兼容性更好，绘图效率更高。


基础模板：
- 所有图表的绘制都基于这个核心模板，只是绘图函数不同：
```python
# 1. 导入库（约定俗成的简写） 
import matplotlib.pyplot as plt 
import numpy as np 

# 2. 准备数据（不同图表数据格式略有差异） 
x = np.array([1, 2, 3, 4, 5]) 
y = np.array([2, 4, 1, 5, 3]) 

# 3. 创建画布/坐标系（可选，默认会自动创建） 
plt.figure(figsize=(8, 5)) # 设置画布大小：宽8英寸，高5英寸 

# 4. 绘制核心图形（关键：替换成不同的绘图函数） 
plt.plot(x, y) # 示例：绘制直线图 

# 5. 添加装饰（提升可读性，可选但建议加） 
plt.title("基础图表示例") # 标题 
plt.xlabel("X轴标签") # X轴标签 
plt.ylabel("Y轴标签") # Y轴标签 
plt.grid(True, alpha=0.3) # 显示网格，alpha控制透明度 
plt.legend(["数据系列1"]) # 图例（多个系列时用） 

# 6. 显示/保存图表 
plt.show() # 显示图表 
# plt.savefig("my_plot.png") # 保存图表（注意：savefig要在show之前）
```

--- 

- 通用参数（所有图表都能用，命名 / 简写一致）
这些参数是控制 “基础视觉样式” 的，无论画直线图、散点图、条形图，用法都一样：

|参数全称|简写|作用|所有图表是否通用|示例|
|---|---|---|---|---|
|`color`|`c`|颜色|✅ 是|`c="red"`/`c="#FF5733"`|
|`alpha`|无|透明度（0-1）|✅ 是|`alpha=0.7`|
|`label`|无|图例标签|✅ 是|`label="销量数据"`|
|`linewidth`|`lw`|线条宽度（有线条时）|✅ 是（有线条则可用）|`lw=2`（直线图/条形图边框）|
|`linestyle`|`ls`|线条样式（有线条时）|✅ 是（有线条则可用）|`ls="--"`（直线图/散点图边框）|
注：参数写全称和写简称效果是一样的。

**示例：通用参数在不同图表中的统一用法**

```Python
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4])
y = np.array([5,3,7,2])

# 1. 直线图：用通用参数c/alpha/label
plt.subplot(1,3,1)
plt.plot(x, y, c="red", alpha=0.8, label="直线图", lw=2, ls="--")
plt.legend()

# 2. 散点图：同样用c/alpha/label（lw/ls控制点的边框）
plt.subplot(1,3,2)
plt.scatter(x, y, c="blue", alpha=0.8, label="散点图", lw=1, ls="-")
plt.legend()

# 3. 条形图：同样用c/alpha/label（lw/ls控制条形边框）
plt.subplot(1,3,3)
plt.bar(x, y, color="green", alpha=0.8, label="条形图", lw=2, ls=":")
plt.legend()

plt.tight_layout()
plt.show()
```



- 专属参数（不同图表特有，其他图表用不了）
这些参数是针对图表的核心形态设计的，只有对应图表能用，比如：

|图表类型|专属参数|作用|示例|
|---|---|---|---|
|直线图|无核心专属参数|-|-|
|散点图|`s`|点的大小（数值）|`s=50`（越大点越大）|
|条形图|`width`/`height`|条形宽度（垂直）/高度（水平）|`width=0.6`|
|扇形图|`autopct`|显示百分比|`autopct="%1.1f%%"`|
|扇形图|`explode`|突出某一块|`explode=(0,0.1,0,0)`|
|热力图|`cmap`|配色方案|`cmap="coolwarm"`|

**示例：不同图表的专属参数**

```Python
import matplotlib.pyplot as plt
import numpy as np

# 1. 散点图专属参数s（点大小）
plt.subplot(2,2,1)
x_scatter = np.random.rand(20)
y_scatter = np.random.rand(20)
plt.scatter(x_scatter, y_scatter, c="red", s=100*np.random.rand(20))  # s控制大小
plt.title("散点图专属参数s")

# 2. 条形图专属参数width（宽度）
plt.subplot(2,2,2)
plt.bar([1,2,3], [4,5,6], width=0.3, c="blue")  # width控制宽度
plt.title("条形图专属参数width")

# 3. 扇形图专属参数autopct/explode
plt.subplot(2,2,3)
labels = ["A","B","C"]
sizes = [30,40,30]
plt.pie(sizes, labels=labels, autopct="%1.1f%%", explode=(0,0.1,0))  # 专属参数
plt.title("扇形图专属参数autopct/explode")

# 4. 热力图专属参数cmap
plt.subplot(2,2,4)
heat_data = np.random.rand(5,5)
plt.imshow(heat_data, cmap="coolwarm")  # cmap专属参数
plt.colorbar()
plt.title("热力图专属参数cmap")

plt.tight_layout()
plt.show()
```

注：简单来说，`plt.tight_layout()`的作用是：**自动调整画布中所有子图的位置和尺寸，避免子图的标题、轴标签、图例等元素重叠或被截断**，且注意必须在所有子图绘制完成后、`plt.show()`/`plt.savefig()`之前调用。


---
**参数值**：
以绘图中最常用的`color`、`linestyle`、`marker`为例：


- `color`（颜色）

|别名|颜色|别名|颜色|
|---|---|---|---|
|`red`/`r`|红色|`blue`/`b`|蓝色|
|`green`/`g`|绿色|`yellow`/`y`|黄色|
|`black`/`k`|黑色|`white`/`w`|白色|
|`cyan`/`c`|青色|`magenta`/`m`|品红|
|`orange`|橙色|`purple`|紫色|


- `linestyle`（线条样式）

|完整值|简写|效果|
|---|---|---|
|`solid`|`-`|实线（默认）|
|`dashed`|`--`|虚线|
|`dotted`|`:`|点线|
|`dashdot`|`-.`|点划线|
|`None`|`''`/`' '`|无线条（只显示标记点）|


- `marker`（标记点样式）

| 别名  | 效果   | 别名     | 效果   |
| --- | ---- | ------ | ---- |
| `o` | 圆圈   | `*`    | 星号   |
| `s` | 正方形  | `^`    | 上三角形 |
| `v` | 下三角形 | `d`    | 菱形   |
| `+` | 加号   | `x`    | 叉号   |
| `.` | 小点   | `None` | 无标记  |

---

- 常用的 array 创建方法（**绘图高频**）

| 函数                              | 作用                   | 示例                            |
| ------------------------------- | -------------------- | ----------------------------- |
| `np.array(列表)`                  | 将普通列表转为array         | `np.array([1,2,3])`           |
| `np.arange(a,b,step)`           | 生成a到b（不含b）的连续整数array | `np.arange(0,24,1)`（0-23点）    |
| `np.linspace(a,b,n)`            | 生成a到b（含b）的n个均匀点array | `np.linspace(0,2π,100)`       |
| `np.random.randint(a,b,size)`   | 生成随机整数array          | `np.random.randint(15,35,24)` |
| `np.random.normal(均值,标准差,size)` | 生成正态分布array          | `np.random.normal(170,5,100)` |

---
### 各类常用图表的具体实现

#### 1. 直线图（plot）

用于展示数据随时间/顺序的变化趋势，是最基础的图表。

```Python
import matplotlib.pyplot as plt
import numpy as np

# 准备数据：模拟时间和温度
x = np.arange(0, 24, 1)  # 0-23点
y = np.random.randint(15, 35, size=24)  # 随机温度

# 绘制直线图（可自定义样式）
plt.figure(figsize=(10, 4))
plt.plot(
    x, y, 
    color="red",    # 线条颜色
    linestyle="-",  # 线条样式：-实线，--虚线，:点线
    linewidth=2,    # 线条宽度
    marker="o",     # 数据点标记：o圆圈，*星号，s正方形
    label="温度变化"
)

# 装饰
plt.title("一天24小时温度变化")
plt.xlabel("时间（点）")
plt.ylabel("温度（℃）")
plt.xticks(x)  # X轴刻度显示所有小时
plt.legend()
plt.grid(alpha=0.3)

plt.show()
```


#### 2. 散点图（scatter）

用于展示两个变量之间的相关性（比如身高和体重）。

```Python
import matplotlib.pyplot as plt
import numpy as np

# 准备数据：模拟身高(cm)和体重(kg)
height = np.random.normal(170, 5, 100)  # 正态分布的身高
weight = height * 0.6 - 80 + np.random.normal(0, 2, 100)  # 体重（带随机误差）

# 绘制散点图
plt.figure(figsize=(8, 6))
plt.scatter(
    height, weight,
    c="blue",       # 点的颜色
    s=50,           # 点的大小
    alpha=0.7,      # 透明度（避免点重叠看不清）
    marker="^",     # 三角形标记
    label="身高-体重分布"
)

# 装饰
plt.title("身高与体重相关性")
plt.xlabel("身高（cm）")
plt.ylabel("体重（kg）")
plt.legend()
plt.grid(alpha=0.3)

plt.show()
```


#### 3. 曲线图（平滑直线图）

本质是直线图的进阶，通过更多数据点+平滑处理实现，常用`np.linspace`生成密集数据。

```Python
import matplotlib.pyplot as plt
import numpy as np

# 准备密集数据：0到2π的100个点（数据越密，曲线越平滑）
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)  # 正弦曲线

# 绘制曲线图
plt.figure(figsize=(8, 4))
plt.plot(x, y, color="green", linewidth=2, label="sin(x)曲线")

# 装饰
plt.title("正弦函数曲线图")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.axhline(y=0, color="black", linestyle="--", alpha=0.5)  # 画y=0参考线
plt.legend()
plt.grid(alpha=0.3)

plt.show()
```


#### 4. 条形图（bar/barh）

用于对比不同类别数据的大小（bar是垂直条形，barh是水平条形）。

```Python
import matplotlib.pyplot as plt
import numpy as np

# 准备数据：不同城市的销量
cities = ["北京", "上海", "广州", "深圳"]
sales = np.array([120, 150, 90, 110])

# 绘制垂直条形图
plt.figure(figsize=(8, 5))
bars = plt.bar(
    cities, sales,
    width=0.6,      # 条形宽度
    color=["red", "blue", "green", "orange"],
    label="月度销量"
)

# 给每个条形加数值标签（实用技巧）
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2,  # x坐标（条形中间）
        height + 2,                       # y坐标（条形上方）
        f"{height}",                      # 显示的数值
        ha="center", va="bottom"          # 对齐方式
    )

# 装饰
plt.title("四城市月度销量对比")
plt.ylabel("销量（件）")
plt.legend()
plt.grid(axis="y", alpha=0.3)  # 只显示y轴网格

plt.show()

# （可选）水平条形图：把bar换成barh即可
# plt.barh(cities, sales)
```


#### 5. 扇形图（pie）

用于展示各部分占总体的比例，重点是`autopct`显示百分比。

```Python
import matplotlib.pyplot as plt
import numpy as np

# 准备数据：各类支出占比
labels = ["餐饮", "房租", "交通", "娱乐", "其他"]
sizes = [30, 40, 10, 10, 10]  # 比例和为100
colors = ["#ff9999", "#66b3ff", "#99ff99", "#ffcc99", "#c2c2f0"]  # 自定义颜色

# 绘制扇形图
plt.figure(figsize=(7, 7))
plt.pie(
    sizes,
    labels=labels,        # 类别标签
    colors=colors,        # 颜色
    autopct="%1.1f%%",    # 显示百分比（1位小数）
    startangle=90,        # 起始角度（90度是垂直向上）
    explode=(0, 0.1, 0, 0, 0),  # 突出某一块（这里突出房租）
    shadow=True           # 加阴影，更立体
)

# 保证扇形图是正圆形
plt.axis("equal")

# 装饰
plt.title("月度支出占比")

plt.show()
```

### 总结

1. **核心逻辑**：`matplotlib`绘图遵循「导入库→准备数据→创建画布→绘制图形→添加装饰→显示/保存」的固定流程，不同图表仅需替换核心绘图函数（`plot`/`scatter`/`bar`/`pie`）。
    
2. **关键技巧**：① 曲线平滑需用密集数据（`np.linspace`）；② 条形图可加数值标签提升可读性；③ 扇形图用`autopct`显示百分比，`explode`突出重点。
    
3. **样式自定义**：颜色、大小、标记、透明度等参数可灵活调整，无需死记，用到时查文档即可，先掌握核心功能再优化样式。
