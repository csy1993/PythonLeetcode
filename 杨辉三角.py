'''
* @File: 杨辉三角.py
* @Author: CSY
* @Date: 2019/7/23 - 9:12
'''
s=5
def f(i,j):
    if i==j or j==1:
        return 1
    else:
        return f(i-1,j-1)+f(i-1,j)
last=[]



i = 1
while i < 6:
    j = 1
    l=[]
    while j <= i:
        l.append(f(i,j))
        j += 1
    last.append(l)
    i += 1
print(last)