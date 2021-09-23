

# 합병정렬 1번 재귀적방법
def mergesort(n, s):
    h = int(n/2)
    m = int(n - h)
    U = [0] * h
    V = [0] * m

    if (n > 1):
        U = s[:h]
        V = s[h:]
        print("U", U, "V", V, "__",h,"__",m)
        mergesort(h, U)
        mergesort(m, V)
        merge(h,m,U,V,s)
    
 

def merge(h, m, U, V, s):
    i = 1
    j = 1
    k = 1
    print("merge", U, "__", V)
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
    print(s)
    
s = [11,5,2,16,12,1,8,15,6,14,9,3,10,7,13,4]
mergesort(16, s)

        
