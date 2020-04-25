# 1、定义类：初始化属性、被烤和添加调料的方法、显示对象信息的str
class SweetPotato():
    def __init__(self):
        # 被烤的时间
        self.cook_time = 0
        # 地瓜的状态
        self.cook_static = '生的'
        # 调料列表
        self.condiments = []

    def cook(self,time):
        """烤地瓜的方法"""
        # 1、先计算地瓜整体烤过的时间
        # 2、用整体烤过的时间再判断地瓜的状态
        self.cook_time += time
        if 0<=self.cook_time<3:
            self.cook_static = '生的'
        elif 3<=self.cook_time <5:
            self.cook_static = '半生不熟'
        elif 5<=self.cook_time<8:
            self.cook_static = '熟了'
        elif self.cook_time>=8:
            self.cook_static = '烤糊了'

    def add_condiments(self,condiment):
        """用户意愿的调料追加到调料列表中"""
        self.condiments.append(condiment)

    def __str__(self):
        return f'这个地瓜的被烤过时间是{self.cook_time},状态是{self.cook_static},调料有{self.condiments}'


# 2、创建对象并调用 对应的实例方法

digua1 = SweetPotato() # 创建对象
print(digua1) # 打印对象--打印的是魔法方法str

digua1.cook(2)
digua1.add_condiments('辣椒面')
print(digua1)

digua1.cook(2)
digua1.add_condiments('酱油')
print(digua1)