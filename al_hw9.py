
class Heap(object):
    n = 0

    def __init__(self, data):
        self.data = data
        self.n = len(self.data) - 1
    
    def addElem(self, elem):
        self.data.append(elem)
        self.n += 1
        self.makeHeap2()
    
    def siftDown(self, i):
        left_index = i * 2
        right_index = i * 2 + 1
        cur = i

        if (left_index <= self.n) and (self.data[left_index] > self.data[cur]):
            cur = left_index
        if (right_index <= self.n) and (self.data[right_index] > self.data[cur]):
            cur = right_index
        if (cur != i):
            temp = self.data[cur]
            self.data[cur] = self.data[i]
            self.data[i] = temp
            self.siftDown(i)



    def makeHeap2(self):
        for i in range (self.n//2, 0, -1):
            self.siftDown(i)
        return self.data

def heapSort(a):
    t = []
    n = len(a) - 1

    for i in range (n, 0, -1):
        t.append(a[1])
        del a[1]
        b = Heap(a).makeHeap2()
        a = b

    a = t
    return a
    

a = [0, 11, 14, 2, 7, 6, 3, 9, 5]
b = Heap(a)
b.makeHeap2()
print(b.data)
b.addElem(50)
print(b.data)
s = heapSort(a)
print(s)

    