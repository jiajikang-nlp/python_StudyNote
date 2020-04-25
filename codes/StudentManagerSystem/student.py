"""
 author:jjk
 datetime:2020/4/25
 coding:utf-8
 project name:Pycharm_workstation
 Program function:
 
"""
"""
需求：
- 学员信息包含：姓名、性别、手机号；
- 添加 __str__ 魔法方法，方便查看学员对象信息

"""

class Student(object):
    def __init__(self,name, gender,tel):
        # 学员信息包含：姓名、性别、手机号；
        self.name = name
        self.gender = gender
        self.tel = tel
    # 添加 __str__ 魔法方法，方便查看学员对象信息
    def __str__(self):
        return f'{self.name}, {self.gender}, {self.tel}'

# 测试代码
# aa = Student('aa','nv',121)
# print(aa)