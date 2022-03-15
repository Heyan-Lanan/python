"""
定义：在{}内用逗号分隔开多个元素，集合具备以下三个特点：
     1：每个元素必须是不可变类型
     2：集合内没有重复的元素
     3：集合内元素无序
"""
s = {1, 2, 3, 4}  # 本质 s = set({1,2,3,4})


# 注意:{}既可以用于定义dict，也可以用于定义集合，但是字典内的元素必须是key:value的格式，现在我们想定义一个空字典和空集合，该如何准确去定义两者?
d = {}  # 默认是空字典
s = set()  # 这才是定义空集合

# 类型转换
# 但凡能被for循环的遍历的数据类型（强调：遍历出的每一个值都必须为不可变类型）都可以传给set()转换成集合类型
s = set([1, 2, 3, 4])
s1 = set((1, 2, 3, 4))
s2 = set({'name': 'jason'})
s3 = set('egon')
print(s)
print(s1)
print(s2)
print(s3)

# 内置方法
friends1 = {"zero", "kevin", "jason", "egon"}  # 用户1的好友们
friends2 = {"Jy", "ricky", "jason", "egon"}   # 用户2的好友们

# 1.合集/并集(|)：求两个用户所有的好友（重复好友只留一个）
print(friends1 | friends2)  # {'kevin', 'ricky', 'zero', 'jason', 'Jy', 'egon'}
print(friends1.union(friends2))

# 2.交集(&)：求两个用户的共同好友
print(friends1 & friends2)  # {'jason', 'egon'}
print(friends1.intersection(friends2))

# 3.差集(-)：
print(friends1 - friends2)  # 求用户1独有的好友 {'kevin', 'zero'}
print(friends2 - friends1)  # 求用户2独有的好友 {'ricky', 'Jy'}
print(friends1.difference(friends2))
print(friends2.difference(friends1))

# 4.对称差集(^) # 求两个用户独有的好友们（即去掉共有的好友）
print(friends1 ^ friends2)  # {'kevin', 'zero', 'ricky', 'Jy'}
print(friends1.symmetric_difference(friends2))

# 5.值是否相等(==)
print(friends1 == friends2)  # False

# 6.子集：一个集合是否包含另外一个集合
print({1, 2, 3} > {1, 2})  # True
print({1, 2, 3} >= {1, 2})  # True
print({1, 2, 3} > {1, 3, 4, 5})  # False
print({1, 2, 3} >= {1, 3, 4, 5})  # False
print({1, 2} < {1, 2, 3})  # True
print({1, 2} <= {1, 2, 3})  # True
s1 = {1, 2, 3}
s2 = {1, 2}
print(s1.issuperset(s2))
print(s2.issubset(s1))

# 去重
l = ['a', 'b', 1, 'a', 'a']
s = set(l)  # 将列表转成了集合
print(s)  # {'b', 'a', 1}
l_new = list(s)  # 再将集合转回列表
print(l_new)  # ['b', 'a', 1] 去除了重复，但是打乱了顺序

# 针对不可变类型，并且保证顺序则需要我们自己写代码实现，例如
l = [
    {'name': 'lili', 'age': 18, 'sex': 'male'},
    {'name': 'jack', 'age': 73, 'sex': 'male'},
    {'name': 'tom', 'age': 20, 'sex': 'female'},
    {'name': 'lili', 'age': 18, 'sex': 'male'},
    {'name': 'lili', 'age': 18, 'sex': 'male'},
]

new_l = []

for dic in l:
    if dic not in new_l:
        new_l.append(dic)

print(new_l)  # 结果：既去除了重复，又保证了顺序，而且是针对不可变类型的去重

s = {1, 2, 3}
s.discard(3)
print(s)
s.remove(2)  # 删除元素不存在则报错
s.update({1, 3, 5})  # 将{1, 3, 5}加到原集合并去重
print(s)
s.difference_update({1, 4, 5})
print(s)
s = {1, 2, 3}
res = s.pop()  # 随机删除一个元素
print(res)
s.add(4)  # 添加一个元素
print(s)
s_ = {5, 6, 7}
print(s.isdisjoint(s_))  # 如果交集为空则返回true


