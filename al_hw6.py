print("1번")

inf=1000
w=[[0,7,4,6,1],
   [inf,0,inf,inf,inf],
   [inf,2,0,5,inf],
   [inf,3,inf,0,inf],
   [inf,inf,inf,1,0]]


n=len(w)
f=set()
touch=n*[0]
length=n*[0]
save_length=n*[0]


def dijkstra(n, w, f):
    for i in range(1,n):
        touch[i]=0
        save_length[i]=0
        length[i]=w[0][i] #[7,4,6,1]

    
    count=0
    while (count < n-1):
        minval=2**32
        for i in range(1,n):
            if length[i]>=0 and length[i]<minval:
                minval=length[i]
                vnear=i
        f.add((touch[vnear],vnear))

        for i in range(1,n):
            if length[vnear]+w[vnear][i]<length[i]:
                length[i]=length[vnear]+w[vnear][i]
                touch[i]=vnear

        save_length[vnear]=length[vnear]
        length[vnear]=-1
        count+=1


        
dijkstra(n, w, f)
print(f)
print(save_length)

print("2번")
def promising(i,col):
    k=0
    switch=True
    while k<i and switch==True:
        if col[i]==col[k] or abs(col[i]-col[k])==i-k:
            switch=False
        k+=1
    return switch


def queens(n,i,col,t):
    t_val = []
    cnt = 0
    if promising(i,col):
        if i==n-1:
 #           print('[',end="")
            for j in range(0,n):
                if j!=n-1:
 #                   print(col[j],end=",")
                    t_val.append(col[j])
                else:
 #                   print(col[j],end="")
 #                   print(']')
                    t_val.append(col[j])
            cnt += 1
            t.append(t_val)    
        elif i<n-1:
            for k in range(0,n):
                col[i+1]=k
                queens(n,i+1,col,t)
    return t

n=7
col=n*[0]
solution=n*[0]
t = []
t = queens(n,-1,col,t)

print("해의 총개수 : ", len(t))
print("두 번째 해 : ", t[1])