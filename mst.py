import heapq

class Graph:
    def __init__(self, vertices):
        #to define max size of ids
        maxI = 0
        self.pq = []
        heapq.heapify(self.pq)
        for v in vertices:
            u,v,w = v
            heapq.heappush(self.pq, [w,u,v])
            maxI = maxI if u <= maxI else u
            maxI = maxI if v <= maxI else v

        maxI+=1
        self.ids = [None] * maxI
        self.sz = [None] * maxI
        for i in range(maxI):
            self.ids[i] = i
            self.sz[i] = 1
        self.mstq = []

    def find(self, i):
        while self.ids[i] != i:
            self.ids[i] = self.ids[self.ids[i]]
            i = self.ids[i]        
        return i

    def connected(self, u, v):
        return self.find(u) == self.find(v)

    def union(self, u, v):
        uroot = self.find(u)
        vroot = self.find(v)
        
        if uroot == vroot:
            return

        if self.sz[uroot] > self.sz[vroot]:
            self.ids[vroot] = uroot
            self.sz[vroot] += self.sz[uroot]
        else:
            self.ids[uroot] = vroot
            self.sz[uroot] += self.sz[vroot]

    def mst(self):
        while self.pq:
            w, u, v = heapq.heappop(self.pq)
            if not self.connected(u, v):
                self.union(u, v)
                self.mstq.append([u,v,w])