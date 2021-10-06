import numpy as np

def order(p, i, j):
    if (i==j):
        print('A',i,end='')  #print함수 줄 바꿈 방지
    else:
        k = p[i][j]
        print('(',end='')
        order(p,i,k)
        order(p,k+1,j)
        print(')',end='')

d = [5,2,3,4,6,7,8]
n = len(d) - 1

m = [[0 for j in range(1,n+2)] for i in range(1, n+2)]
p = [[0 for j in range(1,n+2)] for i in range(1, n+2)]

def minmult(m, n, d, p):
    for i in range(1,n+1):
        m[i][i] = 0
    for diagonal in range(1,n):
        for i in range(1,n-diagonal+1):    
            j = i + diagonal
            temp = []
            for k in range(i,j):
                temp.append(m[i][k] + m[k+1][j] + (d[i-1]*d[k]*d[j]))
#            print(temp)         
            m[i][j] = min(temp)                       # 임시 리스트에 가능한 모든 행렬 곱셈 횟수를 추가하고 최솟값을 m 행렬에 입력
            p[i][j] = i + temp.index(m[i][j])         # 임시 리스트의 최솟값 인덱스를 이용해 k값을 p행렬에 전달
            temp.remove

    return m, p


min, P = minmult(m,n,d,p)
Min = np.array(min)
p_ = np.array(P)
print(Min)
print()
print(p_)
order(p,1,6)

