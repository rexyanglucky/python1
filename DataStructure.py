#coding=utf8
#.................列表....................
#列表
students=["小明","小明的妹妹","小明的哥哥"]
print students[2]
print students[1]
students[1]="修改后的小明的妹妹"
print students[1]
#元组用小括号 只能声明，不能修改值
teachers=("小明","小明的妹妹","小明的哥哥")
print teachers[1]

#.................集合....................

aSet=set("abcdefghijklmn")
bSet=set("bcd")

print "a:\n"
print aSet
print "b:\n"
print aSet

#交集
print "交集:\n"
x=aSet&bSet
print x

#并集
print "并集:\n"
x=aSet|bSet
print x

#差集
print "差集:\n"
x=aSet-bSet
print x

#去除重复元素
print "去除重复元素:\n"
distinctSet=set(aSet)
print distinctSet
#.................字典....................
k={"姓名":"杯子","形状":"圆柱"}
print k["姓名"]
k["容量"]="500ml"
print k["容量"]

