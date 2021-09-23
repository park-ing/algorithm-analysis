import time


# 알고리즘1 : recursion 사용
def fun1(n):
    if (n == 1) or (n == 2):
        return 1
    else:
        t = 0
        for i in range (n):
            t += fun1(i)
        return t


# 알고리즘2 : array 사용
def fun2(n):
    a = [0] * (n + 2)
    a[1] = a[2] = 1
    
    if n >= 3:
        t = 2
        for i in range (3, n):
            a[i] = t
            t += a[i]
        a[n] = t

        return a[n]

start1 = time.time()
print(fun1(26))
print ("수행시간 : ", time.time() - start1)

start2 = time.time()
print(fun2(6400*2))
print ("수행시간 : ", time.time() - start2)









# 알고리즘2 : array 사용 다른 버전
def fun22(n):
    a = [0] * (n + 2)
    a[1] = a[2] = 1
    
    if n >= 3:
        t = 0
        for i in range (n):
            if i >= 3:
                a[i] = t
            t += a[i]
        a[n] = t

        return a[n]
