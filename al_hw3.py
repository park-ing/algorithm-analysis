import numpy as np
import random
import matplotlib.pyplot as plt

def quickSort(s, low, high, cnt):

    if (low < high):
        pivotpoint, cnt = partition(s, low, high, cnt)
        quickSort(s, low, pivotpoint-1, cnt)
        quickSort(s, pivotpoint+1, high, cnt)

    return s, cnt



def partition(s, low, high,cnt):
    pivotpoint = 0
    pivotitem = s[low]
    j = low
    for i in range(low+1, high+1):
        if(s[i] < pivotitem):
            j += 1
            temp = s[j]
            s[j] = s[i]
            s[i] = temp
            cnt += 1    # 데이터 비교 횟수 카운트
    pivotpoint = j
    temp = s[pivotpoint]
    s[pivotpoint] = s[low]
    s[low] = temp
    return pivotpoint, cnt

N = []
S = []
s = []
n = 8
while(True):
    cnt = 0
    for i in range(20): # n값에 따라 정렬할 데이터 20개 생성
        for i in range(n):
            s.append(random.randint(0, n))
        S.append(s)
        s.remove
        s = []
    print("정렬 전")
    print("n = ",n)
    print(S)

    for j in range(20): # 빠른 정렬 알고리즘으로 정렬
        S[j], cnt = quickSort(S[j], 0, n-1, cnt)
    N.append(cnt/20)
    print("정렬 후")    
    print("n = ",n)
    print(S)
    S.remove
    S = []
    if n == 40:
        break
    n += 8
print("======")
print("평균 비교 횟수", N)

plt.title("Quicksort")
plt.plot([8,16,24,32,40],N)
plt.scatter([8,16,24,32,40],N)
plt.grid()
plt.show()



#s = [3, 5, 2, 9, 10, 14, 4, 8]
#quickSort(s, 0, 7)
#print(s)

def strassen (n, A, B, C):
    threshold = 2
    A11 = np.array([[A[rows][cols] for cols in range(int(n/2))]for rows in range (int(n/2))])
    A12 = np.array([[A[rows][cols] for cols in range(int(n/2),n)]for rows in range (int(n/2))])
    A21 = np.array([[A[rows][cols] for cols in range(int(n/2))]for rows in range (int(n/2),n)])
    A22 = np.array([[A[rows][cols] for cols in range(int(n/2),n)]for rows in range (int(n/2),n)])

    B11 = np.array([[B[rows][cols] for cols in range(int(n/2))]for rows in range (int(n/2))])
    B12 = np.array([[B[rows][cols] for cols in range(int(n/2),n)]for rows in range (int(n/2))])
    B21 = np.array([[B[rows][cols] for cols in range(int(n/2))]for rows in range (int(n/2),n)])
    B22 = np.array([[B[rows][cols] for cols in range(int(n/2),n)]for rows in range (int(n/2),n)])

    if (n <= threshold):
        C = np.array(A)@np.array(B)
    else:
        M1 = M2 = M3 = M4 = M5 = M6 = M7 = np.array([])
        M1 = strassen(int(n/2), (A11 + A22), (B11 + B22), M1)
        M2 = strassen(int(n/2), (A21 + A22), B11, M2)
        M3 = strassen(int(n/2), A11, (B12 - B22), M3)
        M4 = strassen(int(n/2), A22, (B21 - B11), M4)
        M5 = strassen(int(n/2), (A11 + A12), B22, M5)
        M6 = strassen(int(n/2), (A21 - A11), (B11 + B12), M6)
        M7 = strassen(int(n/2), (A12 - A22), (B21 + B22), M7)

        C = np.vstack([np.hstack([M1+M4-M5+M7, M3 + M5]), np.hstack([M2 + M4, M1 + M3 - M2 + M6])])
    return C

n = 4
A = [[1,2,0,2],[3,1,0,0],[0,1,1,2],[2,0,2,0]]
B = [[0,3,0,2],[1,1,4,0],[1,1,0,2],[0,5,2,0]]
C = np.array(A) @ np.array(B)
D = [[0 for cols in range (n)] for rows in range (n)]
print("쉬트라센 알고리즘")
print(C)
D = strassen(n, A, B, D)
print(D)