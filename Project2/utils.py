
import heapq

class Stack:
    def __init__(self): self.list=[]
    def push(self,i): self.list.append(i)
    def pop(self): return self.list.pop()
    def isEmpty(self): return len(self.list)==0

class Queue:
    def __init__(self): self.list=[]
    def push(self,i): self.list.insert(0,i)
    def pop(self): return self.list.pop()
    def isEmpty(self): return len(self.list)==0

class PriorityQueue:
    def __init__(self):
        self.heap=[]
        self.count=0
    def push(self,item,priority):
        heapq.heappush(self.heap,(priority,self.count,item))
        self.count+=1
    def pop(self):
        return heapq.heappop(self.heap)[2]
    def isEmpty(self):
        return len(self.heap)==0
