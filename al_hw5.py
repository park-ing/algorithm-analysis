class Node:
    def __init__(self,data):
        self.l_child=None
        self.r_child=None
        self.data=data

def tree(key,r,i,j):
    k=r[i][j]

    if(k==0):
        return
    else:
        p=Node(key[k])
        p.l_child=tree(key,r,i,k-1)
        p.r_child=tree(key,r,k+1,j)
        return p


key=[" ","A","B","C","D","E"]
p=[0,3/15,1/15,2/15,5/15,4/15]
n=len(p)-1

a=[[0 for j in range(0,n+2)] for i in range(0,n+2)]
r=[[0 for j in range(0,n+2)] for i in range(0,n+2)]

for i in range(1,n+1):
    a[i][i-1]=0
    a[i][i]=p[i]
    r[i][i]=i
    r[i][i-1]=0
a[n+1][n]=0
r[n+1][n]=0


for diagonal in range(1,n):
    for i in range(1,n-diagonal+1):
        j=i+diagonal
        temp=[]
        for k in range(i,j+1):
            temp.append(a[i][k-1]+a[k+1][j])
        a[i][j] = min(temp)
        r[i][j] = i + temp.index(a[i][j]) 
        temp.remove

        probability=p[i]
        for q in range(i+1,j+1):
            probability+=p[q]
        a[i][j]+=probability
        tree(key,r,i,j)


def printMatrix(d):
    m=len(d)
    n=len(d[0])
    
    for i in range(0,m):
        for j in range(0,n):
            print("%4d" % d[i][j],end=" ")
        print()

def printMatrixF(d):
    n=len(d[0])
    for i in range(0,n):
        for j in range(0,n):
            print("%5.2f" % d[i][j], end=" ")
        print()
        

def print_inOrder(root):
    if not root:
        return
    print_inOrder(root.l_child)
    print(root.data)
    print_inOrder(root.r_child)

def print_preOrder(root):
    if not root:
        return
    print(root.data)
    print_preOrder(root.l_child)
    print_preOrder(root.r_child)

print("======1번======")
printMatrixF(a)
print()
printMatrix(r)

root=tree(key,r,1,n)
print_inOrder(root)
print()
print_preOrder(root)



a=['C','A','C','A','T','T','A','C','C']
b=['C','A','C','G','T','C','C','A']

m=len(a)
n=len(b)
table=[[0 for j in range(0,n+1)] for i in range(0,m+1)]
minindex=[[(0,0) for j in range(0,n+1)] for i in range(0,m+1)]

for j in range(n-1,-1,-1):
    table[m][j]=table[m][j+1]+2

for i in range(m-1,-1,-1):
    table[i][n]=table[i+1][n]+2


score=0

for i in range(m-1,-1,-1):
    for j in range(n-1,-1,-1):
        if(a[i]==b[j]):
            score=table[i+1][j+1]
        else:
            score=table[i+1][j+1]+1

        table[i][j]=min(score,table[i+1][j]+2,table[i][j+1]+2)

        if(min(score,table[i+1][j]+2,table[i][j+1]+2)==score):
            minindex[i][j]=(i+1,j+1)

        elif(min(score,table[i+1][j]+2,table[i][j+1]+2)==table[i+1][j]+2):
            minindex[i][j]=(i+1,j)
            
        elif(min(score,table[i+1][j]+2,table[i][j+1]+2)==table[i][j+1]+2):
            minindex[i][j]=(i,j+1)


print("======2번======")
printMatrix(table)

x=0
y=0

while(x<m and y<n):
    tx,ty=x,y
    print(minindex[x][y])
    (x,y)=minindex[x][y]
    if x==tx+1 and y==ty+1:
        print(a[tx]," ",b[ty])
    elif x==tx and y==ty+1:
        print(" - ", " ",b[ty])
    else:
        print(a[tx]," "," -")
