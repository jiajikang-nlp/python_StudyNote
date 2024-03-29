# Pycharm的基础设置

==考虑使用xmind==

[file]--[Setting]/[Defaut Settings]

**修改代码文字格式**

[Editor]--[Font]

- Font：修改字体
- Size：修改字号
- Line Spacing：修改行间距

**修改解释器**

[Project:项目名称]--[Project Interpreter]--[设置图标]--[Add]--浏览到目标解释器--[OK]--[OK]

![1586878076136](assets/1586878076136.png) 

**项目管理**

[File]--[Open]--浏览选择目标项目根目录--[ok]--选择打开项目方式

打开项目的方式三种：

![1586878223910](assets/1586878223910.png) 

1、This Window

覆盖当前项目，从而打开目标项目

2、New Window

在新窗口打开，则打开两次Pycharm,每个pycharm负责一个项目

3、Attach

一个窗口下打开多个项目，也就是多个项目重叠（本人比较喜欢这种，一眼尽收眼底）

**项目关闭**： [File]-[Close Project]/[Close Project in current window]

---

# 一、Python基础语法

## 1.1 注释

```
第一种(快捷键：ctrl+/)：  #     
第二种：
        """
        """
```

## 1.2 变量

**定义变量**

```
变量名 = 值
```

> 变量名自定义，要满足==标识符==命名规则



**标识符**

标识符命名规则是 Python中定义各种名字的时候的统一规范，具体如下

- 由数字、字母、下划线组成
- 不能数字开头
    不能使用内置关键字
- 严格区分大小写

![1586879410841](assets/1586879410841.png)   

**命名习惯：**

- 见名知义。
- 大驼峰：即每个单词首字母都大写，例如：`MyName`
- 小驼峰：第二个（含）以后的单词首字母大写，例如：`myName`
- 下划线：例如：`my_name`

---

**使用变量：**

```python
my_name = "jiajikang"
```

## 1.3 认识bug&Debug工具

所谓bug，就是程序中的错误。如果程序有错误，需要程序员排查问题，纠正错误。

Debug工具是PyCharm IDE中集成的用来调试程序的工具，在这里程序员可以查看程序的执行细节和
流程或者调解bug。

**Debug工具使用步骤：**

1. 打断点
2. Debug调试

---

### 1.3.1 打断点

**断点位置：**目标要调试的代码的第一行代码即可，即第一个断点。

**打断点的方法：** 单击目标代码的行号右侧空白位置

### 1.3.2 Debug调试

第一步：Debug运行

![1586947915788](assets/1586947915788.png) 

第二步：

![1586948000643](assets/1586948000643.png) 

![1586948098220](assets/1586948098220.png) 

## 1.4 数据类型

​	在 Python里为了应对不同的业务需求，也把数据分为不同的类型（xmind制作，可了解这个思维导图软件奥，用习惯了，你会比爱你老婆还喜欢这个，哈哈哈）。

![1586948252529](assets/1586948252529.png) 

> <font color=red>说明</font>：使用`type()`函数实现查看数据具体的类型



## ==1.5 变量章节总结==

- 定义变量的值 

    ```
    变量名 = 值
    ```

- 标识符

    由数字、字母、下划线组成

    不能数字开头

    不能使用内置关键字

    严格区分大小写

- 数据类型

    整型：int

    浮点型：float

    字符串：str

    布尔型：bool

    元组：tuple

    集合：set

    字典：dict

## 1.6 输出

- 格式化输出

    格式化符号

    f-字符串

- print的结束符



```python
print('hell')
age = 18
print(age)
```

### 1.6.1 格式化输出



![1586960560100](assets/1586960560100.png) 

**技巧：**

- %06d，表示输出的整数显示位数，不足以0补全，超出当前位数则原样输出
- %.2f，表示小数点后显示的小数位数。



### 1.6.2 输出_格式化基础

所谓的格式化输出即按照一定的格式输出内容。

**格式化符号**

```python
# 格式化符号输出数据
age = 18
name = "jiajikang"
weight = 120.3
stu_id = 1
print('%d岁' % age)
print('%s' % name)
print('%.2f' % weight)# 小数点后面保存2位
```



### 1.6.3 输出_格式化高级使用

```python
print('%d' % stu_id)
# 例如学号001
print('%03d' % stu_id) # %06d，表示输出的整数显示位数，不足以0补全，超出当前位数则原样输出

print('名字%s, 今年年龄%d' %(name,age) )
print('名字%s, 明年年龄%d' %(name,age+1) )
print('名字%s,年龄%d,体重%f,学号%d' % (name,age,weight,stu_id))
```

 ### 1.6.4 输出_拓展格式化字符串

```python
name = 'tom'
age = 13
weight = 12.3

print('名字%s，年龄%s， 体重%s' % (name,age,weight)) # 都可以使用%s

```

### 1.6.5 输出_f-格式化字符串

格式化字符串除了%s，还可以写成：`f{表达式}`

```python
age = 23
name = 'tom'
print('名字%s，年龄%s， 体重%s' % (name,age,weight)) # 都可以使用%s

# 语法：f{表达式}
print(f'名字是{name}, 年龄{age}') # 比%s更高效一点
```

### 1.6.6 输出_转义字符

- `\n`：换行
- `\t`：制表符，一个tab键（4个空格）距离

```python
print('hell \n python') # 换行
print('\tabcd') # 四个制表符
```

### 1.6.7 输出_print结束符

```python
print('输出的内容',end='\n')
print('hello',end='\t')
print('word')
print('hello',end='...')
```

> 在 Python中， print()，默认自带end="\n"这个换行结束符，所以导致每两个print直接会换行展示，用户可以按需求更改结束符。

### ==1.6.8 输出_总结==

- 格式化符号

    %s：格式化输出字符串

    %d：格式化输出整数

    %f：格式化输出浮点数

- f-字符串

    f'{表达式}'

- 转义字符

    \n：换行

    \t：制表符

- print结束符

    ```python
    print('内容',end="")
    ```



## 1.7 输入

在 Python中，程序接收用户输入的数据的功能即是输入。

**目标：**

- 输入功能的特点
- 输入input的特点

**输入语法：**

```python
input('提示信息')
```

**输入的特点：**

- 当程序执行到`input` ，等待用户输入，输入完成之后才继续向下执行。
- 在python中，`input`接收用户输入后，一般存储到变量，方便使用。
- 在python中，`input`会把接收到的任意输入的数据当做**字符串**处理。

**输入功能的实现：**

```python
password=input('请输入您的密码：')
print(f'您输入的密码是{password}')
print(type(password)) # str
```

## 1.8 转换数据类型

- 数据类型转换的必要性
- 数据类型转换常用方法

**转换数据类型的作用：**

问：input()接收用户输入的数据都是字符串类型，如果用户输入1，想得到整型该如何操作

答：转换数据类型即可，即将字符串类型转换成整型

**转换数据类型的函数：**

  ![1586963318720](assets/1586963318720.png) 

```python
num = input('请输入数字：')
print（num）
print(type(num)) # str
print(type(int(num))) # int

num1 = 1
str1 = '10'
print(type(float(num1))) # float
print(float(num1)) # 1.0

print(float(str1)) # 10.0

#数据转换成字符串
print(type(str(num1)))

# 3、tuple()将一个序列转换成元组
list1 = [10,20,30]
print(type(tuple(list1))) # 

#将一个序列转换成列表
t1 = (100,200,300)
print(list(t1)) # [100,200,300]

# 计算在字符串中有效python表达式，并返回一个对象
str2 = '1'
str3 = '1.1'
str4 = '(100,200,300)'
str5 = '[100,200,300]'
print(type(eval(str2))) # int
print(type(eval(str3))) # float
print(type(eval(str4))) # tuple
print(type(eval(str5))) # list

```

##1.9 转换类型总结

- 转换数据类型常用的函数

- [ ] int()
- [ ] float()
- [ ] list()
- [ ] tuple()
- [ ] eval() 

## 1.10 pychrm交互式开发

```
左下角：python Console
关闭交互式开发环境：1、右侧“-”；2、file-close project
```

 ![1587086401554](assets/1587086401554.png) 



# 二、运算符

**运算符的分类：**

●  算数运算符

● 赋值运算符

● 复合赋值运算符

● 比较运算符

● 逻辑运算符

---

##2.1 **算术运算符**

```python
+
-
*
/
// # 整除
%  # 取余
** # 指数
() # 小括号
```

> 混合运算优先级顺序：`（）`高于`**`高于`*` `/` `//` `%` 高于 `+` `-`



---

##2.2 **赋值运算符**

- 单个变量赋值

```python
num = 1
print(num)
```

- 多个变量赋值

```python
num1, float1, str1 = 10,0.5, 'hello world'
print(num1)
print(float1)
print(str1)
```

- 多变量赋相同值

```python
a = b = 10
print(a)
print(b)
```

## 2.3 复合赋值运算符

```python
+=
-=
*=
/=
//= # 整除赋值运算符  c//=a -> c =c//a
%=  # 取余赋值运算符  c%=a  -> c = c%a 
**= # 幂赋值运算符    c**=a -> c = c**a
```

```python
a = 100
a += 1
# 输出101 a = a+1 ，最终a = 100+1
print(a) # 101

b = 10
b -= 1 # b = b-1
print(b) # 9

#注意： 先算复合运算符右边的表达式；算复合赋值运算
c = 10
# c +=3 -- c=c+3
c += 1+2 # c= c+1+2
print(c) # 13

d = 10
d*=1+2
print(d) # 30

```

## 2.4 比较运算符

比较运算符也叫关系运算符，通常用来判断。

 ![1587101527437](assets/1587101527437.png)



## 2.5 逻辑运算符

 ![1587101683797](assets/1587101683797.png)

```python
a = 1
b = 2
c = 3
# 与
print((a<b) and (b<c)) # True
print((a>b) and (b<c)) # False
# 或
print((a>b) or (b<c)) # True
# 非：取反
print(not False) # True
print(not (a>b)) # True
```

**拓展：数字逻辑运算符**

```python
a = 0
b = 1
c = 2

# and运算符，只要有一个值为0，则结果为0，否则结果为最好一个非0数字
print(a and b) # 0
print(b and a) # 0
print(a and c) # 0
print(c and a) # 0
print(b and c) # 2
print(c and b) # 1

#or运算符，只有所有值为0结果才为0，否则结果为第一个非0数字
print(a or b) # 1
print(a or c) # 2
print(b or c) # 1
```

## ==2.6 运算符总结==

- 算符运算的优先级

    混合运算优先级顺序： `（）`高于`**`高于`*` `/` `//` `%` 高于 `+` `-`

- 赋值运算符

    =

- 复合运算符

    +=

    -=

    优先级

    ​       1、先算复合赋值运算符右测的表达式

    ​       2、再算复合赋值运算的算数运算

    ​       3、最后算赋值运算

- 比较运算符

    判断相等：==

    大于等于：>=

    小于等于：<=

    不等于：!=

- 逻辑运算符

    与：and

    或：or

    非：not

# 三、条件语句

假设一个场景：

- 同学们这个年龄去过网吧吗？
- 去网吧进门想要上网必须做的一件事是做什么？（考虑重点）
- 为什么要把身份证给工作人员？
- 是不是就是为了判断是否成年？
- 是不是如果成年可以上网？如果不成年则不允许上网？

其实这里所谓的判断就是条件语句，即条件成立执行某些代码，条件不成立则不执行这些代码。

##3 .1 语法

```python
if 条件:
   条件成立执行的代码1
   条件成立执行的代码2
   ...
```

**快速体验：**

```python
if True:
    print("条件成立执行的代码1")
#注意：在这个下方的没有加缩进的代码，不属于if语句块，即和条件成立与否无关
print("这个代码成立嘛？")
```

##3.2 实例

需求分析：如果用户年龄大于等于18岁即成年，输出已经成年，可以上网"。

```python
age = 20
if age >= 18:
    print("可以上网")
 print("系统关闭")   
```

**进阶版：**新增需求：用户可以输出自己的年龄，然后系统进行判断是否成年，成年则输出您的年龄是用户输入
的年龄'，已经成年，可以上网"。

```python
#1、用户输入
#2、保存用户输入的年龄
#3、if
age = input("请输入年龄：")
age = int(age)
if age >= 18:
    print(f'您输入的年龄是{age},已经成年，可以上网')

```



---

**if...else...**

```python
#1、用户输入
#2、保存用户输入的年龄
#3、if
age = input("请输入年龄：")
age = int(age)
if age >= 18:
    print(f'您输入的年龄是{age},已经成年，可以上网')
else:
    print(f'您输入的年龄是{age},未成年，不可以上网')
```

> 注意：如果某些条件成立执行了相关的代码，那么其他的情况的代码解释器根本不会执行。

## 3.3 多重判断

>思考：中国合法工作年龄为18-60岁，即如果年龄小于18的情况为童工，不合法；如果年龄在18
>-60岁之间为合法工龄；大于60岁为法定退休年龄。

```python
if 条件1：
    条件1成立执行的代码
elif 条件2：
    条件成立执行的代码
...
else:
    以上条件都不成立执行的代码

```

> 多重判断也可以和else配合使用。一般else放到整个if语句的最后，表示以条件都不成立的时候
> 执行的代码。

```python
"""
1、用户输入自己的年龄
2、做判断
3、输出提示信息：您输入的年龄：，合法与否
"""
age= input('请您输入年龄：')
age = int(age)
if age<18:
    print(f'您输入的年龄是{age},童工')
elif (age>=18) and (age<=60):
    print(f'您输入的年龄是{age},合法')
elif age>60:
    print(f'您输入的年龄是{age},退休年龄')

```



----

**if嵌套：**

```
if 条件1：
    条件1成立执行的代码
    if 条件2：
        条件2成立执行的代码
```

> 条件2的if也是出于条件1的缩进关系内部

**实例：**

```python
"""
1、准备将来要做判断的数据：钱和空座位
2、判断是否有钱：上车 和 不能坐上车
3、上车了：判断是否能坐下：有空座位 和 无空座位
"""
money = 1
seat = 1
if money == 1:
    print('土豪，请上车')
    #判断能否坐车
    if seat ==1:
        print('有空座，坐下了')
    else:
        print('没有空座，站着吧你')
else:
    print('土鳖，跑着去')
```

**if嵌套执行流程**

 ![1587111331842](assets/1587111331842.png)



## 3.4 综合应用

需求分析：

- 参与游戏的角色

    玩家

    ​        手动出拳

    电脑

    ​        随机出拳

- 判断输赢

    玩家获胜

    平局

    电脑获胜

```python
"""
1、出拳
      玩家：手动输入
      电脑：1.固定 ：剪刀；2. 随机
      
2、判断输赢
   玩家获胜
   平局
   电脑获胜

"""
import random
player = int(input("请出拳：0--石头；1--剪刀；2--布"))
#电脑
#computer = 1
computer = random.randint(0,2)
print(computer)

# 2、判断输赢
if ((playter==0) and (computer==1) and (playter==1) and (computer==2) and (playter==2) and (computer==0)):
    print('玩家赢')
elif player == computer:
    print('平局')
else:
    print('电脑赢')

```

**随机数做法：**

```
import 模块名
random.randint(开始,结束)
```

```python
import random
num = random.ranint(0,2)
print(num) # 一个随机整数0,1,2

```

# <font color=red>四、三目运算符</font>

```python
条件成立执行的表达式 if 条件 else 条件不成立执行的表达式
```

```python
a = 1
b = 2
c = a if a>b else b
print(c) # 2

# 需求：有两个变量，比较大小，变量1 大于 变量2 执行 变量1 - 变量2； 否则 变量2 - 变量1
aa = 10
bb = 6
c = aa-bb if aa>bb else bb--aa
print(c) # 4

```

# 五、循环语法

**目标：**

- 了解循环
- while语法【重点】
- while应用
- break和continue和
-  while循环嵌套【重点】
-  while循环嵌套应用【难点】
- for循环

---

## 5.1  循环的分类

在python中，循环分为 `while` 和 `for` 两种，最终实现效果相同。

###5.1.2 while语法

```
while 条件：
    条件成立重复执行的代码1
    条件成立重复执行的代码1
    ...
```

**快速体验：**需求：复现重复执行100次 `print('媳妇，我错了')`（输出更简洁一些，我们这里设置5次）。

```python
i = 1
while i<=5:
    print('媳妇我错了')
    i += 1
print('任务结束')
```

**计数器习惯书写**

```python
i = 0
while i<5:
    print('媳妇我错了')
    i += 1
print('任务结束')
```

**解释器如何执行：**

```python
# 采用Debug每步每步执行
i = 0
while i<5:
    print('媳妇我错了')
    i += 1
print('原谅你了')
```



---



**while应用一:**

```python
"""
分析：1-100的累加和，即1+2+3+4+即前两个数字的相加结果+下一个数字（前一个数字+1）
"""
i = 0
sum = 0
while i<100:
    sum +=i
    i += 1

print(f'sum={sum}')

```

**while应用二:**

```python
"""
分析：1-100的偶数和，即2+4+6+8得到偶数的方法如下：
偶数即是和2取余结果为0的数字，可以加入条件语句判断是否为偶数，为偶数则累加
初始值为0/2，计数器每次累加2

"""
```

```python
# 方法一：条件判断和2取余数则累加
i = 1
result = 0
while i <= 100:
    if i % 2 == 0:
        result += i
    i += 1
print('result=%d' % result)
```

```python
# 方法二：计数器控制增量2
i = 2
result = 0
while i<=100:
    result += i
    i += 2
print(result) 
```

### 5.1.2 while循环嵌套

```python
while 条件:
    while 条件：
        print('媳妇我错了')
    print('刷晚饭的碗')
```

```
while 条件1：
    条件1成立的执行的代码
    ...
    while 条件2：
    条件2成立执行的代码

```

**快速体现：**

```python
j = 0
while j<3:
    i =0
    while i<3:
        print('媳妇我错了')
        i+=1
    print('刷碗')    
```

###5.1.3 break和continue

break和continue是循环中满足一定条件退出循环的两种不同方式。

**break**：当某些条件成立，退出当前循环

```python
i = 1
while i <= 5:
    if i==4:
        print(f'吃饱了不吃了')
        break
    print(f'吃了第{i}个苹果')
    i += 1
```

**continue**：当某些条件成立时候，退出当前循环，继而执行下一次循环

```python
i = 1
while i<=5:
    if == 3:
        print('有虫子,这个苹果不说了')
        # 如果使用continue，在continue之前一定要修改计数器，否则进入死循环
        i += 1
        continue
    print(f'吃了第{i}个苹果')
    i += 1
```



### 5.1.4 while循环嵌套应用

**应用一：**

```python
j = 0
while j<5:
    # 一行星星开始
    i = 0
    while i<5:
        print('*'，end='')
        i += 1
    # 一行星星结束    
    print() # 默认换行
    j+=1
```

**应用二：**

```python
# 三角形：每行星星的个数和行号数相等
j = 0
while j<5:
    # 一行星星开始
    i = 0
    # i表示每行里面星星的个数，这个数字要和行号相等所以i要和j联动
    while i<=j: 
        print('*'，end='')
        i += 1
    # 一行星星结束    
    print() # 默认换行
    j+=1
```

**应用三：**

```python
#重复打印9行乘法表达式
"""
1、打印一个乘法表达是：x * x = x*x
2、一行打印多个表达式--一行表达式的个数和行数相等 -- 循环：一个表达式，不换行

"""
j = 1
while j<=9:
    #一行的表达式开始
    i = 1
    while i<=j:
        print(f'{i} * {j} = {i*j}',end='\t')
        i += 1
    #一行表达时的结束
    print()
    j += 1

```

### 5.1.5 for循环

```python
for 临时变量 in 序列：
    重复执行的代码1
    重复执行的代码2
    ......
```

```python
str1 = 'jiajikang'
for i in str1:
    print(i)
```

####1、**break退出for循环**

```python
str1 = 'itheima'
for i in str1:
    if i == 'e':
        break
    print(i) # i t h
```

#### 2、continu退出for循环

```python
str1 = ‘itheima’
for i in str1:
    if i == 'e':
        continue
    print(i) # i t h i m a 
```

## 5.2 while...else

循环可以和else配合使用，else下方缩进的代码指的是当循环正常结束之后要执行的代码。

**while...else**

需求：女朋友生气了，要惩罚：连续说5遍“媳妇儿，我错了”，如果道歉正常完毕女朋友就原谅我了，这
个程序怎么写？

```python
i = 1
while i <= 5:
    print('媳妇我错了')
    i += 1
print('媳妇原谅我了')
```

**while...else语法**

```python
while 条件：
    条件成立重复执行的代码
else：
    循环正常结束之后要执行的代码
```

```python
i = 1
while i <= 5:
    print('媳妇我错了')
    i += 1
else:
    print('原谅我了')

```

###5.2.1 while...else之break和continue

**break:**

```python
i = 1
while i<5:
    if i==3:
        print('这边说的不真诚')
        break
    print('媳妇我错了')
    i += 1
else:
    print('媳妇原谅我了')
```

>  所谓else指的是循环正常结束之后要执行的代码，即如果是 break终止循环的情况，else下方缩进的代码将不执行。



**continue:**

```python
i = 1
while i<5:
    if i==3:
        i +=1
        print('这边说的不真诚')
        continue
    print('媳妇我错了')
    i += 1
else:
    print('媳妇原谅我了')
```

>因为 continue是退出当前一次循环，继续下一次循环，所以该循环在 continue控制下是可以正常结束的，当循环结束后，则执行了else缩进的代码。

## 5.3 for...else

```python
for 临时变量 i 序列：
    重复执行的代码
    ...
else:
    循环正常结束之后要执行的代码
```

```python
str1 = 'itheima'
for i in str1:
    print(i)
else:
    print("循环正常结束之后，执行的代码")
```

### 5.3.1 for...else之break和continue

**break：**

```python
str1 = 'itheima'
for i in str1:
    if i == 'e':
        break
        #continue
    print(i)
else:
    print('循环正常结束执行的else代码')
```

**continue：**

```python
str1 = 'itheima'
for i in str1:
    if i == 'e':
        #break
        continue
    print(i)
else:
    print('循环正常结束执行的else代码')
```

# 六、字符串

**目标：**

- 认识字符串
- 下标
- 切片
- 常用操作方法

## 6.1 认识字符串

字符串是 Python中最常用的数据类型。我们一般使用引号来创建字符串。创建字符串很简单，只要为变量分配一个值即可。

```python
a = 'hello' \ 
     'world'
b = 'abcdefg'
print(type(a)) # str
print(type(b)) # str

# 三引号
e = '''i am tom'''
print(type(e)) # str
f = """i am tom"""
print(type(f)) # str

# 转义字符问题
# I'm Tom
c = " I'm Tom "
print(c) #  I'm Tom
print(type(c)) # str

# d = ' I'm Tom '
d = ' I\'m Tom '
print(d) #  I'm Tom
print(type(d)) # str

```

## 6.2  字符串输出

```python
print('hello wolrd')

name = 'Tom'
print(f'我的名字是%s' % name)
print(f'我们的名字是{name}')

```

## 6.3 字符串输入

在python中，使用 `input()` 接收用户输入

```python
name = input('请输入名字：')
print(f'您输入的名字是{name}')
print(type(name)) # str

password = input('请输入您的密码：')
print(f'您输入的密码是{password}')
print(type(password)) # str
# 总结：无论是字符串还是数字都是str类型
```



## 6.4 下标

==下标==又叫==索引==，就是编号。比如火车座位号，座位号的作用：按照编号快速找到对应的座位。同理，下标的作用就是通过下标快速找到对应的数据。

```python
str1 = 'abcdefg'
print(str1)

# 想得到数据a字符，得到数据b字符 -- 使用字符串中某个特定的数据
# 这些字符数据从0开始顺序分配一个编号 -- 使用这个编号精确找到某个字符数据-- 下标或者索引或索引值
print(str1[0]) # a
print(str1[1]) # b

```

## 6.5 切片

### 6.5.1 切片简介

```python
str1 = 'abcdefg'
print(str1) # 获取整个

# 下标得到的是下标为某个数字的数据
print(str1[2]) # c
# 得到abc这三个数据该怎么办？
```

切片是指对操作的对象截取其中一部分的操作。**字符串、列表、元组**都支持切片操作。

---

**语法：**

```
序列[开始位置下标 ：结束位置下标 ：步长]
```

> 注意

1、不包含结束位置下标对应的数据，正负整数均可.

2、步长是选取间隔，正负整数均可，默认步长为1.

### 6.5.2 切片体验

```python
name = 'abcdefg'
print(name[2:5:1]) # cde
print(name[2:5]) # cde
print(name[:5]) # abcde  -- 如果不写开始，默认从0开始选取
print(name[2:]) # cdefg  -- 如果不写结束，表示选取到最后
print(name[:]) # abcdefg -- 如果不写开始和结束，表示选取所有

# 负数测试
print(name[::-1])  #gfedcba 如果步长为负数，表示倒序选取
print(anme[-4:-1]) # def 下标-1表示最后一个数据，依次向前类推

#终极测试
print(name[-4:-1:1]) # def
print(name[-4:-1:-1]) # 不能选取数据，从-4开始到-1结束，选取方向为从在到右，但是-1步长，从右向左选取
# ***** 如果选取方向(下标开始到结束的方向) 和 步长的方向冲突，则无法选取数据
print(name[-1:-4:-1]) # 要方向一致，才能选取数据
```

##6.6 字符串常用方法

字符串的常用操作方法有**查找、修改和判断**三大类。

### 6.6.1 查找find()和index()

所谓字符串查找方法即是查找子串在字符串中的位置或出现的次数。

- find()：检测某个子串是否包含在这个字符串中，如果在返回这个子串开始的位置下标，否则则返回-1。

**1、语法**

```
字符串序列.find(子串，开始位置下标，结束位置下标)
```

> 注意：开始和解书位置下标可以省略，表示在整个字符串序列中查找。

**2、快速体验**

```python
mystr = "hello world and itcast and iteima and python"

print(mystr.find('and')) # 12
print(mystr.find('and', 15, 30)) # 23
print(mystr.find('ands')) # -1
```



----



- index()：检测某个子串是否包含在这个字符串中，如果在返回这个子串开始的位置下标，否则则报异常

**1、语法**

```
字符串序列.index(子串，开始位置下标，结束位置下标)
```

> 注意：开始和结束位置下标可以省略，表示在整个字符串徐柳中查找。

**2、快速体验**

```python
mystr = "hello world and itcast and iteima and python"

print(mystr.index('and')) # 12
print(mystr.index('and', 15, 30)) # 23
print(mystr.index('ands')) # 如果index查找子串不存在，会报错
```



---



- count（）

**1、语法**

```
字符串序列.count(子串，开始位置下标，结束位置下标)
```

**2、快速体验**

```python
mystr = "hello world and itcast and iteima and python"

print(mystr.count('and',15,30)) # 1
print(mystr.count('and')) #  3
print(mystr.count('ands')) #  3
```



---

- rfind()：和find()功能相同，但查找方向从==右侧==开始
- rindex()：和index()功能相同，但查找方向为==右侧==开始
- count()：返回某个子串在字符串中出现的次数

```python
mystr = "hello world and itcast and iteima and python"
print(mystr.rfind('and')) # 1
```

### 6.6.2 修改

所谓修改字符串，指的就是通过函数的形式修改字符串中的数据。

- replace()： 替换

**1、语法**

```
字符串序列.replace(旧字符串，新子串，替换次数)
```

> 注意：替换次数如果查出子串出现的数据，则替换次数为该子串出现的次数

**2、快速体验**

```python
mystr = "hello world and itcast and iteima and python"
print(mystr.replace('and', 'he')) # hello world he itcast he iteima he python

print(mystr.replace('and', 'he', 10)) # 替换次数如果超出字串出现的次数，表示替换所有这个字串
print(mystr)

#**** 调用了replace函数后，发现原有字符串的数据并没有做到修改，修改后的数据是replace函数的返回值
#--- 说明 字符串是不可变数据类型
#数据是否可以改变划分为 可变类型 和  不可变类型
```

> 注意：数据按照是否能直接修改分为可变类型和不可变类型两种。字符串类型的数据修改的时候
>
> 不能改变原有字符串，属于不能直接修改数据的类型即是不可变类型。



---



- split()：按照指定字符分割字符串  ---  分割， 返回一个列表， 丢失分割字符

**1、语法**

```
字符串序列.split(分割字符，num)
```

> 注意：num表示的是分割字符出现的次数，即将来返回数据个数为num+1个。

**2、快速体验**

```python
mystr = "hello world and itcast and iteima and python"

list1 = mystr.split('and')
# ['hello world ', ' itcast ', ' iteima ', ' python']
print(list1)
```



---



- join()： 用一个字符或子串合并字符串，即是将多个字符串合并为一个新的字符串

**1、语法**

```python
字符或者子串.join(多字符串组成的序列)
```

**2、快速体验**

```python
list1 = ['chuan', 'zhi', 'bo', 'ke']
t1 = ('aa','b','cc','ddd')
#chuan...zhi...bo...ke
#<class 'str'>
new_list1 = '...'.join(list1)
print(new_list1)

```

### 6.6.3 修改之大小写转换

- capitalize()： 将字符串第一个字符转换成大写

```python
mystr = "hello world and itcast and iteima and python"
# Hello world and itcast and iteima and python
print(mystr.capitalize())

```

> 注意：capitalize()函数转换后，字符串第一个字符大写，其他的字符全是小写



---

- title()：将字符串每个单词首字母转换成大写。

```python
mystr = "hello world and itcast and iteima and python"
# Hello World And Itcast And Iteima And Python
print(mystr.title())
```



---

- lower()：将字符串中大写转换成小写

```python
mystr = "hello World and itcast and iteima and python"

print(mystr.lower())

```

  

---



- upper()：将字符串中小写转换成大写

```python
mystr = "hello World and itcast and iteima and python"

print(mystr.upper())
```



----



### 6.6.4 修改之删除空白字符

- lstrip()：删除字符串左侧空白字符
- rstrip()：删除字符串右侧空白字符
- strip()：删除字符串两侧空白字符（这里要注意和split函数注意区分）

```python
mystr = "     hello World and itcast and iteima and python     "
new_str = mystr.lstrip()
print(new_str)
```



### 6.6.5 修改之字符串对齐

- ljust()：返回一个原字符串左对齐，并使用指定字符（默认空格）填充至对应长度的新字符串。

1、语法

```
字符串序列.ljust(长度，填充字符)
```

2、快速检测

```python
mystr = 'hello'
print(mystr.ljust(10,'.')) # hello.....

```

- rjust()：返回一个原字符串右对齐并使用指定字符（默认空格）填充至对应长度的新字符串，语法和ljust()相同
- center()：返回一个原字符串居中对齐并使用指定字符（默认空）填充至对应长度的新字符串，语法和ljust()相同。



### 6.6.6 判断开头或结尾

所谓判断即是判断真假，返回的结果是布尔型数据类型：True或 False

- startswith()： 检查字符串是否是以指定子串开头，是则返回True，否则返回 False。如果设置开始和结束位置下标，则在指定范围内检查。

1、语法

```
字符串序列.startswitch(字串，开始位置下标，结束位置下标)
```

2、快速体验

```python
mystr = "hello World and itcast and iteima and python"
print(mysrt.startswith('hello')) # True

```

- endswith（）：与startswitch函数类似

```python
# endswitch()
print(mystr.endswitch('pythons')) # False
```



### 6.6.7 判断

- isalpha()：如果字符串至少有一个字符并且所有字符都是字母则返回True，否则返回False

```python
mystr1 = 'hello'
mystr2 = 'hello1234'

print(mystr1.isalpha()) # True

print(mystr2.isalpha()) # False

```

- isdigit()：如果字符串只包含数字则返回True否则返回False

```python
mystr1 = 'aaa23232'
mystr2 = '12121'
print(mystr1.isdigit()) # False
print(mystr2.isdigit()) # True
```

- isalnum：如果字符串至少有一个字符并且所有字符都是字母或者数字则返回True，否则返回Flase

```python
mystr1 = 'aaa2332'
mystr2 = '33434-'

print(mystr1.isalnum()) # True
print(mystr1.isalnum()) # False 
```

- isspace()：都是空白时，返回True

```python
mystr1 = ‘1 2 3 4’
print(mystr1.isspace()) # False 
```

# 七、列表

目标

- 列表的应用场景
- 列表的格式
- 列表的常用操作
- 列表的循环遍历
- 列表的嵌套使用

## 7.1 列表简介

**列表的应用场景**

思考：有一个人的姓名（TOM）怎么书写存储程序？

答：变量。

思考：如果一个班级100位学生，每个人的姓名都要存储，应该如何书写程序？声明100个变量吗？

答：列表即可，列表一次性可以存储多个数据。

**列表的格式**

```
[数据1，数据2，数据3，数据4.......]
```

列表可以一次性存储多个数据，且可以为不同数据类型。

##7.2 **列表的常用操作**

列表的作用是一次性存储多个数据，程序员可以对这些数据进行的操作有：**增、删、改、查。**

### 7.2.1 查找

#### 7.2.1.1 下标

```python
name_list = ['tome', 'lily', 'rose']

print(name_list[0]) # tome
print(name_list[1]) # lily
print(name_list[2]) # rose
```



#### 7.2.1.2 函数

- index()：返回指定数据所在位置的下标

1、语法

```
列表序列.index(数据，开始位置下标，结束位置下标)
```

2、快速体验

```python
name_list = ['tome', 'lily', 'rose']
print(name_list.index('lily',0,2)) # 1
```

> 注意：如果查找的数据不存在则报错



---



- count()：统计指定数据在当前列表中出现的次数。

```python
name_list = ['Tom', 'lily', 'rose']
print(name_list.count('lily')) # 1
```



---



- len()：访问列表长度，即列表中数据的个数

```python
name_list = ['Tom', 'lily', 'rose']
print(len(name_list)) # 3
```

### 7.2.2 查找数据之判断是否存在

- in：判断指定数据在某个列表序列，如果在返回True，否则返回Flase

```python
name_list = ['Tom', 'lily', 'rose']
print('lily' in name_list) # True

print('Lily' in name_list) # False
```

- not in：判断指定数据不在某个列表序列，如果不在返回True，否则返回 False

```python
name_list = ['Tom', 'lily', 'rose']
print('lily' not in name_list) # Flase

print('Lily' not in name_list) # True
```



**体验案例：**需求：查找用户输入的名字是否已经存在

```python
name_list = ['Tom', 'Lily', 'Rose']
name = input("请输入您要搜索的名字：")
if name in name_list:
    print(f'您输入的名字是{name},名字已经存在')
else:
    print(f'您输入的名字是{name},名字不存在')
```

### 7.2.3 列表添加数据

作用：增加知道数据到列表中

#### 7.2.3.1 列表添加数据之append

- append()：列表结尾追加数据

**1、语法**

```
列表序列.append(数据)
```

**2、快速体验**

```python
name_list = ['Tom', 'Lily', 'Rose']
name_list.append('JJK')
print(name_list) # ['Tom', 'Lily', 'Rose', 'JJK']
```

>列表追加数据的时候，直接在原列表里面追加了指定数据，即修改了原列表，故列表为可变类型数据。

**注意点：**如果 append（）追加的数据是一个序列，则追加整个序列到列表

```python
name_list = ['Tom', 'Lily', 'Rose']
name_list.append(['jjk','jiajikang'])
print(name_list) # ['Tom', 'Lily', 'Rose', ['jjk', 'jiajikang']]
```



#### 7.2.3.2 列表添加数据之extend

- extend（）：列表结尾追加数据，如果数据是一个序列，则将这个序列的数据逐一添加到列表。

1、语法

```
列表序列.extend(数据)
```

2、快速体验

**单个数据**

```python
name_list = ['Tom', 'Lily', 'Rose']
name_list.extend('jiajikang')
print(name_list) # ['Tom', 'Lily', 'Rose', 'j', 'i', 'a', 'j', 'i', 'k', 'a', 'n', 'g']
```

**序列数据**

```python
name_list = ['Tom', 'Lily', 'Rose']
name_list.extend(['jiajikang', 'jiajikang'])
print(name_list)  # ['Tom', 'Lily', 'Rose', 'jiajikang', 'jiajikang']
```

####7.2.3.3 列表添加数据之insert

- insert()：指定位置新增数据

**1、语法**

```
列表序列.insert(位置下标，数据)
```

**2、快速体验**

```python
name_list = ['Tom', 'Lily', 'Rose']
name_list.insert(1,"jiajiknag")
print(name_list)  # ['Tom', 'jiajiknag', 'Lily', 'Rose']
```



### 7.2.4 列表删除数据

- del 

1、语法

```
del 目标
```

2、快速体验

**删除列表**

```python
name_list = ['Tom', 'Lily', 'Rose']
def name_list
print(name_list) # 会报错

```

**删除指定数据**

```python
#del可以删除指定下标的数据
name_list = ['Tom', 'Lily', 'Rose']
del name_list[0]
print(name_list)
```



---



- pop()：删除指定下标的数据（默认为最后一个），并且返回该数据

1、语法

```
列表序列.pop(下标)
```

2、快速体验

```python
name_list = ['Tom', 'Lily', 'Rose']
del_name = name_list.pop(1)
print(del_name) # Lily
print(name_list) # ['Tom', 'Rose']
```



---



- remove()：移除列表中某个数据的第一个匹配项

1、语法

```
列表序列.remove(数据)
```

2、快速体验

```python
name_list = ['Tom', 'Lily', 'Rose']
name_list.remove('Rose')
print(name_list) # ['Tom', 'Lily']
```



---



- clear()：清空列表

```python
name_list = ['Tom', 'Lily', 'Rose']
name_list.clear()
print(name_list) # []
```



### 7.2.5 列表修改数据

- **修改指定下标数据**

```python
name_list = ['Tom', 'Lily', 'Rose']
name_list[0] = 'jiajiknag'
print(name_list) # ['jiajiknag', 'Lily', 'Rose']
```

- **逆置：reverse()**

```python
num_list = [1,2,3,4,5,6]
num_list.reverse()
print(num_list) # [6, 5, 4, 3, 2, 1]
```

- **排序**

1、语法

```python
列表序列.sort(key=None,reverse=False)
```

> 注意：reverese表示排序规则，reverse=True降序，reverse=False升序（默认）

2、快速体验

```python
list1 = [1,2,3,4,5,6,34,55,2,756,8]
list1.sort()
print(list1) # [1, 2, 2, 3, 4, 5, 6, 8, 34, 55, 756]
```





###7.2.6 列表复制数据

函数：copy()

```python
name_list1 = ['Tom', 'Lily', 'Rose']
name_list2 = name_list1.copy()
print(name_list2) # ['Tom', 'Lily', 'Rose']
```



###7.2.7 列表的循环遍历

#### 7.2.7.1 列表的循环之while

需求：依次打印列表中的各个数据

- 代码

```python
name_list1 = ['Tom', 'Lily', 'Rose']
i = 0
while i< len(name_list1):
    print(name_list1[i])
    i += 1
"""
Tom
Lily
Rose

"""
```



#### 7.2.7.2 列表的循环之for

- 代码

```python
name_list1 = ['Tom', 'Lily', 'Rose']
for i in name_list1:
    print(i)
"""
Tom
Lily
Rose

"""    
```

##7.3 列表嵌套

所谓列表嵌套指的就是一个列表里面包含了其他的子列表。

应用场景：要存储班级一、二、三三个班级学生姓名，且每个班级的学生姓名在一个列表。

```python
name_list = [['小明', '小红', '小绿'], ['Tom', 'Lily', 'Rose'], ['张三', '李四', '王五']]
```

思考：如何查找数据“李四”

```python
# 列表嵌套的时候的数据查找
# 第一步：按下标查找到李四所在的列表
print(name_list[2])
# 第二步：从李四所在的列表里面，再按下标找到数据李四
print(name_list[2][1]) # 整体，局部观察
```



---

**总和应用**

需求：有三个办公室，8位老师，8位老师随机分配到3个办公室

```python
"""
需求：有三个办公室，8位老师，8位老师随机分配到3个办公室
步骤：
    1、准备数据
       8位老师 -- 列表
       3个办公室 -- 列表嵌套
    2、分配老师到办公室
       随机分配
       就是吧老师的名字写入到办公室列表 -- 办公室列表追加老师名字数据
    3、验证是否分配成功
       打印办公室详细信息：每个办公室的人数和对应的老师名字

"""
import random
#1、准备数据
teachers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
offices = [[], [], []]

#2、分配老师到办公室 -- 取到每个老师放到办公室列表 -- 变量老师列表数据
for name in teachers:
    # 列表追加数据 -- append  extend  insert
    #xx[0] -- 不能指定是具体某个下标 -- 随机
    num = random.randint(0,2)
    offices[num].append(name)
#print(num)

#print(offices)
# 为了更贴近生活，把各个办公室子列表加一个办公室编号 1,2,3
i = 1
#3、验证是否分配成功
for office in offices:
    # 打印办公室人数 -- 子列表数据的个数 len()
    print(f'办公室{i}的人数是{len(office)},老师分别是：')
    # 打印老师的名字
    # print -- 每个子列表里面的名字个数不一定-- 遍历 -- 子列表
    for name in office:
        print(name)
```



##  7.2 列表推导式

```python
x = 'ABC'
dumny = [ord(x) for x in x]
```







# 八、元组

**目标**

- 元组的应用场景
- 定义元组
- 元组常见操作

## 8.1 元组的应用场景

思考：如果想要存储多个数据，但是这些数据是不能修改的数据，怎么做？

答：列表？列表可以一次性存储多个数据，但是列表中的数据允许更改。

```
num_list = [10,20,30]
num_list[0] = 100
```

==一个元组可以存储多个数据，元组内的数据是不能修改的。==

## 8.2 定义元组

元组特点：定义元组使用==小括号==，且==逗号==隔开各个数据，数据可以是不同的数据类型。

```python
t1 = (10,20,30) # 多个数据元组
t2 = (10,) # 单个数据元组

```

> 注意：如果定义的元组只有一个数据，那么这个数据后面也要==添加逗号==，否则数据类型为唯一的
> 这个数据的数据类型

```python
t2 = (10,)
print(type(t2)) # tuple

t3 = (20)
print(type(t3)) # int

t4 = ('hello')
print(type(t4)) # str
```



## 8.3 元组的常见操作

### 8.3.1 元组的常见操作之查找

元组数据不支持修改，只支持查找，具体如下：

- **按下标查找数据**

```python
tuple1 = ('aa', 'bb', 'cc', 'dd')
print(tuple1[0]) # aa
```

- **index()：**查找某个数据，如果数据存在返回对应的下标，否则报错，语法和列表、字符串的index方法相同。

```python
tuple1 = ('aa', 'bb', 'cc', 'dd')
print(tuple1.index('aa')) # 0
```

- **count()：**统计某个数据在当前元组出现的次数

```python
tuple1 = ('aa', 'bb', 'cc', 'dd', 'bb')
print(tuple1.count('bb')) # 2
```

- **len()：**统计元组中数据的个数

```python
tuple1 = ('aa', 'bb', 'cc', 'dd', 'bb')
print(len(tuple1)) # 5
```



### 8.3.2 元组的常见操作之修改

注意：元组内的直接数据如果修改则立即报错

```python
tuple1 = ('aa', 'bb', 'cc', 'dd', 'bb')
tuple1[0] = 'aaa'
```

但是如果元组里面有列表，修改列表里面的数据则是支持的，故自觉很重要。

```python
tuple2 =  (10,20, ['aa', 'bb', 'cc'], 50, 30)
print(tuple2[2]) # 访问到列表

tuple2[2][0] = 'aaaaaa'
print(tuple2)
"""
['aa', 'bb', 'cc']
(10, 20, ['aaaaaa', 'bb', 'cc'], 50, 30)
"""
```

# 九、字典

 **目标**

- 字典的应用场景
- 创建字典的语法
- 字典常见操作
- 字典的循环遍历

## 9.1 字典的应用场景

思考1：如果有多个数据，例如：Tom，男，20，如何快速存储？

答：列表

```
list1 = ['tom','男'，20]
```

思考2：如何查找到数据Tom'？

答：查找到下标为0的数据即可。

```
list1[0]
```

思考3：如果将来数据顺序发生变化，如下所示，还能用list1[0]访问到数据'Tom吗？

```
list1 = ['男','tom',20]
```

答：不能，数据Tom'此时下标为2

思考4：数据顺序发生变化，每个数据的下标也会随之变化，如何保证数据顺序变化前后能使用同一的
标准查找数据呢？

答：字典，字典里面的数据是以==键值对==形式出现，字典数据和数据顺序没有关系，即字典不支持下标，
后期无论数据如何变化，只需要按照对应的键的名字查找数据即可。

## 9.2 创建字典的语法

**字典特点：**

- 符号为大括号
- 数据为键值对形式出现
- 各个键值对之间用逗号隔开

```python
#有数据字典
dict1 = {'name' : 'jiajiknag', 'age':20, 'gender':'男'}
print(dict1)
#空字典
dict2 = {}
dict3 = dict() #函数创建
```

## 9.3 字典常用操作

### 9.3.1 增

**写法：**字典序列[key] = 值

**注意：**如果key存在则修改这个key对应的值；如果key不存在则新增此键值对。

```python
dict1 = {'name' : 'jiajiknag', 'age':20, 'gender':'男'}

dict1['name'] = 'jjk'
print(dict1)

dict1['id'] = 110
print(dict1) # {'name': 'jjk', 'age': 20, 'gender': '男', 'id': 110}
```

**注意：**字典为可变类型



### 9.3.2 删

- del()/del：删除字典或删除字典中指定键值对

```python
dict1 = {'name' : 'jiajiknag', 'age':20, 'gender':'男'}
#del(dict1) 
del dict1['gender']
print(dict1) # {'name': 'jiajiknag', 'age': 20}


```

- clear()：清空字典

```python
dict1 = {'name' : 'jiajiknag', 'age':20, 'gender':'男'}
dict1.clear()
print(dict1) # {}
```



### 9.3.3 改

**写法：**字典序列[key] = 值

**注意：**如果key存在则修改这个key对应的值；如果key不存在则新增此键值对。

```python
dict1 = {'name' : 'jiajiknag', 'age':20, 'gender':'男'}
dict1['name'] = 'JJK'
print(dict1) # 

dict1['ID'] = 1111
print(dict1)
```

### 9.3.4 查

#### 9.3.4.1 key值查找

```python
dict1 = {'name' : 'jiajikang', 'age':20, 'gender':'男'}
print(dict1['name']) # jiajikang
print(dict1['ID']) # 报错
```



#### 9.3.4.2 get()

- 语法

```
字典序列.get(key, 默认值)
```

- 注意：如果当前查找的key不存在则返回第二个参数（默认值），如果省略第二个参数，则返回
    None.

- 快速体验

```python
dict1 = {'name' : 'jiajikang', 'age':20, 'gender':'男'}
print(dict1.get('name')) # jiajikang
print(dict1.get('id',110)) # 110
print(dict1.get('id')) #None
```

#### 9.3.4.3 keys()

查找字典中所有的key，返回可迭代对象

```python
dict1 = {'name' : 'jiajikang', 'age':20, 'gender':'男'}
print(dict1.keys()) # dict_keys(['name', 'age', 'gender'])
```

#### 9.3.4.4 values()

查找字典中所有的value，返回可迭代对象

```python
dict1 = {'name' : 'jiajikang', 'age':20, 'gender':'男'}
print(dict1.values())# dict_values(['jiajikang', 20, '男'])
```

#### 9.3.4.5 items()

查找字典中所有的键值对，返回可迭代对象，里面的数据是元组，元组数据1是字典的key，元组数据2是字典key对应的value。

```python
dict1 = {'name' : 'jiajikang', 'age':20, 'gender':'男'}
print(dict1.items()) # dict_items([('name', 'jiajikang'), ('age', 20), ('gender', '男')])
```



## 9.4 字典的循环遍历

### 9.4.1  字典的循环遍历之key

```python
dict1 = {'name' : 'jiajikang', 'age':20, 'gender':'男'}
for key in dict1.keys():
    print(key) #
"""
name
age
gender

"""
```



###9.4.2  字典的循环遍历之value

```python
dict1 = {'name' : 'jiajikang', 'age':20, 'gender':'男'}
for value in dict1.values():
    print(value)
"""
jiajikang
20
男
"""
```

### 9.4.3  字典的循环遍历之元素

```python
dict1 = {'name' : 'jiajikang', 'age':20, 'gender':'男'}
for item in dict1.items():
    print(item)
    
"""
('name', 'jiajikang')
('age', 20)
('gender', '男')
"""
```

### 9.4.4 遍历字典的键值对

```python
dict1 = {'name' : 'jiajikang', 'age':20, 'gender':'男'}
for key, value in dict1.items():
    print(f'{key} = {value}')
    
"""
name = jiajikang
age = 20
gender = 男

"""
```

# 十、集合

创建集合使用 `{}` 或者 `set()`，但是如果要创建空集合只能使用 `set()`，因为 `{}` 用来创建空字典。

```python
s1 = {10,20,30,40,50}
print(s1)

s2 = set('abcddfdf')
print(type(s2)) # set
print(s2)

s3 = set()
print(type(s3)) # set

s4 = {}
print(type(s4)) # dict
```



## 10.1 集合常见操作

### 10.1.1 增加

- **add()**

```python
s1 = {10,20}
s1.add(100)
# 集合有去重功能，如果追加的数据是集合已有的数据，则什么事情都不做
s1.add(10)
print(s1)  # {100, 10, 20}
```

因为集合有去重功能，所以，当向集合内追加的数据是当前集合已有数据的话，则不进行任何操作。

- **update()，追加的数据是序列**

```python
s1 = {10,20}
s1.update([100,200])
s1.update('abc')
```



### 10.1.2 删除

- remove()，删除集合中指定数据，如果数据不存在则报错

```python
s1 = {10,20}
s1.remove(10)
print(s1) # 20

s1.remove(10) # 报错
print(s1)
```

- discard()，删除集合中指定数据，如果数据不存在也不会报错

```python
s1 = {10,20}
s1.discard(10)
print(s1) # {20}


s1.discard(10)
print(s1) # {20}
```

- pop()，随机删除集合中的某个数据，并返回这个数据

```python
s1 = {10,20,30,40,50}

del_num = s1.pop()
print(del_num)
print(s1)
```



###10.1.3 查找

- in：判断数据在集合序列
- not in：判断数据不在集合序列

```python
s1 = {10,20,30,40,50}
print(10 in s1) #True
print(10 not in s1) # False
```

# 十一、公共操作

**目标：**

- 运算符
- 公共方法
- 容器类型转换

## 11.1 运算符

 ![1587273639917](assets/1587273639917.png)



### 11.1.1 +

```python
str1 = 'aa'
str2 = 'bb'
#列表
list1 = [1,2]
list2 = [10,20]
# 元组
t1 = (1,2)
t2 = (10,20)
dict1 = {'name':'python'}
dict2 = {'age':30}

# +:合并
str3 = str1 + str2
print(str3)

print(list1+list2)
print(t1+t2)

# 字典不支持+操作
```

### 11.1.2 *

```python
str1 = 'a'
list1 = ['hello']
t1 = ('word',)

# *:复制
print(str1*5)
#打印10个-
print('-'*10)

print(list1*5)
print(t1*5)

"""
aaaaa
----------
['hello', 'hello', 'hello', 'hello', 'hello']
('word', 'word', 'word', 'word', 'word')

"""
```

### 11.2.3 in and not in

```python
str1 = 'aa'
str2 = 'bb'
#列表
list1 = [1,2]
list2 = [10,20]
# 元组
t1 = (1,2)
t2 = (10,20)
dict1 = {'name':'python'}
dict2 = {'age':30}

print('a' in str1) # True
print('a' not in str1)

print(10 in list2)
print(10 not in list2)

print(10 not in t1)
print(10 in t2)

print('name' in dict2)
print('name' in dict1)
```



# 十二、公共方法

 ![1587276667009](assets/1587276667009.png)

## 12.1 len()

```python
# 1、字符串
str1 = 'abdfdf'
print(len(str1))

# 2、列表
list1 = [10,20,30,40,50]

# 3、元组
t1 = (10,20,30,40,50)

# 4、集合
s1 = {10,20,30,40,50}

# 5、字典
dict1 = {'name':'jiajikang', 'age':2}

print(len(list1))
print(len(str1))
print(len(t1)) # 5
print(len(s1)) # 5
print(len(dict1)) # 2
```

## 12.2 del或者del()

```python
# 1、字符串
str1 = 'abdfdf'
# 2、列表
list1 = [10,20,30,40,50]
# 3、元组
t1 = (10,20,30,40,50)
# 4、集合
s1 = {10,20,30,40,50}
# 5、字典
dict1 = {'name':'jiajikang', 'age':2}
# del 目标 或者del(目标)
#del str1
#print(str1)

# del(list1)
# print(list1)

del(list1[0])
print(list1)

del s1
print(s1)

del dict1
print(dict1)

del dict1['name']
print(dict1)
```



## 12.3 max()和min()

```python
# 1、字符串
str1 = 'abdfdf'
# 2、列表
list1 = [10,20,30,40,50]
print(max(str1))
print(max(list1))

print(min(str1))
print(min(list1))
```

## 12.4 range(start,end,step)

```python
for i in range(1,10,1):
    print(i) # 1-9
# print(range(1,10,1)) # 返回的可迭代的对象
for i in range(1,10,2):
    print(i) # 1 3 5 7 9
    
for i in range(10):
    print(i) # 1-9
# 1、如果不写开始，默认从0开始
# 2、如果不写步长，默认为1
```

注意：range()生成的序列不包含end数字。

## 12.5 enumerate()

- 语法

```python
enumerate(可遍历对象，start=0)
```

注意：start参数用来设置遍历数据的下标的起始值，默认为0

- 快速体验

```python
list1 = ['a', 'b', 'c', 'd', 'e']
for i in enumerate(list1):
    print(i)
for index, char in enumerate(list1,start=1):
    print(f'下标是{index},对应的字符是{char}')
    
"""
(0, 'a')
(1, 'b')
(2, 'c')
(3, 'd')
(4, 'e')
"""

"""
下标是1,对应的字符是a
下标是2,对应的字符是b
下标是3,对应的字符是c
下标是4,对应的字符是d
下标是5,对应的字符是e

"""
```

说明：enumerate 返回的结果是元组，元组第一个数据是原迭代对象的数据对应的下标，元组第二个数据是元迭代对象的数据。



# 十三、容器类型的转换

## 13.1 tuple()

作用：将某个序列转换成元组

```python
list1 = [10,20,30,40,50]
s2 = {100,200,300,400,50}

print(tuple(list1))
print(tuple(s1))
```

## 13.2 list()

作用：将某个序列转换成列表

```python
t1 = ('a', 'b', 'c', 'd', 'e')
s2 = {100,200,300,400,50}

print(list(t1))
print(list(s1))

```



## 13.3 set()

作用：将某个序列转换成集合

```python
list1 = [10,20,30,40,50]
t1 = ('a', 'b', 'c', 'd', 'e')
print(set(list1))
print(set(t1))
```



# 十四、==推导式==

**目标：**

- 列表推导式
- 字典推导式
- 集合推导式

## 14.1 列表推导式

**作用：**用一个表达式创建一个有规律的列表或控制一个有规律列表。

列表推导式又叫列表生成式。

------

**快速体验：**

**while实现**

需求：创建一个0-10的列表

```python
#1、准备一个空列表
list1 = []
#2、书写循环，一次追加数字到空列表list1中
i = 0
while i<10:
    list1.append(i)
    i += 1
print(list1)
```

**for循环实现**

```python
list1 = []
for i in  range(10):
    list1.append(i)
print(list1)
```

**列表推导式实现**

```python
list1 = [i for i in range(10)]
print(list1)
```



------

**带if的列表推导式**

需求：创建0-10的偶数列表

- 方法一：range()步长实现

```python
list1 = [i for i in range(0,10,2)]
print(list1)
```

- 方法二：if实现

```python
list1 = []
for i in range(10):
    if i%2 ==0:
        list1.append(i)

list1 = [i for i in range(10) if i % 2 ==0]
print(list1)
```



------

**多个for循环实现列表推导式**

```python
# 需求：[(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

list1 = []
for i in range(1,3):
    for j in range(3):
        # 列表里面追加元组，循环前面准备一个空列表，然后这里追加元组数据到列表
        list1.append((i,j))
print(list1)

list1 = [(i,j) for i in range(1,3) for j in range(3)]

# 多for的列表推导式等同于for循环嵌套
```



## 14.2 字典推导式

思考：如果有如下两个列表：

```python
list1 = ['name', 'age', 'gender']
list2 = ['Tom', 23, 'man']
```

如何快速合并成一个字典？

**答：**字典推导式

字典推导式作用：快速合并列表为字典或提取字典中目标数据。

------

**快速体验**

1、创建一个字典：字典key是1-5数字，value是这个数字的2次方。

```python
dict1 = {i : i**2 for i in range(1,5)}
print(dict1)
"""
{1: 1, 2: 4, 3: 9, 4: 16}
"""
```

2、将两个列表合并成一个字典

```python
list1 = ['name', 'age', 'gender']
list2 = ['Tom', 23, 'man']

dict1 = {list1[i]:list2[i] for i in range(len(list1))}
print(dict1)

"""
{'name': 'Tom', 'age': 23, 'gender': 'man'}
"""
# 总结：
# 如果两个列表数据个数相同，len统计任何一个列表的长度都可以
# 如果两个列表数据个数不同，len统计数据多的列表数据个数会报错；len统计数据少的列表数据个数不会报错
```

3、提取字典中目标数据

```python
counts = {'MBP':268, 'hp':235, 'DELL':343, 'Lenovo':123,'acer':99}
# 需求：提取上述电脑数量大于200的字典数据
count1 = {key:value for key,value in counts.items() if value>=200}
print(count1)

# {'MBP': 268, 'hp': 235, 'DELL': 343}
```



## 14.3 集合推导式

需求：创建一个集合，数据为下标列表的2次方

```python
list1 = [1,1,2]
```

代码如下：

```
list1 = [1,1,2]
set1 = {i**2 for i in list1}
print(set1)
#{1, 4}
```

**注意：**集合有数据去重功能



------

**总结**

```python
#列表推导式
[xx for xx in range()]

# 字典推导式
{xx1:xx2 for ... in ...} # 注意字典是键值对存在

# 集合推导式
{xx for xx in ...}
```



# 十五、函数一

**目标：**

- 函数的作用
- 函数的使用步骤
- 函数的参数作用
- 函数的返回值作用
- 函数的说明文档
- 函数嵌套

## 15.1 函数的作用

需求：用户到ATM机取钱：

1. 输入密码后显示"选择功能"界面
2. 查询余额后显示"选择功能"界面
3. 取2000钱后显示"选择功能"界面

特点：显示选择功能”界面需要重复输出给用户，怎么实现？

函数就是将一段具有==独立功能的代码块==整合到一个整体并命名，在需要的位置==调用这个名称==即可完成对
应的需求。

函数在开发过程中，可以更高效的实现==代码重用==。


## 15.2 函数的使用步骤

### 15.2.1 定义函数

```python
def 函数名称(参数):
    代码1
    代码2
    ...
```

### 15.2.2 调用函数

```python
函数名(参数)
```

> 注意：

1、不同的需求，参数可有可无

2、在python中，函数必须==先定义后调用==

### 15.2.3 快速体验

需求：复现ATM取钱功能

1、搭建整体框架（复现需求）

```python
print('密码正确登录成功')
# 显示“选择功能”界面
print('查询余额完毕')

# 显示“选择功能”界面
print('取了2000大洋')
# 显示“选择功能”界面
```

2、确定“选择功能”界面内容

```python
print('余额查询')
print('存款')
print('取款')
```

3、封装“选择功能”

注意：一定是先定义函数，后调用函数

```python
# 封装ATM机功能选择---定义函数
def select_func():
    print('---请选择功能---')
    print('查询余额')
    print('存款')
    print('取款')
    print()
    print('---请选择功能---')
```

4、调用函数

在需要显示“选择功能”函数的位置调用函数

```python
select_func()
```

## 15.3 函数的注意事项

```python
1、先定义函数
2、后调用函数
3、函数的执行流程***
   当调用函数的时候，解释器回到定义函数的地方执行下方缩进的代码，当这些代码执行完，回到调用函数的地方继续向下执行；
   定义函数的时候，函数体内部缩进的代码并没有执行
```

## 15.4 函数的参数作用

思考：完成需求如下：一个函数完成两个数1和2的加法运算，如何书写程序？

```python
def add_num1():
    result = 1+2
    print(result)
# 调用函数
add_num1()
```

**思考：**上述add_num1函数只能完成数字和2的加法运算，如果想要这个函数变得更灵活，可以计算任
何用户指定的两个数字的和，如何书写程序？

**分析：**用户要在调用函数的时候指定具体数字，那么在定义函数的时候就需要接收用户指定的数字。函
数调用时候指定的数字和定义函数时候接收的数字即是函数的参数。

```python
#定义函数时同时定了接收用户数据的参数num1，num2 被称为形参
def add_num2(num1,num2):
    result = num1 + num2
    print(result)
# 调用函数时传入了真实的数据10和20，真实数据为实参    
add_num2(10,20) # 30
```

## 15.5 函数返回值

例如：我们去超市购物，比如买烟，给钱之后，是不是售货员会返回给我们烟这个商品，在函数中，如
果需要返回结果给用户需要使用函数返回值。

```python
def buy():
    return '烟'
# 使用变量保存函数返回值
goods = buy()
print(goods)
# reutrn返回结果给函数调用的位置
# return作用：
# 1、负责函数返回值
# 2、退出当前函数，导致return下方的所有代码（函数体内部）不执行
```

**应用**

需求：制作一个计算器，计算任意两个字数之和。

```python
def sum_num(a,b):
    return a+b
#用result变量保存函数返回值
result = sum_num(10,20)
print(result)
```

## 15.6 ==函数的说明文档==

思考：定义一个函数后，程序员如何书写程序能够快速提示这个函数的作用？

答：注释
思考：如果代码多，我们是不是需要在很多代码中找到这个函数定义的位置才能看到注释？如果想更方
便的查看函数的作用怎么办？

答：函数的说明文档

注意：函数的说明文档也叫函数的文档说明。

### 15.6.1 语法

- 定义函数的说明文档

```python
def 函数名(参数):
    """说明文档的位置"""
    代码
    ....
```

- 查看函数的说明文档

```python
help(函数名)
```

### 15.6.2 快速体验

```python
def sum_num(a,b):
    """求和函数"""
    return a+b

help(sum_num)

# 函数说明文档的高级使用
def sum_num1(a, b):
    """
    求和函数sum_num1
    :param a: 参数1
    :param b: 参数2
    :return:  返回值
    """
    return a+b
help(sum_num1)
```

## 15.7 函数的嵌套调用

所谓函数嵌套调用指的是一个函数里面又调用了另外一个函数。

```python
def testB():
    print('-------testb start------')
    print('这里是testb函数执行的代码')
    print('--------testb end-------')

def testA():
    print('------testa start--------')
    testB()
    print('------testa end----------')
testA()
```

### 15.7.1 函数嵌套调用之应用一

**1、打印一条横线**

```python
def print_line():
    print('-'*20)
```

**2、打印多条横线**

```python
def print_line():
    print('-'*20)
    
def print_lines(num):
    i = 0
    while i<=num:
        print_line()
        i += 1
print_lines(5) 
```



### 15.7.2 函数嵌套调用之应用二

1、求三个函数之和

```python
def sum_num(a,b,c):
    return a+b+c
result = sum_num(1,2,3)
print(result)

```

2、求三个数的平均值

```python
def sum_num(a,b,c):
    return a+b+c
def average_num(a,b,c):
    sumResult = sum_num(a,b,c)
    return sumResult /3
averageResult = average_num(1,2,3)
print(averageResult) # 2.0
```

# 十六、函数二

**目标：**

- 变量作用域
- 多函数程序执行流程
- 函数的返回值
- 函数的参数
- 拆包和交换两个变量的值
- 引用
- 可变和不可变类型

## 16.1 变量作用域

变量作用域指的是变量生效的范围，主要分为两类：==局部变量和全局变量==。

- **局部变量**

所谓局部变量是定义在函数体内部的变量，即只在函数体内部生效。

```python
def testA():
    a = 100
    print(a)
testA() # 100
print(a) # 报错
```

变量a是定义在 testA函数内部的变量，在函数外部访问则立即报错。

局部变量的作用：在函数体内部，临时保存数据，即当函数调用完成后，则销毁局部变量。

- **全局变量**

所谓全局变量，指的是在函数体内、外都能生效的变量。

思考：如果有一个数据，在函数A和函数B中都要使用，该怎么办？

答：将这个数据存储在一个全局变量里面。

```python
# 定义全局变量
a = 100
def testA():
    print(a) # 访问全局变量
    
def testB():
    print(a) # 访问全局变量 
testA()
testB()
```

思考：testB函数需求需改变量a的值为200，如何修改程序？

```python
# 定义全局变量
a = 100
def testA():
    print(a) # 访问全局变量
    
def testB():
    a = 200
    print(a) # 访问全局变量 
testA()
testB()
print(f'全局变量a={a}') # 100
```

思考：在 testB函数内部的a=200中的变量a是在修改全局变量a吗？

答：不是。观察上述代码发现，11行得到a的数据是100，仍然是定义全局变量a时候的值，而没有返回testB函数内部的200。综上：testB函数内部的a=200是定义了一个局部变量。

```python
# 定义全局变量
a = 100
def testA():
    print(a)  # 访问全局变量

def testB():
    # a =200 # 如果直接修改a=200,此时的a是全局还是局部a? ---局部
    # 因为在全局变量（b函数调用后）打印a得到的不是200而是100
    # 想要全局变量a 值是200
    global a # 声明全局变量
    a = 200
    print(a)  # 访问全局变量

testA()
testB()
print(a) # 200
```

## 16.2 多函数程序执行流程

一般在实际开发过程中，一个程序往往由多个函数（后面知识中会讲解类）组成，并且多个函数共享某
些数据，如下所示：

- 共用全局变量

```python
#1、定义全局吧今后
glo_num = 0

def test1():
    global glo_num
    # 修改全局变量
    glo_num = 100

def test2():
    #调用test1函数中修改后的全局变量
    print(glo_num)
#2、调用test1函数，执行函数内部代码：声明和修改全局变量
test1()
#3、调用test2函数，执行函数内部代码：打印
test2() # 100
```

## 16.3 返回值作为参数传递

- 返回值作为参数传递

```python
def test1():
    return 50

def test2(num):
    print(num)
#1、保存函数test1的返回值
result = test1()

#2、将函数返回值所在变量作为参数传递到test2函数
test2(result) # 50
```

  

## 16.4 函数的返回值

思考：如果一个函数如些两个 return（如下所示），程序如何执行？

```python
def return_num():
    return 1
    return 2
result = return_num()
print(result)#1
```

答：只执行了第一个 return，原因是因为 return可以退出当前函数，导致 return下方的代码不执行。

思考：如果一个函数要有多个返回值，该如何书写代码？

```python
def return_num():
    return 1,2
    return （10,20）
    return [100,200]
    return {'name':'python','age':30}

result = return_num()
print(result)#(1,2)是一个元组

```

注意：

1. `return a,b` 写法，返回多个数据的时候，默认是元组类型。
2. return后面可以连接列表、元组或字典，以返回多个值。



## 16.5 函数的参数

### 16.5.1 位置参数

**位置参数：**调用函数时根据函数定义的参数位置来传递参数。

```python
def users_info(name,age,gender):
    print(f'您的名字是{name},年龄是{age},性别是{gender}')
users_info('jjk',20,'男')
```

**注意：**传递和定义参数的顺序及个数必须一致

### 16.5.2 关键字参数

函数调用，通过“键=值“形式加以指定。可以让函数更加清晰、容易使用，同时也清除了参数的顺序需求。

```python
def users_info(name,age,gender):
    print(f'您的名字是{name},年龄是{age},性别是{gender}')
user_info('Rose',age=20,gender='女')
user_info('小敏',gender='男',age=20)
```

**注意：**函数调用时，如果有位置参数时，位置参数必须在关键字参数的前面但关键字参数之间不存在
先后顺序。

### 16.5.3 缺省参数

缺省参数也叫默认参数，用于定义函数，为参数提供默认值，调用函数时可不传该默认参数的值（注意：所有位置参数必须出现在默认参数前包括函数定义和调用）。

```python
def users_info(name,age,gender='男'):
    print(f'您的名字是{name},年龄是{age},性别是{gender}')
    
user_info('Rose',age=20)
user_info('小敏',age=20,gender='男')
```

注意：函数调用时，如果为缺省参数传值则修改默认参数值；否则使用这个默认值。

### 16.5.4 ==不定长参数==

不定长参数也叫可变参数。用于不确定调用的时候会传递多少个参数（不传参也可以）的场景。此时，
用包裹（packing）位置参数，或者包裹关键字参数，来进行参数传递，会显得非常方便。

- **包裹位置传递**

```python
def user_info(*args):
    print(args)

#('tom',)
user_info('tom')
#('tom',18)
user_info('tom',18)
```

==注意==：传进的所有参数都会被args变量收集，它会根据传进参数的位置合并为一个元组（tuple）
args是元组类型，这就是包裹位置传递。

- **包裹关键字传递**

```python
def user_info(**kwargs): # key word args
    print(kwargs)
    
# {'name': 'jjk', 'age': 18, 'id': 110}
user_info(name='jjk',age=18,id=110)
```

综上：无论是包裹位置传递还是包裹关键字传递，都是一个==组包==的过程。

## 16.6 拆包和交换变量值

### 16.6.1 拆包

- 拆包：元组

```python
def return_num():
    return 100,200 # 默认返回一个元组

num1,num2 = return_num()
print(num1) # 100
print(num2) # 200
```

- 拆包：字典

```python
dicts = {'name':'tom', 'age':18}
a, b =dict1
# 对字典进行拆包，取出来的是字典的key
print(a) # name
print(b) # age
print(dict1[a]) # tom
print(dict1[b]) # 18
```

### 16.6.2 交换变量值

需求：有变量 `a=10` 和 `b=20` ，交换两个变量的值。

- 方法一

借助第三变量存储数据

```python
# 1、定义中间变量
c = 0
# 2、将a的数据存储到c
c = a
# 3、将b的数据20复制到a，此时a=20
a = b
# 4、将之前c的数据10赋值到b，此时b = 10
b = c
print(a) # 20
print(b) # 10
```

- 方法二

```python
a, b = 1,2
a, b = b,a
print(a) # 2
print(b) # 1
```

### 16.6.3 引用

#### 16.6.3.1 **了解引用**

在python中，值是靠引用传递来的。

我们可以用 `id` 来判断两个变量是否为同一个值的引用。我们可以将id值理解为那块内存的地址标识。

```python
# 1、int类型
a = 1
b = a
print(b) # 1
print(id(a)) # 1617604832
print(id(b)) # 1617604832

a = 2
print(b) # 1、说明int类型为不可变类型
```

#### 16.6.3.2 可变类型

```python
#2、列表
aa = [10,20]
bb = aa

print(id(aa)) # 1470481080200
print(id(bb)) # 1470481080200

aa.append(30)
print(bb) # [10, 20, 30]  列表为可变类型

print(id(aa)) # 2125878697864
print(id(bb))  #2125878697864
```

#### 16.6.3.3 引用当做实参

```python
def test1(a):
    print(a) # 100
    print(id(a)) # 1617608000

    a += a

    print(a) # 200
    print(id(a)) # s

# int:计算前后id值不同
b = 100
test1(b)

#列表：计算前后id值不同
c = [11,12]
test1(c)

"""
[11, 12]
2728354815880
[11, 12, 11, 12]
2728354815880

"""
```

#### 16.6.3.4 可变和不可变类型

所谓可变类型与不可变类型是指：数据能够直接进行修改，如果能直接修改那么就是可变，否则是不可变。

- 可变类型

    列表

    字典

    集合

- 不可变类型

    整型

    浮点型

    字符串

    元组

# 十七、函数加强

**目标**

- 应用：学员管理系统
- 递归
- lambda表达式
- 高阶函数

## 17.1 应用：学员管理系统

**1.1 吸引简介**

需求：进入系统显示功能界面，功能如下：

- 添加学员
- 删除学员
- 修改学员信息
- 查询学员信息

系统共6个功能，用户根据自己需求选取

## 17.2 步骤分析

1、显示功能界面

2、用户输入功能序号

3、根据用户输入的功能序号，执行不能的功能（函数）

​     3.1 定义函数

​     3.2 调用函数

## 17.3 需求实现

### 17.3.1 显示功能界面

定义函数 `print_info` ，负责显示系统功能。

```python
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


# 系统功能需要循环使用，直到用户输入6，退出系统
while True:
    # 1、显示功能界面
    info_print()

    # 2、用户输入功能序号
    user_num = int(input('请输入功能序号：'))

    # 3、按照用户输入的功能序号，执行不同的界面
    # 如果用户输入1、执行添加...... ----多重判断
    if user_num == 1:
        print('添加')
    elif user_num == 2:
        print('删除')
    elif user_num == 3:
        print('修改')
    elif user_num == 4:
        print('查询')
    elif user_num == 5:
        print('显示所有')
    elif user_num == 6:
        print('退出系统')
        break
    else:
        print('输入的功能序号有误')
```

### 17.3.2 定义不同功能的函数

所有功能函数都是操作学员信息，所有存储所有学员信息应该是一个==全局变量==，数据类型为==列表==。

```
info = []
```

#### 17.3.2.1 添加学员

- 需求分析

    1、接收用户输入学员信息，并保存

    2、判断是否添加学员信息

    ​      2.1 如果学员姓名已经存在，则报错提示

    ​      2.2 如果学员姓名不存在，则准备空字典，将用户输入的数据追加的字典，再列表追加字典数据

    3、对应的if条件成立的位置调用该函数

- 代码实现

```python
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
```



#### 17.3.2.2 删除学员

- 需求分析

按用户输入的姓名进行删除

1、用户输入目标学员姓名

2、检查这个学员是否存在

​      2.1 如果存在，则列表删除这个数据

​      2.2 如果不存在，则提示“该用户不存在”

3、对应的if条件成立的位置调用该函数

- 代码实现

```python
# 删除学员信息的函数
def del_info():
    """删除学员信息"""
    # 1、用户输入目标学员姓名
    del_name = input('请输入要删除的学员姓名：')

    global info
    # 2、检查这个学员是否存在
    for i in info:
        if del_name == i['name']:
            info.remove(i)
            break
    else:
        print('该学员不存在')
    print(info)
```



#### 17.3.2.3 修改学员

- 需求分析

1、用户输入目标学员姓名

2、检查这个学员是否存在

​      2.1 如果存在，则修改这个学员的信息，例如手机号

​      2.2 如果不存在，则报错

3、对应的if条件成立的位置调用该函数

```python
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
```

#### 17.3.2.4  查询学员信息

- 需求分析

1、用户输入目标学员名称

2、检查学员是否存在

      2.1 如果存在，则显示这个学员的信息 

​      2.2 如果不存在，则报错

3、对应的if条件成立的位置调用该函数

- 代码实现

```python
def search_info():
    """查询学员信息"""
    # 1、用户输入目标学员名称
    search_name = input('请输入要查找的学员姓名：')
    global  info
    # 2、检查学员是否存在
    #    2.1 如果存在，则显示这个学员的信息
    #    2.2 如果不存在，则报错
    for i in info:
        if search_name == i['name']:
            print('查到找学习信息如下：--------')
            print(f"该学员的学号为{i['id']},姓名是{i['name']}, 手机号是{i['tel']}")
            break
    else:
        print('不存在')
    # 3、对应的if条件成立的位置调用该函数
```

#### 17.3.2.5  显示所有成员信息

- 需求分析

打印所以学员信息

- 代码实现

```python
# 显示所有学员信息
def print_all():
    """显示所有学员信息"""
    #1、打印提示字
    print('学号\t姓名\t手机号')
    #2、打印所有学员的数据
    for i in info:
        print(f"{i['id']}\t {i['name']}\t {i['tel']}")
```



#### 17.3.2.6 退出系统功能

在用户输入序号6的时候要退出系统，代码如下：

```python
elif user_num == 6:
    exit_fla = input('确定要退出系统 yes or no:')
    if exit_fla == 'yes':
        break
```



# 十八、递归

## 18.1 递归的应用场景

**递归是一种编程思想，应用场景：**

1. 在我们日常开发中，如果要遍历一个文件夹下面所有的文件，通常会使用递归来实现；
2. 在后续的算法学习中，很多算法都离不开递归，例如：快速排序。

## 18.2 递归的特点

- 函数内部自己调用自己
- 必须有出口

## 18.3 应用：3以内数字累加和

虽然方法很多（sun(range(4)),while等实现），但是您能想到递归的方法嘛？？？滋滋

```python
#3+2+1
def sum_numbers(num):
    # 1、如果是1，直返返回1 -- 出口
    if num ==1:
        return  1
    # 2、如果不是1， 重复执行累加并返回结果
    return num + sum_numbers(num-1)
sum_result = sum_numbers(3)
print(sum_result)
```

 ![1587447724171](assets/1587447724171.png)

# 十九、lambda表达式

## 19.1 lambda的应用场景

如果一个函数有一个返回值，并且只有一句代码，可以使用lambda简化

## 19.2 lambda语法

```python
lambda 参数列表 ： 表达式
```

**注意：**

1.  lambda表达式的参数可有可无，函数的参数在 lambda表达式中完全适用。
2.  lambda表达式能接收任何数量的参数但只能返回一个表达式的值。

**快速入门：**

```python
#需求：函数 返回值100
def fn1():
    return 200
result = fn1()
print(result)


# lambda 匿名函数
# lambda 参数列表 ：表达式
fn2 = lambda : 100
print(fn2) # lambda内存地址
#100返回值 调用函数
print(fn2())
```

**注意：**直接打印 lambda表达式，输出的是此 lambda的内存地址

## 19.3 实例

### 19.3.1 计算a+b

```python
def add(a,b):
    return a+b
result = add(1,2)
print(result)

```

不难发现代码太多了。

### 19.3.2 lambda实现

```python
fn1 = lambda a,b : a+b
print(fn1(1,2))
```

## 19.4 lambda参数

### 19.4.1 无参数

```python
fn1 = lambda : 100
print(fn1()) # 100
```

### 19.4.2 一个参数

```python
fn1 = lambda a:a
print(fn1('hello word'))
```



### 19.4.3 默认参数

```python
fn1 = lambda a,b,c=100:a+b+c
print(fn1(10,20)) # 100
```



### 19.4.4 可变参数：*args

参数个数不定，根据程序员输入界定

```python
fn1 = lambda *args: args
print(fn1(10,20,30))
```

**注意：**这里可变参数传入到lambda之后，返回值为==元组==

### 19.4.5 可变参数：**kwargs

```python
fn1 = lambda **kwargs :kwargs
print(fn1(name='python',arg=20))
```

**注意：**这里可变参数传入到lambda之后，返回值为==字典==

## 19.5 lambda应用

### 19.5.1 带判断的lambda

```python
fn1 = lambda a, b: a if a>b else b
print(fn1(1,2))
```



### 19.5.2 列表数据按字典key的值排序

```python
students = [
    {'name':'jjk', 'age':20},
    {'name':'ROSE', 'age':18},
    {'name':'Jack', 'age':23}
]

#按name值升序排列
students.sort(key=lambda x:x['name'])
print(students)

#按name值升序排列
students.sort(key=lambda x : x['name'],reverse=True)
print(students)

# 按age值升序排序
students.sort(key=lambda x : x['age'])
print(students)
```



# 二十、高阶函数

==把函数作为参数传入==，这样的函数称为高阶函数，高阶函数是函数式编程的体现。函数式编程就是指这种高度抽象的编程范式。

## 20.1 ==体验高阶函数==

在python中，`abs()` 函数可以完成对数字求绝对值计算

```python
abs(-10) # 10
```

`round()` 函数可以完成对数字的四舍五入计算

```python
round(1.2) # 1
round(1.9) # 2
```

需求：任意两个数字，按照指定要求整理数字后再进行求和计算。

- **方法1**

```python
def add_num(a,b):
    return abs(a) + abs(b)
result = add_num(-1,2)
print(result) # 3
```

- **方法2**：f是第三个参数，用来接收将来传入的函数

```python
def sum_num(a,b,f):
    return f(a) +f(b)
result = sum_num(-1,2,abs)
print(result) #3

result2 = sum_num(1.1,1.3,round)
print(result2)
```

注意：两种方法对比之后，发现，方法2的代码会更加简洁，函数灵活性更高。

函数式编程大量使用函数，减少了代码的重复，因此程序比较短，开发速度较快。

## 20.2 内置高阶函数

### 20.2.1 map()

`map(func,lst)` ，将传入的函数变量func作用到st变量的每个元素中，并将结果组成新的列表（Python2）/
迭代器（Python3）返回。

需求：计算 `1ist1` 序列中各个数字的2次方。

```python
list1 = [1,2,3,4,5]
def func(x):
    return x**2

result = map(func,list1)

print(result) # <map object at 0x0000024DA11BC438>
print(list(result)) # [1, 4, 9, 16, 25]
"""
1、准备列表
2、准备2次方计算的函数
3、调用map
"""
```



### 20.2.2 reduce()

`reduce(func,lst)`，其中func必须有两个参数。每次func计算的结果继续和序列的下一个元素做累计计算。

注意：`reduce()` 传入的参数func必须接收**2个参数。**

需求：计算 `list1` 序列中各个数字的累加和

```python
import functools
list1 = [1,2,3,4,5]
def func(a,b):
    return  a+b

result = functools.reduce(func,list1)
print(result) # 15
```



### 20.2.3 filter()

`filter(func,lst)` 函数用于过滤序列，过滤掉不符合条件的元素，返回一个filter对象。如果要转换为列表，可以使用 `list()` 来转换。

```python
list1 = [1,2,3,4,5,6,7,8,9,10]

def func(x):
    return x %2 ==0 # 求偶数

result = filter(func,list1)
print(result) # <filter object at 0x000002015D4AC438>
print(list(result)) # [2, 4, 6, 8, 10]
```

## 20.3 总结

- 递归

    函数内部自己调用自己

    必须有出口

- lambda

    语法

    ```python
    lambda 参数列表 ： 表达式
    ```

    lambda的参数形式

    无参数

    ```python
    lambda : 表达式
    ```

    一个参数

    ```python
    lambda 参数：表达式
    ```

    默认参数

    ```python
    lambda key= value:表达式
    ```

    不定长位置参数

    ```python
    lambda *args : 表达式
    ```

    不定长关键字参数

    ```python
    lambda **kwargs:表达式
    ```

- 高阶函数

    作用：把函数作为参数传入，简化代码

    内置高阶函数：map()，reduce()，filter()



# 二十一、文件

**目标**

- 文件操作的作用

- 文件的基本操作

    打开

    读取

    关闭

- 文件备份

- 文件和文件夹的操作

## 21.1 文件操作的作用

**思考：**什么是文件？文件操作包含什么？

**答：**打开、关闭、读、写、复制

**思考：**文件操作的的作用是什么？

**答：**读取内容、写入内容、备份内

**总结：**文件操作的作用就是把一些内容数据）存储存放起来，可以让程序下一次执行的时候直接使
用，而不必重新制作一份，省时省力。

---

## 21.2 文件的基本操作

### 21.2.1 文件操作步骤

1、打开文件

2、读写等操作

3、关闭文件

注意：可以只打开和关闭文件，不进行任何读写操作。

```python
f = open('test.txt','w')
f.write('aaa')
f.close()
```



----

**1、打开**

在python，使用open函数，可以打开一个已经存在的文件，或者创建一个新文件，语法如下：

```python
open(name,mode)
```

name：是要打开的目标文件名的字符串（可以包含文件所在的具体路径）。

mode：设置打开文件的模式（访问模式：只读、写入、追加等。

**2、打开文件模式之读访问模式**

 ![image-20200422145841750](assets/image-20200422145841750.png)

```python
# r 如果文件不存在，就会报错;r只是读
f = open('test.txt','r')
f.close()

# w 如果文件不存在，新建文件;w会覆盖式写入
f = open('test.txt','w')
f.write('aa')
f.close()

# a 追加，如果文件不存在，新建文件；会以追加的方式写入文件。
f = open('text.txt','a')
f.write('bbbb')
f.close()

# 访问模式参数是否可以省略   如果省略表示访问默认为r，
f = open('test.txt')
f.close()
```

### 21.2.2 读

- read()

```
文件对象.read(num)
```

num表示要从文件中读取的数据的长度（单位是字节），如果没有传入num，那么就表示读取文
件中所有的数据。

```python
f = open('test.txt')
#content = f.read()
content = f.read(2)
print(content)

f.close()
```

1、文件内容如果换行，底层有\n,会有字节占位，导致read书写参数读取出来的眼睛看到的个数和参数值不匹配。

2、read()不写参数读取所有内容。

----

- readlines()

readlines可以按照行的方式把整个文件中的内容进行一次性读取，并且返回的是一个列表，其中每一行
的数据为一个元素。

```python
f = open('test.txt','r')
content = f.readlines()
print(content) # ['aaa\n', 'bbb\n', 'ccc']

f.close() 
```

---

- readline()

readline()一次读取一行内容

```python
f = open('test.txt','r')
content = f.readline()
print(f'第一行：{content}')

content = f.readline()
print(f'第二行：{content}')

f.close()
"""
第一行：aaa
第二行：bbb
"""
```

### 21.2.3 访问模式的特点

```python
# 1、r+ 和 w+ a+区别
# 2、文件指针对数据读取的影响

# r+：r没有该文件则会报错，文件指针在开头，所以能读取出来数据
f = open('test.txt', 'r+')
# w+：没有该文件会新建该文件，w特点：文件指针在开头，用新内容覆盖原内容
f = open('test.txt', 'w+')

#a+：没有该文件会新建该文件；文件指针在结尾，无法读取数据（文件指针后面没有数据）
f = open('test.txt', 'a+')

con  =f.read()
print(con)
f.close()
```

### 21.2.4 seek()

**作用：**用来移动文件指针

**语法如下：**

```python
文件对象.seek(偏移量，起始位置)
```

> 起始位置：
>
> - 0：文件开头
> - 1：当前位置
> - 2：文件结尾



```python
"""
语法：文件对象.seek(偏移量，起始位置) 0开头1当前2结尾
目标：
    1. r改变文件指针位置：改变读取数据开始位置或把文件指针放结尾（无法读取数据）
    2. a改变文件指针位置，做到可以读取出来数据
"""
f = open('test.txt','r+')
# 1、改变读取数据起始位置
# f.seek(2,0)
# 1、把文件指针放结尾（无法读取数据）
# f.seek(0,2)

f = open('test.txt','a+')
#2. a改变文件指针位置，做到可以读取出来数据
f.seek(0,0)


con = f.read()
print(con)
f.close()

```

## 21.3 文件备份

###21.3.1 实现

需求：用户输入当前目录下任意文件名，程序完成对该文件的备份功能（备份文件名为xx[备份]后缀，例
如：test[备份].txt）。

**步骤**

1. 接收用户输入的文件名
2. 规划备份文件名
3. 备份文件写入数据

**代码实现**

1、接收用户输入目标文件名

```python
old_name = input('请输入您要备份的文件名：')
```

2、规划备份文件名

​      2.1 提取目标文件后缀

​      2.2 组织备份的文件名，xx[备份]后缀

```python
# 2. 规划备份文件名
# 2.1 提取目标文件后缀
# == 找到名字中的点 -- 名字和后缀分离--最右侧的点才是后缀的点 -- 字符串查找某个子串rfind
index = old_name.rfind('.') # .
print(index)

# 2.2 组织备份的文件名，xx[备份]后缀   就文件名+[备份]+后缀
# 原名字就是字符串中的一部分子串 -- 切片[开始：结束：步长]
# print(old_name[:index])
# print(old_name[index:])
new_name = old_name[:index] + '[备份]' + old_name[index:]
print(new_name)

```

3、备份文件写入数据

3.1 打开源文件和备份文件

3.2 将源文件数据写入备份文件

3.3 关闭文件

```python
# 3. 备份文件写入数据
# 3.1 打开文件
old_f = open(old_name,'rb')
new_f = open(new_name,'wb')

# 3.2 将原文件数据写入备份文件
# 如果不确定文件大仙，循环读取写入，当读取出来的数据没有了终止循环
while True:
    con = old_f.read(1024)
    if len(con) ==0:
        break
    new_f.write(con)

# 3.3 关闭文件
old_f.close()
new_f.close()
```

### 21.3.2 思考

如果用户输入.txt，这是一个无效文件，程序如何更改才能限制只有有效的文件名才能备份？

答：添加条件判断即可。

```python
old_name = input('请输入您要备份的文件名：')
index = old_name.rfind('.')

if index>0:
    postfix = old_name[index:]
new_name = old_name[:index] + '[备份]' +postfix

old_f = open(old_name, 'rb')
new_f = open(new_name, 'wb')

while True:
    con = old_f.read(1023)
    if len(con) == 0:
        break
    new_f.write(con)
 # 3.3 关闭文件
old_f.close()
new_f.close()   
```



# 二十二、文件函数操作

在 Python中文件和文件夹的操作要借助os模块里面的相关功能，具体步骤如下：

1、导入os模块

```
import os
```

2、使用os模块相关功能

```
os.函数名()
```

##  22.1 文件操作

### 22.1.1 文件重命名

```python
# os.rename(目标文件名，新文件名)
import os

# 1、rename():重命名
os.rename('test.txt', 'text.txt')
```



### 22.1.2 删除文件

```python
# 2、renove():删除文件
os.remove('test[备份].txt')
```



## 22.2 文件夹操作

### 22.2.1 创建文件夹

```python
os.mkdir(文件夹名字)
import os
os.mkdir('aa')
```



### 22.2.2 删除文件夹

```python
os,rmdir(文件夹名字)
import os
os.rmdir('aa')
```



### 22.2.3 获取当前目录

```python 
os.getcwd()
import os
print(os.getcwd()) # F:\Pycharm\Pycharm_workstation\python系统学习
```



### 22.2.4 改变默认目录

```python
os.chdir(目录)
import os
# 需求：在aa里面创建bb文件夹：1、切换到aa。 2创建bb
os.mkdir('aa')
os.chdir('aa')
os.mkdir('bb')

```



### 22.2.5 获取目录列表

```python
os.listdir(目录)
import os
# listdir():获取某个文件夹下所有文件，返回一个列表
print(os.listdir()) #
print(os.listdir('aa'))# 获取aa文件夹下。。。。
```

 ## 22.3 应用案例

需求：批量修改文件名，既可添加指定字符串，又能删除指定字符串。

- 步骤

    1、设置添加删除字符串的的标识

    2、获取指定目录的所有文件

    3、将原有文件名添加/删除指定字符串，构造新名字

    4、os. rename（）重命名

- 代码

```python
import os
# 1、找到所有文件，获取指定文件夹的目录列表 -- listdir()
file_list = os.listdir()
print(file_list)

# 2、构造名字
for i in file_list:
    # new_name = 'python_'+原文件i
    new_name = 'python_' + i
    # 3、重命名
    os.rename(new_name)
```

```python
# 1、将指定文件夹所有文件重命名 python xxx
# 2、删除python_ 重命名：

import os
# 构造条件的数据
flag = 1

# 1、找到所有文件，获取指定文件夹的目录列表 -- listdir()
file_list = os.listdir()
print(file_list)

# 2、构造名字
for i in file_list:
    if flag ==1:
        # new_name = 'python_'+原文件i
        new_name = 'python_' + i
    #
    elif flag ==2:
        # 删除前缀
        num = len('python_')
        new_name = i[num:]
    #  3、重命名
    os.rename(new_name)
```

## 22.4 总结

- **文件操作步骤**

    打开

    ```
    文件对象= open(目标文件，访问模式)
    ```

    操作：读

    ```
    文件对象.read()
    文件对象.readlines()
    文件对象.readline()
    ```

    操作：写

    ```
    文件对象.write()
    ```

    操作：seek()

    关闭

    ```
    文件对象.close()
    ```

- **主要访问模式**

    w：写，文件不存在则新建该文件

    r：读，文件不存在则报错

    a：追加

- **文件和文件夹操作**

    重命名：os.rename()

    获取当前目录：os.getcwd()

    获取目录列表：os.listdir()



# 二十三、面向对象基础

**目标**

- 理解面向对象
- 类和对象
- 添加和获取对象属性
- 魔法方法



---

## 23.1 理解面向对象

面向对象是一种抽象化的编程思想，很多编程语言中都有的一种思想。

例如：洗衣服

思考：几种途径可以完成洗衣服？

答：手洗和机洗

手洗：找盆-放水-加洗衣粉-浸泡-搓洗-拧水-倒水-漂洗N次-拧干-晾晒。

机洗：打开洗衣机-放衣服-加洗衣粉-按下开始按钮-晾晒。

思考：对比两种洗衣服途径，发现了什么？

答：机洗更简单

思考：机洗，只需要找到一台洗衣机，加入简单操作就可以完成洗衣服的工作，而不需要关心洗衣机内
部发生了什么事情。

总结：<font color=red>面向对象就是将编程当成是一个事物，对外界来说，事物是直接使用的，不用去管他内部的情况。而编程就是设置事物能够做什么事。</font>

---

## 23.2 类和对象

思考：洗衣机洗衣服描述过程中，洗衣机其实就是一个事物，即对象，洗衣机对象哪来的呢？

答：洗衣机是由工厂工人制作出来。

思考：工厂工人怎么制作出的洗衣机？

答：工人根据设计师设计的功能图纸制作洗衣机。

总结：图纸→洗衣机→洗衣服。

在面向对象编程过程中，有两个重要组成部分：==类和对象==。

==类和对象的关系：用类去创建一个对象。==

## 23.3 理解类和对象

### 23.3.1 类

类是对一系列具有相同==特征==和==行为==的事物的统称，是一个==抽象的概念==，不是真实存在的事物。

- 特征即是属性
- 行为即是方法

类比如是制造洗衣机时要用到的图纸，也就是说==类是用来创建对象==。

### 23.3.2 对象

对象是类创建出来的真实存在的事物，例如：洗衣机。

==注意==：开发中，先有类，再有对象。



## 23.4 面向对象实现方法

### 23.4.1 定义类

- 语法

```python
class 类名():
    代码
    .....

```

注意：类名要满足标识符命名规则，同时遵循==大驼峰命名习惯==

- 体验

```python
class Washer():
    def wash(self):
        print("我会洗衣服")
```

- 拓展：经典类

```python
class 类名：
    代码
    ....
```

### 23.4.2 创建对象

对象又名实例

- 语法

```
对象名 = 类名()
```

- 体验

```python
haier1 = Washer() # 创建对象
print(haier1) # <__main__.Washer object at 0x00000194F1331160>
# 使用wash功能 -- 实例方法/对象方法 -- 对象名.wash()
haier1.wash()
```

### 23.4.3 ==self==

==self指的是调用该函数的对象==

```python
# 1、定义类
class Washer():
    def wash(self):
        print('我会洗衣服')
        print(self) # <__main__.Washer object at 0x0000021B3A5EE160>

# 2、创建对象
haier1 = Washer()
print(haier1)  # <__main__.Washer object at 0x000002BB8EA31160>

haier1.wash()
# 由于打印对象和打印self得到的内存地址相同，所以self 指的是调用该函数的对象
```

### 23.4.4 一个类创建多个对象

```python
# 1、一个类可以创建多个对象
# 2、多个对象都调用函数的时候，self地址是否相同 ---不相同

# 1、定义类
class Washer():
    def wash(self):
        print('我会洗衣服')
        print(self) # <__main__.Washer object at 0x0000021B3A5EE160>

# 2、创建对象
haier1 = Washer()
haier1.wash()

haier2 = Washer()
haier2.wash() #
```

### 23.4.5==扩展经典类和新式类==

- **拓展1：**经典类或旧式类

不由任意内置类型派生出的类，称之为经典类。

```python
class 类名：
    ....
```

- **拓展2：**新式类

```python
class 类名(object):
    代码
    ....
```

Python面向对象的继承指的是多个类之间的所属关系，即子类默认继承父类的所有属性的方法，具体如





## 23.5 添加和获取对象属性

属性即是特征，比如：洗衣机的宽度、高度、重量

对象属性既可以在类外面添加和获取，也能在类里面添加和获取。

---

### 23.5.1 类外面添加对象属性

- 语法

```
对象名.属性名 = 值
```

- 体验

```python
haier1.width =500
haier1.height = 500
```



### 23.5.2 类外面获取对象属性

- 语法

```
对象名.属性名
```

- 体验

```python
print(f'haier1洗衣机的宽度是{haier1.width}')
print(f'haier1洗衣机的高度是{haier1.height}')
```

### 23.5.3  类里面获取对象属性

- 语法

```python
self.属性名
```

- 体验

```python
# 1、定义类
class Washer():
    def wash(self):
        print('我会洗衣服')
    # 获取对象属性
    def print_info(self):
        """self.属性名"""
        #print(self.width)
        # 在类里面定义一个实例方法
        print(f'洗衣机的宽度是{self.width}')
        print(f'洗衣机的高度是{self.heigth}')

haier1 = Washer()

# 添加属性
haier1.width = 400
haier1.heigth = 500

# 对象调用方法
haier1.print_info()
```



## 23.6 ==魔法方法==

在python中，`__xx__()` 的函数叫做魔法方法，指的是具有特殊功能的函数。

### 23.6.1 `__init__()`

#### 23.6.1.1 体验 `__init__()`

思考：洗衣机的宽度高度是与生俱来的属性，可不可以在先产过程中就赋予这些属性呢？

答：理应如此。

`__init__()` ==方法的作用：初始化对象==

```python
class Washer():
     # 定义__init__，添加实例属性(通常是创建类时候，与生俱来的属性)
     def __init__(self):
         # 添加实例属性
         self.width = 400
         self.height = 500
     def print_info(self):
         # 类里面调用实例属性
         print(f'洗衣机的宽度是{self.width},高度是{self.height}')

haier1 = Washer() # 创建对象
haier1.print_info() # 调用实例对象
```

> 注意：====
>
> - `__init__()` 方法，在创建一个对象时默认被调用，不需要手动调用
> - `__init__(self)` 中的self参数，不需要开发者传递， python解释器会自动把当前的对象引
>     用传递过去。



#### 23.6.1.2 带参数的 `__init__()`

思考：一个类可以创建多个对象，如何对不同的对象设置不同的初始化属性那？

答：传参数。

---

```python
# 定义类：带参数的__init__：宽度和高度；实例方法：调用实例属性
class Washer():
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def print_info(self):
        print(f'洗衣机的宽度是{self.width}')
        print(f'洗衣机的高度是{self.height}')

# 创建对象，创建多个对象且属性值不同；调用实例方法
haier1 = Washer(10,20) # 创建对象
haier1.print_info() # 实例化对象

haier2 = Washer(10,30) # 创建对象
haier2.print_info() # 实例化对象

```



### 23.6.2 `__str__()` 

当使用==print输出对象的时候==，默认打印对象的==内存地址==。如果类定义了 `__str__()` 方法，那么就会打印从这个方法中return的数据。

```python
class Washer():
    def __init__(self,width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return '这是海尔洗衣机说明书'

haier1 = Washer(10,20)
print(haier1) # 这是海尔洗衣机说明书
```



### 23.6.3 `__del__()`

当删除对象时候，python解释器也会默认调用 `__del__()` 方法。

```python
class Washer():
    def __init__(self,width, height):
        self.width = width
        self.height = height

    def __del__(self):
        print(f'{self}对象已经被删除') # <__main__.Washer object at 0x0000020A40431198>对象已经被删除

haier1 = Washer(10,20)
del haier1 # 
```

## 23.7 综合应用

###23.7.1烤地瓜

#### 23.7.1.1 需求

**需求主线：**

1、被烤的时间和对应的地瓜状态

​      0-3分钟：生的

​      3-5分钟：半生不熟

​      5-8分钟：熟的

​      超过8分钟：烤糊了

2、添加的调料

​      用户可以按照自己的意愿添加调料

#### 23.7.1.2 步骤分析

需求涉及一个事物：地瓜，故案例涉及一个类：地瓜类

**定义类**

- 地瓜的属性

    被烤的时间

    地瓜的状态

    添加的调料

- 地瓜的方法

    被烤

    ​        用户根据意愿设定每次烤地瓜的时间

    ​        判断地瓜被烤的总时间是在哪个区间，修改地瓜状态

    添加调料

    ​        用户根据意愿设定添加的调料

    ​        将用户添加的调料存储

- 显示对象信息

----

#### 23.7.1.3 具体实现

- 地瓜属性

    定义地瓜初始化属性、后期根据程序推荐更新实例属性

```python
# 1、定义类：初始化属性、被烤和添加调料的方法、显示对象信息的str
class SweetPotato():
    def __init__(self):
        # 被烤的时间
        self.cook_time = 0
        # 地瓜的状态
        self.cook_static = '生的'
        # 调料列表
        self.condiments = []
# 2、创建对象并调用 对应的实例方法
```

- 定义烤地瓜方法

```python
# 1、定义类：初始化属性、被烤和添加调料的方法、显示对象信息的str
class SweetPotato():
    .....
    
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
# 2、创建对象并调用 对应的实例方法
```

- 书写str魔法方法，用于输出对象状态

```python
class SweetPotato():
    ....
    
    def __str__(self):
        return f'这个地瓜的被烤过时间是{self.cook_time},状态是{self.cook_static}'
```

- 创建对象，测试实例属性和实例方法

```python
# 2、创建对象并调用 对应的实例方法
digua1 = SweetPotato() # 创建对象
print(digua1) # 打印对象--打印的是魔法方法str

digua1.cook(2)
print(digua1)
"""
这个地瓜的被烤过时间是0,状态是生的
这个地瓜的被烤过时间是2,状态是生的
这个地瓜的被烤过时间是4,状态是半生不熟

"""
```

- 定义添加调料方法，并调用该实例方法

```python
# 1、定义类：初始化属性、被烤和添加调料的方法、显示对象信息的str
class SweetPotato():
    ...
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

"""
这个地瓜的被烤过时间是0,状态是生的,调料有[]
这个地瓜的被烤过时间是2,状态是生的,调料有['辣椒面']
这个地瓜的被烤过时间是4,状态是半生不熟,调料有['辣椒面', '酱油']
"""
```



### 23.7.2 搬家具

将小于房子剩余面积的家具搬放到房子中

#### 23.7.2.1 步骤分析

需求涉及两个事物：房子 和 家具，故被案例涉及两个类：房子类 和 家具类

- 房子类

    实例属性

    ​        房子占地面积

    ​        房子地理位置

    ​       房子剩余面积

    ​       房子内家具列表

    实例方法

    ​       容纳家具

    显示房屋信息

- 家具类

    家具名称

    家具占地面积

    

#### 23.7.2.2 具体实现

**创建对象并调用相关方法**

- 家具类

```python
class Furniture():
    def __init__(self,name,area):
        # 家具名字
        self.name = name
        # 家具占地面积
        self.area = area
        

```



- 房子类

```python
# 房子类
class Home():

    def __init__(self,address,area):
        # 地理位置
        self.address = address
        # 房屋面积
        self.area = area
        # 剩余面积
        self.free_area = area
        # 家具列表
        self.furniture = []

    def __str__(self):
        return f'房子坐落于{self.address},占地面积{self.area},剩余面积{self.free_area},家具有{self.furniture}'
```



- 容纳家具

```python
    def add_furniture(self,item):
        """容纳家具"""
        # 如果家具占地面积<=房子剩余面积：可以搬入（家具列表添加家具名字，并且房子剩余面积更新）
        # 房屋剩余面积-该家具的占地面积
        # 否则：提示用户家具太大，剩余面积不足，无法容纳
        if item.area <= self.free_area:
            self.furniture.append(item.name)
            self.free_area -= item.area
        else:
            print('用户家具太大，剩余面积不足，无法容纳')
```

**所以源码：**

```python
# 家具类
class Furniture():
    def __init__(self,name,area):
        # 家具名字
        self.name = name
        # 家具占地面积
        self.area = area

# 房子类
class Home():

    def __init__(self,address,area):
        # 地理位置
        self.address = address
        # 房屋面积
        self.area = area
        # 剩余面积
        self.free_area = area
        # 家具列表
        self.furniture = []

    def __str__(self):
        return f'房子坐落于{self.address},占地面积{self.area},剩余面积{self.free_area},家具有{self.furniture}'

    def add_furniture(self,item):
        """容纳家具"""
        # 如果家具占地面积<=房子剩余面积：可以搬入（家具列表添加家具名字，并且房子剩余面积更新）
        # 房屋剩余面积-该家具的占地面积
        # 否则：提示用户家具太大，剩余面积不足，无法容纳
        if item.area <= self.free_area:
            self.furniture.append(item.name)
            self.free_area -= item.area
        else:
            print('用户家具太大，剩余面积不足，无法容纳')

# 双人床
bed = Furniture('双人床', 6)
sofa = Furniture('沙发',10)

# 房子1：北京，1000
jia1 = Home('北京',1000)
print(jia1)

jia1.add_furniture(bed)
print(jia1)

ball = Furniture('篮球场', 2000)
jia1.add_furniture(ball)
print(jia1)
```



# 二十四、==继承==

**目标**

- 继承的概念
- 单继承
- 多继承
- 子类重写父类的同名属性和方法
- 子类调用父类的同名属性和方法
- 多层继承
- super()
- 私有属性和私有方法



## 24.1 体验继承

- **拓展1：**经典类或旧式类

不由任意内置类型派生出的类，称之为经典类。

```python
class 类名：
    ....
```

- **拓展2：**新式类

```python
class 类名(object):
    代码
    ....
```

Python面向对象的继承指的是多个类之间的所属关系，即子类默认继承父类的所有属性的方法，具体如

```python
# 实例属性
# 实例方法
# 继承：子类默认继承父类的所有属性和方法
# 1、定义父类
class A(object):
    def __init__(self):
        self.num = 1

    def info_print(self):
        print(self.num)

# 2、定义子类，继承父类
class B(A):
    pass

# 3、创建对象，验证结论
result = B()
result.info_print() # 1
```

==在 Python中，所有类默认继承object类， object类是顶级类或基类；其他子类叫做派生类。==



---



## 24.2 单继承

> 故事主线：一个煎饼果子老师傅，在煎饼果子界摸爬滚打多年，研发了一套精湛的摊煎饼果子的技术。师父要把这套技术传授给他的唯一的最得意的徒弟。



分析：徒弟是不是要继承师父的所有技术？

```python
# 1、师傅类：属性和方法
class Master(object):
    def __init__(self):
        self.kongfu = '古法煎饼果子配方'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

# 2、徒弟类：继承师傅类
class Prentice(Master):
    pass

# 3、用徒弟类创建对象，调用实例属性和方法结论验证
daqiu = Prentice()
print(daqiu.kongfu)
daqiu.make_cake()

"""
古法煎饼果子配方
运用古法煎饼果子配方制作煎饼果子
"""
```



## 24.3 多继承

> 故事推进：daqiu是个爱学习的好孩子想学习更多的煎饼果子技术，于是，在百度搜索到jjk程序员，报班学习煎饼果子技术。

所谓多继承意思就是一个类同时继承了多个父类。

```python
# 1、师傅类：属性和方法
class Master(object):
    def __init__(self):
        self.kongfu = '古法煎饼果子配方'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

#为了验证我们的多继承，添加school父类
class School(object):
    def __init__(self):
        self.kongfu = 'jjk煎饼果子配方'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

# 2、徒弟类：继承师傅类 和 学校类
class Prentice(Master,School): # 想要继承谁，就把谁写在第一个位置
    pass

# 3、用徒弟类创建对象，调用实例属性和方法结论验证
daqiu = Prentice()

print(daqiu.kongfu)

daqiu.make_cake()
#结论：如果一个类继承多个父类，优先继承第一个父类的同名属性和方法

```

==注意：当一个类有多个父类的时候，默认使用第一个父类的同名属性和方法。==



----



## 24.4 子类重写父类同名方法和属性

> 故事：daqiu掌握了师父和培训的技术后，自己潜心钻研出自己的独门配方的一套全新的煎饼果子
> 技术。

```python
# 1、师傅类：属性和方法
class Master(object):
    def __init__(self):
        self.kongfu = '古法煎饼果子配方'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

#为了验证我们的多继承，添加school父类
class School(object):
    def __init__(self):
        self.kongfu = 'jjk煎饼果子配方'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

# 2、徒弟类：继承师傅类 和 学校类， 添加和父类同名的属性和方法
class Prentice(Master,School): # 想要继承谁，就把谁写在第一个位置
    def __init__(self):
        self.kongfu = '独创的煎饼果子技术'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

# 3、用徒弟类创建对象，调用实例属性和方法结论验证
daqiu = Prentice()

print(daqiu.kongfu)

daqiu.make_cake()

#结论：如果子类和父类拥有同名属性和方法，子类创建对象调用属性和方法的时候，调用到的是子类里面的同名属性和方法。

```

==子类和父类具有同名属性和方法，默认使用子类的同名属性和方法。==

## 24.5 拓展 `__mro__` 顺序

`__mro_` ：查看某个类的继承关系

```python
# 1、师傅类：属性和方法
class Master(object):
    def __init__(self):
        self.kongfu = '古法煎饼果子配方'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

#为了验证我们的多继承，添加school父类
class School(object):
    def __init__(self):
        self.kongfu = 'jjk煎饼果子配方'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

# 2、徒弟类：继承师傅类 和 学校类， 添加和父类同名的属性和方法
class Prentice(Master,School): # 想要继承谁，就把谁写在第一个位置
    def __init__(self):
        self.kongfu = '独创的煎饼果子技术'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

# 3、用徒弟类创建对象，调用实例属性和方法结论验证
daqiu = Prentice()

print(daqiu.kongfu)

daqiu.make_cake()
#结论：如果一个类继承多个父类，优先继承第一个父类的同名属性和方法

# (<class '__main__.Prentice'>, <class '__main__.Master'>, <class '__main__.School'>, <class 'object'>)
print(Prentice.__mro__) 
```



## 24.6 子类调用父类的同名方法和属性

> 故事：很多顾客都希望也能吃到古法和JJK的技术的煎饼果子。

```python
# 1、师傅类：属性和方法
class Master(object):
    def __init__(self):
        self.kongfu = '古法煎饼果子配方'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

class School(object):
    def __init__(self):
        self.kongfu = 'jjk煎饼果子配方'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

# 2、徒弟类：继承师傅类 和 学校类， 添加和父类同名的属性和方法
class Prentice(Master,School): 
    def __init__(self):
        self.kongfu = '独创的煎饼果子技术'

    def make_cake(self):
        # 加自己的初始化原因：如果不加这个自己的初始化，kongfu属性值是上一次调用的init内的kongfu属性值       
        # 如果是先调用了父类的属性和方法，父类属性会覆盖子类属性，故在调用属性前，先调用自己子类的初始化
        self.__init__()
        print(f'运用{self.kongfu}制作煎饼果子')

    # 子类调用父类的同名属性和方法：把父类的同名属性和方法再次封装
    # 调用父类方法，但是为了保证调用到的也是父类的属性，必须在调用方法前调用父类的初始化 
    def make_master_cake(self):
        # 父类类名.函数()
        # 再次调用初始化的原因：这里想要调用父类的同名方法和属性，属性在init初始化位置，所以需要再次调用init
        Master.__init__(self)
        Master.make_cake(self)

    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)


# 3、用徒弟类创建对象，调用实例属性和方法结论验证
daqiu = Prentice()
daqiu.make_cake()

daqiu.make_master_cake()
daqiu.make_school_cake()
daqiu.make_cake()

"""
运用独创的煎饼果子技术制作煎饼果子
运用古法煎饼果子配方制作煎饼果子
运用jjk煎饼果子配方制作煎饼果子
运用独创的煎饼果子技术制作煎饼果子

"""
```



## 24.7 多层继承

> 故事：N年后， daqiu老了，想要把所有技术传承给自己的徒弟。



```python
# 1、师傅类：属性和方法
class Master(object):
    def __init__(self):
        self.kongfu = '古法煎饼果子配方'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

class School(object):
    def __init__(self):
        self.kongfu = 'jjk煎饼果子配方'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


# 2、徒弟类：继承师傅类 和 学校类， 添加和父类同名的属性和方法
class Prentice(Master,School): # 想要继承谁，就把谁写在第一个位置
    # 加自己的初始化原因：如果不加这个自己的初始化，kongfu属性值是上一次调用的init内的kongfu属性值
    def __init__(self):
        self.kongfu = '独创的煎饼果子技术'

    def make_cake(self):
        self.__init__()
        print(f'运用{self.kongfu}制作煎饼果子')

    # 子类调用父类的同名属性和方法：把父类的同名属性和方法再次f封装
    def make_master_cake(self):
        # 父类类名.函数()
        # 再次调用初始化的原因：这里想要调用父类的同名方法和属性，属性在init初始化位置，所以需要再次调用init
        Master.__init__(self)
        Master.make_cake(self)

    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)
        

# 徒孙类
# 步骤：1、创建类Tusun，用这个类创建对象；2、用这个对象调用父类的属性或方法看能否成功。
class Tusun(Prentice):
    pass

xiaoqiu = Tusun()

xiaoqiu.make_cake()

xiaoqiu.make_master_cake()

xiaoqiu.make_school_cake()
```



## 24.8 super()调用父类方法

```python
# 1、师傅类：属性和方法
class Master(object):
    def __init__(self):
        self.kongfu = '古法煎饼果子配方'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

class School(Master):
    def __init__(self):
        self.kongfu = 'jjk煎饼果子配方'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

        # 2.1 super()带参数写法
        # super(School,self).__init__()
        # super(School,self).make_cake()

        # 2.2 无参数super
        super().__init__()
        super().make_cake() # master类


# 2、徒弟类：继承师傅类 和 学校类， 添加和父类同名的属性和方法
class Prentice(School): # 想要继承谁，就把谁写在第一个位置
    # 加自己的初始化原因：如果不加这个自己的初始化，kongfu属性值是上一次调用的init内的kongfu属性值
    def __init__(self):
        self.kongfu = '独创的煎饼果子技术'

    def make_cake(self):
        self.__init__()
        print(f'运用{self.kongfu}制作煎饼果子')

    # 子类调用父类的同名属性和方法：把父类的同名属性和方法再次f封装
    def make_master_cake(self):
        # 父类类名.函数()
        # 再次调用初始化的原因：这里想要调用父类的同名方法和属性，属性在init初始化位置，所以需要再次调用init
        Master.__init__(self)
        Master.make_cake(self)

    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)

    # 需求：一次性调用父类School Master的方法
    def make_old_cake(self):
        # 方法一：如果定义的类名修改，这里也要修改，麻烦；代码量庞大，冗余
        # School.__init__(self)
        # School.make_cake(self)
        # Master.__init__(self)
        # Master.make_cake(self)

        # 方法二：super()
        # 方法2.1 super(当前类名，self).函数()
        # super(Prentice,self).__init__()
        # super(Prentice,self).make_cake() # 调用到了School类的方法

        # 方法2.2 无参数super
        super().__init__()
        super().make_cake() # School类

# 3、用徒弟类创建对象，调用实例属性和方法结论验证
daqiu = Prentice()
daqiu.make_old_cake()

```



注意：使用 super()可以自动查找父类。调用顺序遵循 `__mro__` 类属性的顺序。比较适合单继承使用。



----





## 24.9 私有权限

### 24.9.1 定义私有属性和方法

在 Python中，可以为实例属性和方法设置私有权限，即设置某个实例属性或实例方法不继承给子类。

> 故事：daqiu把技术传承给徒弟的同时，不想把自己的钱（200000个亿）继承给徒弟，这个时候就要为钱这个实例属性设置私有权限。

设置私有权限的方法：在属性名和方法名前面加上两个下划线__。

```python
# 1、师傅类：属性和方法
class Master(object):
    def __init__(self):
        self.kongfu = '古法煎饼果子配方'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

class School(object):
    def __init__(self):
        self.kongfu = 'jjk煎饼果子配方'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


# 2、徒弟类：继承师傅类 和 学校类， 添加和父类同名的属性和方法
class Prentice(School,Master): # 想要继承谁，就把谁写在第一个位置
    # 加自己的初始化原因：如果不加这个自己的初始化，kongfu属性值是上一次调用的init内的kongfu属性值
    def __init__(self):
        self.kongfu = '独创的煎饼果子技术'
        #self.money = 220000 # 
        self.__money = 220000 # 定义私有属性

    # 定义私有方法
    def __info_print(self):
        print('这是私有方法')


    def make_cake(self):
        self.__init__()
        print(f'运用{self.kongfu}制作煎饼果子')

    # 子类调用父类的同名属性和方法：把父类的同名属性和方法再次f封装
    def make_master_cake(self):
        # 父类类名.函数()
        # 再次调用初始化的原因：这里想要调用父类的同名方法和属性，属性在init初始化位置，所以需要再次调用init
        Master.__init__(self)
        Master.make_cake(self)

    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)

class Tusun(Prentice):
    pass

# 3、用徒弟类创建对象，调用实例属性和方法结论验证
xiaoqiu = Tusun()
#print(xiaoqiu.money) # 220000
#xiaoqiu.__info_print() # 这是私有方法
```

### 24.9.2 获取和修改私有属性值

在 Python中，一般定义函数名 `get_xx`  用来获取私有属性，定义 `set_xx` 用来修改私有属性值。

```python
# 1、师傅类：属性和方法
class Master(object):
    def __init__(self):
        self.kongfu = '古法煎饼果子配方'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

class School(object):
    def __init__(self):
        self.kongfu = 'jjk煎饼果子配方'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


# 2、徒弟类：继承师傅类 和 学校类， 添加和父类同名的属性和方法
class Prentice(School,Master): # 想要继承谁，就把谁写在第一个位置
    # 加自己的初始化原因：如果不加这个自己的初始化，kongfu属性值是上一次调用的init内的kongfu属性值
    def __init__(self):
        self.kongfu = '独创的煎饼果子技术'
        #self.money = 220000 #
        self.__money = 220000 # 定义私有属性

    # 定义函数：获取私有属性值  get_xx
    def get_money(self):
        return self.__money
    # 定义函数：修改私有属性值 set_xx
    def set_money(self):
        self.__money = 500

    # 定义私有方法
    def __info_print(self):
        print('这是私有方法')


    def make_cake(self):
        self.__init__()
        print(f'运用{self.kongfu}制作煎饼果子')

    # 子类调用父类的同名属性和方法：把父类的同名属性和方法再次f封装
    def make_master_cake(self):
        # 父类类名.函数()
        # 再次调用初始化的原因：这里想要调用父类的同名方法和属性，属性在init初始化位置，所以需要再次调用init
        Master.__init__(self)
        Master.make_cake(self)

    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)

class Tusun(Prentice):
    pass

# 3、用徒弟类创建对象，调用实例属性和方法结论验证
xiaoqiu = Tusun()
print(xiaoqiu.get_money())

xiaoqiu.set_money()
print(xiaoqiu.get_money())

"""
220000
500
"""
```



#  二十五、==面向对象-其他==

**目标**

- 面向对象三大特性
- 类属性和实例属性
- 类方法和静态方法



## 25.1 面向对象三大特性

- 封装

    将属性和方法书写到类的里面的操作即为封装

    封装可以为属性和方法添加私有权限

- 继承

    子类默认继承父类的所有属性和方法

    子类可以重写父类属性和方法

- 多态

    传入不同的对象，产生不同的结果



---



## 25.2 ==多态==

### 25.1.1 了解多态

多态指的是一类事物有多种形态，（一个抽象类有多个子类，因而多态的概念依赖于继承）。

- 定义：多态是一种使用对象的方式，子类重写父类方法，调用不同子类对象的相同父类方法，可以产生不同的执行结果

- 好处：调用灵活，有了多态，更容易编写出通用的代码，做出通用的编程，以适应需求的不断变
    化！

- 实现步骤：

    定义父类，并提供公共方法

    定义子类，并重写父类方法

    传递子类对象给调用者，可以看到不同子类执行效果不同



### 25.1.2 体验多态

```python
# 需求：警务人员和警犬一起工作，警犬分两种：追击敌人和追查毒品，携带不同的警犬，执行不同的工作

# 1、定义父类，提供公共方法：警犬  和   人
class Dog(object):
    """父类"""
    def work(self):
        pass


# 2、定义子类，子类重写父类方法：定义2个类表示不同的警犬
class ArmyDog(Dog):
    def work(self):
        print('追击敌人....')

class DruDog(Dog):
    def work(self):
        print('追查毒品....')

# 定义人类
class Person(object):
    def work_with_dog(self,dog):
        dog.work()

# 3、创建对象，调用不同的对象，传入不同的对象，执行不同的结果
ad = ArmyDog()
dd = DruDog()

daqiu = Person()
daqiu.work_with_dog(ad)
daqiu.work_with_dog(dd)
```



---



## 25.3 ==类属性和实例属性==

### 25.3.1 类属性

#### 25.3.1.1 设置和访问类属性

- 类属性就是**类对象**所拥有的属性，它被**该类的所有实例对象所共有**。
- 类属性可以使用**类对象**或**实例对象**访问。

```python
# 1、定义类，定义类属性
class Doa(object):
    tooth = 20

# 2、创建对象
wangcai = Doa()
xiaohei = Doa()

# 3、访问类属性：类和对象
print(Doa.tooth) # 20
print(wangcai.tooth) #20
print(xiaohei.tooth) # 20
```

>  类属性的优点
>
> - 记录的某项数据始终保持一致时，则定义类属性。
> - **实例属性**要求**每个对象**为其**单独开辟一份内存空间**来记录数据，而**类属性**为全类所共有
>     ，**仅占用一份内存，更加节省内存空间。**



###25.3.2 实例属性

**修改类属性**

类属性只能通过**类对象**修改，不能通过实例对象修改，如果通过实例对象修改类属性，表示的是创建了
一个实例属性。

```python
# 1、定义类，定义类属性
class Dog(object):
    tooth = 20

# 2、创建对象
wangcai = Dog()
xiaohei = Dog()

# 修改类属性
# 1、类 类.类属性 = 值
Dog.tooth = 1000
print(Dog.tooth) # 1000
print(wangcai.tooth) #1000
print(xiaohei.tooth) # 1000

# 2、测试通过对象修改类属性
wangcai.tooth = 200
print(Dog.tooth) # 20
print(wangcai.tooth) #200
print(xiaohei.tooth) # 20
```

## 25.3.2 ==类方法和静态方法==

#### 25.3.2.1 类方法的特点

需要用装饰器 `@classmethod` 来标识其为类方法，对于类方法，**第一个参数必须是类对象**，一般以
`cls` 作为第一个参数。



#### 25.3.2.2 类方法使用场景

- 当方法中**需要使用类对象**（如访问私有类属性等）时，定义类方法
- 类方法一般和类属性配合使用

```python
# 1、定义类：私有类属性，类方法获取私有类属性
class Dog(object):
    __tooth = 10

    # 定义类方法
    @classmethod
    def get_tooch(cls):
        return cls.__tooth

# 2、创建对象，调用类方法
wangcai = Dog()
result = wangcai.get_tooch()
print(result) # 10
```



#### 25.3.2.3 ==静态方法==

##### 25.3.2.3.1 静态方法的特点

- 需要通过装饰器 `@staticmethod` 来进行修饰，**静态方法既不需要传递类对象也不需要传递实例对象**
    **（形参没有 `self/cls` ）**。
- 静态方法也能够通过**实例对象**和**类对象**去访问。



##### 25.3.2.3.2 静态方法使用场景

- 当方法中**既不需要使用实例对象**（如实例对象，实例属性），**也不需要使用类对象**（如类属性、类方
    法、创建实例等）时，定义静态方法
- **取消不需要的参数传递**，有利于**减少不必要的内存占用和性能消耗**。

```python
# 1、定义类：定义静态方法
class Dog(object):
    @staticmethod
    def info_print():
        print('这是一个静态方法')
# 2、创建对象
wangcai = Dog()

# 3、调用静态方法：类 和 对象
wangcai.info_print()
Dog.info_print() # 静态方法也可以通过类来调用
```



# 二十六、异常

**目标**

- 了解异常
- 捕获异常
- 异常的else
- 异常 finally
- 异常的传递
- 自定义异常



## 26.1 了解异常

当检测到一个错误时，解释器就无法继续执行了，反而出现了一些错误的提示，这就是所谓的"异常"。
例如：以 `r` 方式打开一个不存在的文件。

## 26.2 异常的写法

### 26.2.1 语法

```python
try:
    可能发生错误的代码
except:
    如果发生异常执行的代码
```

### 26.2.1 快速体验

需求：尝试以 `r` 模式打开文件，如果文件不存在，则以 `w` 方式打开

```python
try:
    f = open('test.txt','r')
except:
    f = open('text.txt','w')
```

## 26.3 捕获指定异常

### 26.3.1 语法

```python
try:
    可能发生错误的代码
except 异常类型：
    如果捕获到该异常类型执行的代码

```

### 26.3.2 体验

```python
try:
    print(num)
except NameError:
    print('有错误')
```

> 注意：
>
> 1. 如果尝试执行的代码的异常类型和要捕获的异常类型不一致，则无法捕获异常。
> 2. 一般try下方只放一行尝试执行的代码。



### 26.3.3 捕获多个指定异常

当捕获多个异常时，可以把要捕获的异常类型的名字，放到 except后，并使用元组的方式进行书写。

```python
try:
    print(1/0)
except (NameError,ZeroDivisionError):
    print('有错误')
```



### 26.3.4 捕获异常描述信息

```python
try:
    print(num)
except (NameError,ZeroDivisionError) as result:
    print(result)
```



### 26.3.5 捕获所有异常

Exception是所有程序异常类的父类。

```python
try:
    print(num)
except Exception as result:
    print(result)
```



## 26.4 异常的else

else表示的是如果没有异常要执行的代码。

```python
try:
    print(1)
except Exception as result:
    print(result)
else:
    print('我是else，当没有异常的时候执行的代码')
   
"""
1
我是else，当没有异常的时候执行的代码

"""
```



## 26.5 异常的finally

finally表示的是无论是否异常都要执行的代码，例如关闭文件。

```python
try:
    f = open('text.txt', 'r')
except Exception as result:
    f = open('test.txt', 'w')
else:
    print('没有异常，真开心')
finally:
    f.close()
```



## 26.6 异常的传递

需求：

1、尝试只读方式打开test.txt文件，如果文件存在则读取文件内容，文件不存在则提示用户即可。

2、读取内容要求：尝试循环读取文件，读取过程中如果检测到用户意外终止程序，则except捕获异常并提示用户。

```python
# 需求1：尝试只读打开test.txt 文件存在读取内容，不存在提示用户
# 需求2：读取内容：循环读取，当无内容的时候退出循环，如果用户意外终止，提示用户已经被意外终止。
import time
try:
    f = open('test.txt')
    try:
        while True:
            content = f.readline()
            if len(content) ==0:
                break
            time.sleep(2)
            print(content)
    except:
        # 如果在读取文件的过程中，产生了异常，那么就会捕获到
        # 比如，按下了ctrl+c
        print('意外终止了读取数据')
    finally:
        f.close()
        print('关闭文件')
except:
    print('文件不存在')
```



## 26.7 自定义异常

在 Python中，抛出自定义异常的语法为 `raise` 异常类对象。

**需求：**密码长度不足，则报异常（用户输入密码，如果输入的长度不足3位，则报错，即抛出自定义异常，并捕获该异常）。

```python
# 1、自定义异常类：继承Exception，魔法方法有init和str(设置异常描述信息)
# 2、抛出异常: 尝试执行：用户输入密码，如果长度小于3，抛出异常
# 3、捕获异常

# 自定义异常类，继承Exception
class ShortInputError(Exception):
    def __init__(self,length, min_len):
        #用户输入的密码长度
        self.length = length
        #系统要求的最少长度
        self.min_len = min_len

    # 设置抛出异常的描述信息
    def __str__(self):
        return f'你输入的长度是{self.length},不能少于{self.min_len}个字符'

def main():
    try:
        con = input('请输入密码：')
        if len(con)<3:
            raise ShortInputError(len(con),3)
    except Exception as e:
        print(e)
    else:
        print('输入密码完成')

main()
```



## 26.8 异常总结

- 异常语法

```python
try:
    可能发生异常的代码
except:
    如果发出异常执行的代码
else:
    没有异常执行的代码
finally:
    无论是否异常都要执行的代码
```

- 捕获异常

```python
except 异常类型:
    代码
except 异常类型 as xx:
    代码
```

- 自定义异常

```python
# 1、自定义异常类
class 异常类类名(Exception):
    代码
    #设置抛出异常的描述信息
    def __str__(self):
        return ...
# 2、抛出异常
raise 异常类名()
# 捕获异常
except Exception
```





# 二十七、模块和包

**目标**

- 了解模块
- 导入模块
- 制作模块
- `__all__`
- 包的使用方法

---



## 27.1 模块

Python模块（Module），是一个 Python文件，以py结尾，包含了 Python对象定义和 Python语句。

**模块能定义函数，类和变量，模块里也能包含可执行的代码。**



### 27.1.1 导入模块

#### 27.1.1.1 导入模块的方式

- import 模块名
- from 模块名 import 功能名
- from 模块名 import *
- import 模块名as 别名
- from 模块名 import 功能名 as 别名



### 27.1.2 导入方式详解

#### 27.1.2.1 import

- 语法

```python
# 1、导入模块
import 模块名
import 模块名1，模块名2...

# 2、调用功能
模块名.功能名()
```

- 体验

```python
import math
print(math.sqrt(9)) # 3.0
```



#### 27.1.2.2 from...import...

- 语法

```
from 模块名 import 功能1，功能2，功能3...
```

- 体验

```python
from math import sqrt
print(sqrt(9))
```



#### 27.1.2.3 from..import *

- 语法

```python
from 模块名 import *
```

- 体验

```python
from math import *
print(sqrt(9))
```



#### 27.1.2.4 as定义别名

- 语法

```python
#模块定义别名
import 模块名 as 别名

# 功能定义别名
from 模块名 import 功能 as 别名
```

- 体验

```python
# 模块别名
import time as tt
tt.sleep(2)
print('hello')

# 功能别名
from time import sleep as sl
sl(2)
print('hello')
```



### 27.1.3 ==制作模块==

在 Python中，每个 Python文件都可以作为一个模块，模块的名字就是文件的名字。<font color=red>**也就是说自定义模块名必须要符合标识符命名规则。**</font>



#### 27.1.3.1 定义模块

新建一个python文件，命名为 `my_module1.py` ，并定义 `testA` 函数。

```python
def testA(a,b):
    print(a+b)
```



#### 27.1.3.2 测试模块

在实际开中，当一个开发人员编写完一个模块后，为了让模块能够在项目中达到想要的效果，这个开发
人员会自行在py文件中添加一些测试信息，例如，在 `my_module1.py` 文件中添加测试代码。

```python
def testA(a,b):
    print(a+b)

testA(1,1)

```

此时，无论是当前文件，还是其他已经导入了该模块的文件，在运行的时候都会自动执行 ` testA` 函数的调用。
解决办法如下：

```python
def testA(a,b):
    print(a+b)
    
# 只在当前文件中调用该函数，其他导入的文件内不符合该条件，则不执行testA函数调用
#__name__是系统变量，是模块的标识符，值是：如果是自身模块值是__main__,否则是当前模块的名字
if __name__ == '__main__':
   testA(1,1)
```



#### 27.1.3.3 调用模块

```python
# 1、导入模块
import my_module1
# 2、调用功能
my_module1.testA(2,2)
```



### 27.1.4 模块定位顺序

当导入一个模块， Python解析器对模块位置的搜索顺序是：

1. 当前目录
2. 如果不在当前目录， Python则搜索在shell变量PYTHONPATH下的每个目录。
3. 如果都找不到， Python会察看默认路径。UNIX下，默认路径一般为/usr/local/lib/python/

模块搜索路径存储在system模型的sys.path变量中。变量里包含当前目录，PYTHONPATH和由安装过程决定的默认目录。

- **注意**

    自己的文件名不要和已有的模块名重复，否则导入模块功能无法使用（大概意思就是你本地文件同目录下，不要有和模块名重复的文件名）

    使用from 模块名 import 功能 的时候，如果功能名字重复，调用到的是最后定义或导入的功能。



---



**名字重复的严重性**

```python
问题：import 模块名  是否担心  功能名字重复的问题 ------不需要
import time
print(time)

time = 1
print(tim3) #1


# 问题：为什么变量也能覆盖模块？     -----在python语言中，数据是通过  引用  传递的。
```



### 27.1.5 `__all__` 列表

如果一个模块文件有 `__all__` 变量，当使用 `from xxx import *` 导入时，只能导入这个列表中的元素。

- my_module1模块代码

```python
__all__ = ['testA']

def testA():
    print('testA')

def testB():
    print('testB')
```

**说明**：本来我们能导入这个模块中的所有功能，奈何模块中有：`__all__`  ，导致只能导入`__all__` 列表中的内容。

- 导入模块的文件代码

```python
from my_module1 import *

testA()

# 因为testB函数没有添加到all函数，只有all列表里面的功能才能导入
# testB()  # NameError: name 'testB' is not defined
```



## 27.2 包

包将有联系的模块组织在一起，即放到同一个文件夹下，并且在这个文件夹创建一个名为 `__init__.py` 文件，那么这个文件夹就称之为包。

### 27.2.1 制作包

[new]—[python package]—输入包名—[ok]—新建功能模块(有联系的模块)

注意：新建包后，包内会自动创建 `__init__.py` 文件，这个文件控制这包的**导入行为**。

### 27.2.2 快速体验

1. 新建包 `mypackage`
2. 新建包内模块：`my_module1` 和 `my_module2`
3. 模块内代码加下

```python
# my_module1
print(1)

def info_print1():
    print('my_module1')
```



```python
# my_module2
print(2)

def info_print1():
    print('my_module2')
```



### 27.2.3 导入包

#### 27.2.3.1 方法一

- 语法

```python
import 包名.模块名

包名.模块名.目标
```

- 体验

```python
import my_package.my_module1

my_package._my_module1.info_print1()
```



#### 27.2.3.2 方法二

<font color=red>注意：</font>必须在 `__init__.py` 文件中添加 `__all__=[]` ，**控制允许导入的模块列表。**

- 语法

```python
from 包名 import *
模块名.目标
```

- 体验

```python
# __init__.py文件：
__all__ = ['my_module1']

# 测试文件
from my_package import *
my_module1.info_print1() 

"""
1
my_module1
"""
```



# 二十八、面向对象版学院管理系统

**目标**

- 了解面向对象开发过程中类内部功能的分析方法

- 了解常用系统功能

    添加

    删除

    修改

    查询

## 28.1 系统需求

使用面向对象编程思想完成学员管理系统的开发，具体如下：

- 系统要求：学员数据存储在文件中
- 系统功能：添加学员、删除学员、修改学员信息、查询学员信息、显示所有学员信息、保存学员信
    息及退出系统等功能。

## 28.2 准备程序文件

### 28.2.1 分析

- 角色分析

    学员

    管理系统

**工作中注意事项**

1. 为了方便维护代码，一般一个角色一个程序文件；
2. 项目要有主程序入口，习惯为main.py

---



### 28.2.2 创建程序文件

创建项目目录，例如：`StudentManageSystem`

**程序文件如下：**

- 程序入口文件：main.py
- 学员文件：student.py
- 管理系统文件：manageSystem.py

---

### 28.2.3 书写程序

#### 28.2.3.1 student.py

**需求：**

- 学员信息包含：姓名、性别、手机号；
- 添加 `__str__` 魔法方法，方便查看学员对象信息

**程序源码：**

```python
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
```



#### 28.2.3.2 managerSystem.py

**需求：**

- 存储数据的位置：文件（student.data）

    加载文件数据

    修改数据后保存到文件

- 存储数据的形式：列表存储学员对象

- 系统功能

    添加学员

    删除学员

    修改学员

    查询学员信息

    显示所有学员信息

    保存学员信息

---

**定义类**：

```python
class StudentSystem(object):
    def __init__(self):
        # 存储数据所用的列表
        self.student_list = []
```



----



**管理系统框架：**

需求：系统功能循环使用，用户输入不同的功能序号执行不同的功能。

- 步骤

    定义程序入口函数

    ​        加载数据

    ​        显示功能菜单

    ​        用户输入功能序号

    ​        根据用户执行不同的功能序号执行不同的功能

    定义系统功能函数，添加、删除学员等

```python
# 一、程序入口函数，启动程序后执行的函数
    def run(self):
        # 1、加载学员信息
        while True:
            # 2、显示功能菜单
            # 3、用户输入功能序号
            menu_num = int(input('您输入的功能序号：'))

            # 4、根据用户输入的序号执行不同的功能
            if menu_num ==1:
                # 添加学员
                pass
            elif menu_num ==2:
                # 删除学员
                pass
            elif menu_num ==3:
                # 修改学员信息
                pass
            elif menu_num ==4:
                # 查询学员信息
                pass
            elif menu_num ==5:
                # 显示所有学员信息
                pass
            elif menu_num ==6:
                # 保存学员信息
                pass
            elif menu_num ==7:
                # 退出系统----退出循环
                break
```



更新

```python
"""
 author:jjk
 datetime:2020/4/25
 coding:utf-8
 project name:Pycharm_workstation
 Program function:
 
"""

class StudentSystem(object):
    def __init__(self):
        # 存储学员数据所用的列表
        self.student_list = []

    # 一、程序入口函数，启动程序后执行的函数

    def run(self):
        # 1、加载学员信息
        self.add_student()
        while True:
            # 2、显示功能菜单
            self.show_menu() # 类里面调用方法self
            # 3、用户输入功能序号
            menu_num = int(input('您输入的功能序号：'))

            # 4、根据用户输入的序号执行不同的功能
            if menu_num ==1:
                # 添加学员
                self.add_student()
            elif menu_num ==2:
                # 删除学员
                self.del_student()
            elif menu_num ==3:
                # 修改学员信息
                self.modify_student()
            elif menu_num ==4:
                # 查询学员信息
                self.search_student()
            elif menu_num ==5:
                # 显示所有学员信息
                self.show_menu()
            elif menu_num ==6:
                # 保存学员信息
                self.save_student()
            elif menu_num ==7:
                # 退出系统----退出循环
                break


    # 二、系统功能函数
    # 2.1 显示功能菜单 -- 打印序号的功能对应关系 ---静态
    @staticmethod
    def show_menu():
        print('请选择如下功能：')
        print('1:添加学员')
        print('2:删除学员')
        print('3:修改学员信息')
        print('4:查询学员信息')
        print('5:显示学员信息')
        print('6:保存学员信息')
        print('7:退出系统')

    # 2.2 添加学员
    def add_student(self):
        """添加学员"""
        print('添加学员')
    # 2.3 删除学员
    def del_student(self):
        print('删除学员')
    # 2.4 修改学员信息
    def modify_student(self):
        print('修改学员信息')
    # 2.5 查询学员信息
    def search_student(self):
        print('查询学员信息')
    # 2.6 显示所有学员信息
    def show_student(self):
        print('显示所有')
    # 2.7 保存学员信息
    def save_student(self):
        print('保存学员信息')

    # 2.8 加载学员信息
    def load_student(self):
        print('加载学员信息')
```



----

#### 28.2.3.3 main.py

```python
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
```



#### 28.2.3.4 定义系统功能函数

**添加功能**

- 需求：用户输入学员姓名、性别、手机号，将学员添加到系统。

- 步骤

    用户输入姓名、性别、手机号

    创建该学员对象

    将该学员对象添加到列表

- 代码

```python
# 2.2 添加学员
def add_student(self):
    """添加学员"""
    #1、用户输入姓名、性别、手机号
    name = input('请输入您的姓名：')
    gender = input('请输入您的性别：')
    tel = input('请输入您的手机号：')

    #2、创建学员对象  --类？ 类在student文件中，先导入student模块，再创建对象
    student = Student(name,gender,tel)
    #3、将该对象添加到学员列表
    self.student_list.append(student)
    print(self.student_list)
    print(student)
```

----

**删除学员**

- 需求：用户输入目标学员姓名，如果学员存在则删除该学员。

- 步骤

    用户输入目标学员姓名

    遍历学员数据列表，如果用户输入的学员姓名存在则删除，否则则提示该学员不存在。

- 代码

```python
    # 2.3 删除学员
    def del_student(self):
        #1、用户输入目标学员姓名
        del_name = input('请输入需要删除的学员：')
        #2、遍历学员数据列表，如果用户输入的学员姓名存在则删除，否则则提示该学员不存在。
        for i in self.student_list:
            if del_name == i.name:
                # 删除该学员对象
                self.student_list.remove(i)
                break
        else:
            # 循环正常结束执行的代码：循环结束都没有删除任何一个对象，所以说明用户输入的目标学员不存在
            print('查无此人')
        print(self.student_list)
```



---



**修改学员信息**

- 需求：用户输入目标学员姓名，如果学员存在则修改该学员信息。

- 步骤

    用户输入目标学员姓名；

    遍历学员数据列表，如果用户输入的学员姓名存在则修改学员的姓名、性别、手机号数据，
    否则则提示该学员不存在。

- 代码

```python
# 2.4 修改学员信息
def modify_student(self):
    # 用户输入目标学员姓名；
    modify_name = input('请输入要修改的学员姓名：')

    #遍历学员数据列表，如果用户输入的学员姓名存在则修改学员的姓名、性别、手机号数据，否则则提示该学员不存在。
    for i in self.student_list:
        if modify_name == i.name:
            i.name = input('请输入您的姓名：')
            i.gender = input('请输入您的性别：')
            i.tel = input('请输入您的手机号：')
            print(f'修改学员信息成功， 姓名：{i.name}, 性别：{i.gender},手机号：{i.tel}')
            break
            else:
```



----

**查询学员信息功能**

- 需求：用户输入目标学员姓名，如果学员存在则打印该学员信息

- 步骤

    用户输入目标学员姓名

    遍历学员数据列表，如果用户输入的学员姓名存在则打印学员信息，否则提示该学员不存在。

- 代码

```python
# 2.5 查询学员信息
    def search_student(self):
        print('查询学员信息')
        # 1、用户输入目标学员姓名
        search_name = input('请输入要查询的学员姓名：')
        # 2、遍历学员数据列表，如果用户输入的学员姓名存在则打印学员信息，否则提示该学员不存在。
        for i in self.student_list:
            if i.name == search_name:
                print(f'姓名：{i.name}, 性别：{i.gender}, 手机号：{i.tel}')
                break
        else:
            print('查无此人')
```



---



**显示所有学员信息**

- 打印所有学员信息

- 步骤

    遍历学员数据列表，打印所有学员信息

- 代码

```python
    # 2.6 显示所有学员信息
    def show_student(self):
        print('姓名\t性别\t手机号')
        for i in self.student_list:
            print(f'{i.name}\t{i.gender}\t{i.tel}')
```



---



**保存学员信息**

- 需求：将修改后的学员数据保存到存储数据的文件。

- 步骤

    打开文件

    文件写入数据

    关闭文件

思考

1. 文件写入的数据是学员对象的内存地址吗？
2. 文件内数据要求的数据类型是什么？

- 拓展 `__dict__`：**收集类对象或者实例对象的属性和方法以及对应的值**

```python
#1、定义类
#2、创建对象
#3、调用__dict__
class A(object):
    a = 0 # 类属性
    def __init__(self):
        self.b = 1 # 实例属性

aa = A()
# {'__module__': '__main__', 'a': 0, '__init__': <function A.__init__ at 0x000001C220638C80>, '__dict__': <attribute '__dict__' of 'A' objects>, '__weakref__': <attribute '__weakref__' of 'A' objects>, '__doc__': None}....
print(A.__dict__)  
print(aa.__dict__) # {'b': 1}
```

==保存学员数据==

```python
    # 2.7 保存学员信息
    def save_student(self):
        # 1、打开文件
        f = open('student.data', 'w')
        # 2、文件写入数据
        # 2.1 [学员数据] 转换成 [字典]
        new_list = [i.__dict__  for i in self.student_list] # [{'name': 'jbji', 'gender': 'dfdf', 'tel': 'dfdf'}]
        # 2.2 文件写入  字符串数据
        f.write(str(new_list))
        # 3、关闭文件
        f.close()
```



----

==**加载学员数据**==

- 需求：每次进入系统后，修改的数据是文件里面的数据

- 步骤

    尝试以 `"r"` 模式打开学员数据文件，如果文件不存在则以 `"w"` 模式打开文件

    如果文件存在则读取数据并存储数据

    ​       读取数据

    ​       转换数据类型为列表并转换列表内的字典为对象

    ​        存储学员数据到学员列表

    关闭文件

- 代码

```python
# 2.8 加载学员信息
def load_student(self):
    """加载学员数据"""
    # 1、打开文件：尝试以 "r" 模式打开学员数据文件，如果文件不存在则以 "w" 模式打开文件
    try:
        f = open('student.data', 'r')
        except:
            f = open('student.data', 'w')
            else:
                # 如果文件存在则读取数据并存储数据
                # 读取数据：文件读取的数据是字符串，还原成列表类型： [{}] 转换 [学员对象]
                data = f.read() # 字符串
                new_list = eval(data) # 还原成原本的列表形式
                self.student_list = [Student(i['name'], i['gender'], i['tel']) for i in new_list]

                # 3、关闭文件
                finally:
                    f.close()
```





# 三十、杂记

## 30.1 jupyter lab中多个变量打印输出：

```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = 'all'
```

![image-20210207101133835](image-20210207101133835.png)

## 30.2 不同类型变量互相转换

- `int()`：将一个数值或字符串转换成整数，可以指定进制。
- `float()`：将一个字符串转换成浮点数。
- `str()`：将指定的对象转换成字符串形式，可以指定编码。
- `chr()`：将整数转换成该编码对应的字符串（一个字符）。
- `ord()`：将字符串（一个字符）转换成对应的编码（整数）。



## 30.3 range()用法

- `range(101)`：可以用来产生0到100范围的整数，需要注意的是取不到101。
- `range(1, 101)`：可以用来产生1到100范围的整数，相当于前面是闭区间后面是开区间。
- `range(1, 101, 2)`：可以用来产生1到100的奇数，其中2是步长，即每次数值递增的值。
- `range(100, 0, -2)`：可以用来产生100到1的偶数，其中-2是步长，即每次数字递减的值。















