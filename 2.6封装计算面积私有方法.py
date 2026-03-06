import math
class Shape:
    total_num = 0
    def __init__(self):
        self.__area = 0
        Shape.total_num += 1

    #子类重写计算方法
    def _calc_area(self):
        pass

    #修改私有属性area
    def _set_area(self,value):
        self.__area = value

    #对外接口，获取面积
    def get_area(self):
        self._calc_area()
        return self.__area

class Circle(Shape):
    def __init__(self,r):
        super().__init__()
        self.r = r

    def _calc_area(self):
        area = math.pi * self.r ** 2
        self._set_area(area)

class Rectangle(Shape):
    def __init__(self,x,y):
        super().__init__()
        self.x = x
        self.y = y

    def _calc_area(self):
        area = self.x * self.y
        self._set_area(area)

#测试
n1 = Rectangle(10,20)
n2 = Circle(30)
print(f"测试矩形的面积是：{n1.get_area()}")
print(f"测试圆形的面积是：{n2.get_area()}")
print(f"创建图形总数：{Shape.total_num}")