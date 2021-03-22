print('~~~~~~~~~~~~传不可变对象~~~~~~~~~~~~')
def change(a):
    print(id(a))
    a = 23
    print(id(a))

a=1
print(id(a))
change(a)

'''
不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，
再让 a 指向它，而 5 被丢弃，不是改变 a 的值，相当于新生成了 a。

类似 C++ 的值传递，如整数、字符串、元组。如 fun(a)，传递的只是 a 的值，没有影响 a 对象本身。
如果在 fun(a) 内部修改 a 的值，则是新生成一个 a 的对象。
'''

