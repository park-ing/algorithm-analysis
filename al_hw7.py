print("1번 문제")

def promising(i,weight, total):
    if (weight+total >= W) and (weight == W or weight+w[i+1] <= W):
        return True
    else:
        return False

def s_s(i, weight, total, include):
    if(promising(i, weight, total)):
        if (weight == W):
            print("sol",include)
        else:
            include[i+1] = 1
            s_s(i+1, weight+w[i+1],total-w[i+1],include)
            include[i+1] = 0
            s_s(i+1, weight, total-w[i+1],include)

n = 6
w = [1,2,3,4,5,6]
W = 11
print("item =", w, "W =", W)
include = n*[0]
total = 0
for k in range(len(w)):
    total += w[k]
s_s(-1,0,total,include)


print("2번 문제")

def color(i, vcolor):
    if promising(i,vcolor):
        if(i == n-1):
            print(vcolor)
        else:
            for Color in range(1,m+1):
                vcolor[i+1] = Color
                color(i+1,vcolor)

def promising(i, vcolor):
    switch = True
    j = 0
    while(j < i and switch):
        if(W[i][j] and vcolor[i] == vcolor[j]):
            switch = False
        j += 1

    return switch

n = 5
W = [[0,1,1,0,1],[1,0,1,0,0],[1,1,0,1,1],[0,0,1,0,1],[1,0,1,1,0]]
vcolor = n*[0]
m = 3
color(-1,vcolor)