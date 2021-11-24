print("1번 문제")

def knapsack(i, profit, weight):
    global bestset
    global maxprofit
    global cnt 
    cnt += 1
    if(weight <= W) and (profit > maxprofit):
        maxprofit = profit
        numbest = i
        bestset = include[:]

    if(promising(i, weight, profit)):
        include[i+1] = 1
        knapsack(i+1, profit + p[i+1], weight+w[i + 1])
        include[i+1] = 0
        knapsack(i+1, profit, weight)

def promising(i, weight, profit):
    global maxprofit

    if (weight >= W):
        return False
    else:
        j = i + 1
        bound = profit
        totweight = weight
        while(j<n) and (totweight + w[j] <= W):
            totweight = totweight + w[j]
            bound = bound + p[j]
            j += 1
        
        k = j
        if (k<n):
            bound = bound + (W-totweight)*p[k]/w[k]

        return bound > maxprofit

n = 4
W = 16
p = [20,40,24,40]
w=[2,5,4,8]
cnt = 0
maxprofit = 0
include=[0,0,0,0]
bestset=[0,0,0,0]
knapsack(-1,0,0)
print(maxprofit)
print(bestset)
print("총 노드의 개수 : ",cnt)


print("2번 문제")

import queue
import copy
def cmp(a, b):
    return (a > b) - (a < b)

class Node:
    def __init__(self,level, weight, profit, bound, include):
        self.level = level
        self.weight = weight
        self.profit = profit
        self.bound = bound
        self.include = include


        
def kp_Best_Fs():
    global maxprofit
    global bestset
    global cnt
    global n

    temp = n*[0]
    v = Node(-1,0,0,0.0,temp)
    q = queue.PriorityQueue()
    v.bound = comBound(v)
    q.put((-v.bound,v))
    u = Node(0,0,0,0.0,bestset)
    temp = Node
    cnt = 1

    while (not q.empty()):
        v = q.get()[1]
        if(v.bound > maxprofit):
            u.level = v.level + 1
            u.weight = v.weight + w[u.level]
            u.profit = v.profit + p[u.level]
            u.include = v.include

            if(u.weight <= W) and (u.profit > maxprofit):
                maxprofit = u.profit

            u.bound = comBound(u)
            t = u.bound
            #print(u.level, u.weight, u.profit, u.bound,u.include)
            u.include[u.level] = 1
            if (u.bound > maxprofit):
                temp = copy.deepcopy(u)  #메모리 저장 주소 같아지는 것을 방지
                q.put((-temp.bound,temp)) #최대값부터 추출하기 위해 key값에 음수 취함
            #print(u.include)
                
            u.weight = v.weight
            u.profit = v.profit

            u.bound = comBound(u)
            #print(u.level, u.weight, u.profit, u.bound,u.include)

            u.include[u.level] = 0
            if (u.bound > maxprofit):
                temp = copy.deepcopy(u)
                q.put((-temp.bound,temp))
            #print(temp.include)
    
            bestset = u.include[:]
            if (u.level == n-1):
                if (t > u.bound):
                    bestset[u.level] = 1
                else:
                    bestset[u.level] = 0
            cnt += 2
            
    

def comBound(u):
    if (u.weight >= W):
        return 0
    else:
        result = u.profit
        j = u.level + 1
        totweight = u.weight
        while(j < n) and (totweight + w[j] <= W):
            totweight += w[j]
            result += p[j]
            j += 1
        k = j
        if (k < n):
            result = result + (W-totweight)*p[k]/w[k]

        return result

n = 4
W = 16
p = [20,40,24,40]
w=[2,5,4,8]
include=[0]*n
maxprofit = 0
bestset = n*[0]
cnt = 1
kp_Best_Fs()
print(bestset)
print(maxprofit)
print("노드의 총 수 : ", cnt)
















