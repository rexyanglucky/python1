#coding=utf8
#运算符 优先级练习

func=lambda x,y:x+y

#优先级排行榜第1名--函数调用、寻址、下标
print "优先级排行榜第1名--函数调用、寻址、下标"
print "a=4*func(1,2)"
a=4*func(1,2)
print a

#优先级排行榜第2名--幂运算**
print "优先级排行榜第2名--幂运算**"
print "a=4*2**3"
a=4*2**3
print a

#优先级排行榜第3名--翻转运算~
print "优先级排行榜第3名--翻转运算~"
print "a=4*~2"
a=4*~2
print a

#优先级排行榜第4名--正负号
print "优先级排行榜第4名--正负号"
print "a=4*-2"
a=4*-2
print a

#优先级排行榜第5名--乘 除 取余数
print "优先级排行榜第5名--乘 除 取余数"
print "a=2+4*2/4"
a=2+4*2/4
print a

#优先级排行榜第6名--加减
print "优先级排行榜第6名--加减"
print "a=3<<2+1"
a=3<<2+1
print a

#优先级排行榜第7名--左移右移 << >>
print "优先级排行榜第7名--左移右移 << >>"
print "a=3<<2+1"
a=3<<2+1
print a

#优先级排行榜第8名--按位运算 & | ^ 按位与或非
print "优先级排行榜第8名--按位运算 & | ^ 按位与或非"
print "a=18&1+1"
a=18&1+1
print a

#优先级排行榜第9名--比较运算符 <= >= ==
print "优先级排行榜第9名--比较运算符 <= >= =="
print "a=1+2==3+1"
a=1+2==3+1
print a

#优先级排行榜第10名--逻辑与或非 and or not
print "优先级排行榜第10名--逻辑与或非 and or not"
print "a=0&1"
a=0&1
print a

#优先级排行榜第11名--lambda 表达式
print "优先级排行榜第11名--lambda 表达式"
print "a=lambda x:x**2 + 1"
a=lambda x:x**2 + 1
print a

