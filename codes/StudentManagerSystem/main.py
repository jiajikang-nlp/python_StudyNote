"""
 author:jjk
 datetime:2020/4/25
 coding:utf-8
 project name:Pycharm_workstation
 Program function:
 
"""

# 1、导入managerSystem模块
from managerSystem import *
# 2、启动学员管理系统
# 保证是当前文件运行才启动管理系统  if --创建对象并调用run方法
if __name__ == '__main__':
    student_manager = StudentSystem()
    student_manager.run()