#!/usr/bin/env python
# 经典面试题：‘fizz和buzz’，1到100范围内，若被3整除用fizz替换，若被5整除用buzz替换
# 若同时被3和5整除用fizzbuzz替换
for x in range(1,101):
    print('fizz'[x % 3 * len('fizz')::] + 'buzz'[x % 5 * len('buzz')::] or x)

# 列表推导(list comprehensions)
list1 = [1,2,3,4,5,4,7,3]
another_list = [x+1 for x in list1]
print(another_list) #[2, 3, 4, 5, 6, 5, 8, 4]
# 集合推导(set comprehensions)
even_set = {x for x in list1 if x % 2 ==0}
print(even_set) #{2,4}

# 字典推导(dict comprehensions)
dic = {x:x%2 == 0 for x in range(1,11)}
print(dic) #{1: False, 2: True, 3: False, 4: True, 5: False, 6: True, 7: False, 8: True, 9: False, 10: True}

# codecs模块处理字符转换
import codecs
with codecs.open ('pytest.ini','r',encoding='utf8') as f:
    f.read()

# 打印漂亮的json
import json
dict = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
json_data = json.dumps(dict,indent=2)
print(json_data)

# 字符串格式化的方法：
# 1、%占坑
# 2、format方法
#3、f''
name = 'liq'
age = 23
print('my name is %s,age is %d' % (name, age))
print('my name is {},age is {}'.format(name, age))
print(f'my name is {name},age is {age}')





# 计数使用Counter计数对象
from collections import Counter
c = Counter('hello word')
print(c.most_common(1))


# 判断2000到2050闰年，并打印出来
# year被400整除是世纪闰年，或者能被4整除但不能被100整除是普通闰年
def is_leap_year(year):
    if  year % 400 ==0:
         print(f'{year}是世纪闰年')
    elif year % 4 == 0 and year % 100 != 0:
        print(f'{year}是普通闰年')
    else:
         print(f'{year}不是闰年')


if __name__ == '__main__':
    is_leap_year(2005)









