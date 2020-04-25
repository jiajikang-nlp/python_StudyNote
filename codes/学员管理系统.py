# 定义功能界面函数
def info_print():
    print('请选择功能-------')
    print('1、添加学员')
    print('2、删除学员')
    print('3、修改学员')
    print('4、查询学员')
    print('5、显示所有学员')
    print('6、退出系统')
    print('-' * 20)

# 等待存储所有学员的信息
info = []
# 添加学员信息的函数
def add_info():
    """添加学员函数"""
    # 添加用户输入学员信息
    # 1 用户书臣：学号、姓名、手机号

    new_id = input('请输入学号：')
    new_name = input('请输入姓名：')
    new_tel = input('请输入手机号：')

    # 声明info是全局变量
    global info
    #2 判断是否添加这个学员：如果学员姓名一斤存在报错提示：如果不存在则添加数据
    # 2.1 不允许姓名重复：判断用户输入的姓名和 列表里面字典的name对应的值 相等 提示
    for i in info:
        if new_name == i['name']:
            print('此用户已经存在')
            return # 此时，退出当前函数，后面添加信息的代码不执行

    # 2.2 如果输入的姓名不存在，添加数据：准备空字典，字典新增数据，列表追加字典
    info_dict = {}

    # 字典新增数据
    info_dict['id'] = new_id
    info_dict['name'] = new_name
    info_dict['tel'] = new_tel
    print(info_dict) # 打印一下

    # 列表追加字典
    info.append(info_dict)
    print(info)






# 系统功能需要循环使用，直到用户输入6，退出系统

# 删除学员信息的函数
def del_info():
    """删除学员信息"""
    # 1、用户输入目标学员姓名
    del_name = input('请输入要删除的学员姓名：')


    # 2、检查这个学员是否存在:存在删除，不存在提示
    # 2.1 声明info是全局变量
    global info
    # 2.2 遍历列表
    for i in info:
        # 2.3 判断学员是否存在，执行删除（列表里面的字典），break：这个系统不允许重名，删除了一个后面的不需要在遍历
        if del_name == i['name']:
            info.remove(i)
            break
    else:
        print('该学员不存在')
    print(info)

# 修改学员信息的函数
def modify_info():
    """修改函数"""
    # 1、用户输入目标学员姓名
    modify_name = input('请输入要修改学员的姓名：')
    global info
    # 2、检查这个学员是否存在
    #    2.1 如果存在，则修改这个学员的信息，例如手机号
    #    2.2 如果不存在，则报错
    for i in info:
        if modify_name== i['name']:
            # 将tel这个key修改值，并终止此循环
            i['tel'] = input('请输入新的手机号：')
            break
    else: # 循环都没执行，自然不存在
        print('学员不存在')
    print(info)

# 查询学员
def search_info():
    """查询学员信息"""
    # 1、用户输入目标学员名称
    search_name = input('请输入要查找的学员姓名：')
    global  info
    # 2、检查学员是否存在
    #    2.1 如果存在，则显示这个学员的信息
    #    2.2 如果不存在，则报错
    for i in info:
        if search_name == i['name']:
            print('查到找学习信息如下：--------')
            print(f"该学员的学号为{i['id']},姓名是{i['name']}, 手机号是{i['tel']}")
            break
    else:
        print('不存在')
    # 3、对应的if条件成立的位置调用该函数

# 显示所有学员信息
def print_all():
    """显示所有学员信息"""
    #1、打印提示字
    print('学号\t姓名\t手机号')
    #2、打印所有学员的数据
    for i in info:
        print(f"{i['id']}\t{i['name']}\t {i['tel']}")


# 循环功能
while True:
    # 1、显示功能界面
    info_print()

    # 2、用户输入功能序号
    user_num = int(input('请输入功能序号：'))

    # 3、按照用户输入的功能序号，执行不同的界面
    # 如果用户输入1、执行添加...... ----多重判断
    if user_num == 1:
        #print('添加')
        add_info()
    elif user_num == 2:
        #print('删除')
        del_info()
    elif user_num == 3:
        #print('修改')
        modify_info()
    elif user_num == 4:
        #print('查询')
        search_info()
    elif user_num == 5:
        print_all()
        #print('显示所有')
    elif user_num == 6:
        exit_fla = input('确定要退出系统 yes or no:')
        if exit_fla == 'yes':
            break
    else:
        print('输入的功能序号有误')






