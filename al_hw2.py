

# 합병정렬 1번 재귀적방법
def mergesort(n, s, cnt):
    h = int(n/2)
    m = int(n - h)
    U = [0] * h
    V = [0] * m
    cnt += (h + m)
#    print("추가공간 : ",h," + ",m)
    if (n > 1):
        U[:h] = s[:h]
        V[:m] = s[h:]
 #       print("U", U, "V", V, "__",h,"__",m)
        cnt,t = mergesort(h, U,cnt)
        mergesort(m, V,cnt)
        merge(h,m,U,V,s)
    return cnt,s

 

def merge(h, m, U, V, s):
    i = 1
    j = 1
    k = 1
 #   print("merge", U, "__", V)
    while(i <= h and j <= m):
        if (U[i-1] < V[j-1]):
            s[k-1] = U[i-1]
            i += 1
        else:
            s[k-1] = V[j-1]
            j += 1
        k += 1
    
    if (i > h):
        s[k-1:h+m] = V[j-1:m]
    else:
        s[k-1:h+m] = U[i-1:h]
 #   print(s)
    
s = [11,5,2,16,12,1,8,15,6,14,9,3,10,7,13,4]
print(mergesort(16, s, 0))


# 합병정렬 2번 공간복잡도 개선 버전
def mergesort2(s, low, high):
    if (low < high):
        mid = int((low + high) / 2)
        mergesort2(s, low, mid)
        mergesort2(s, mid + 1, high)
        merge2(s, low, mid, high)



def merge2(s, low, mid, high):
    i = low
    j = mid + 1
    k = low
    U = [0] * (high + 1)
    cnt = 0
    cnt += (high + 1)
    while(i<=mid and j <= high):
        if(s[i] < s[j]):
            U[k] = s[i]
            i += 1
        else:
            U[k] = s[j]
            j += 1
        k += 1

    if(i>mid):
        U[k:high+1] = s[j:high+1]
    else:
        U[k:high+1] = s[i:mid+1]        
    s[low:high+1] = U[low:high+1]
    print("mergesort2",s)
    print("발생한 추가공간", cnt)



s = [11,5,2,16,12,1,8,15,6,14,9,3,10,7,13,4]
mergesort2(s,0,15)

