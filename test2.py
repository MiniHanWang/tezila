#@Time:2/26/20211:52 PM
#@Author: Mini(Wang Han)
#@Site:
#@File:test2.py
#即著名的科拉茨猜想，即3N+1的问题！该算法总能终止于n=1,运行的结果发现，序列最终变成4、2、1，4，2，1………的循环
def function(i):
    if i%2==0:
        j=i/2
    else:
        j=3*i+1
    return j
def function2(n):
    x=[]
    n=function(n)
    x.append(n)
    while (n!=1):
        n=function(n)
        x.append(n)
    print(x)
    number=len(x)+1
    print("number:",number)
function2(1)