
class UnionFind:
    def __init__(self):
        self.father = {}
        self.num_of_sets = 0
    
    def find(self, x):
        while x != self.father[x]:
            x = self.father[x]
        return x
    
    def merge(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return False
        
        self.father[y_root] = x_root
        self.num_of_sets -= 1
        return True
        
        
    def add(self, x):
        if x not in self.father:
            self.father[x] = x
            self.num_of_sets += 1
    
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        uf = UnionFind()
        if len(edges) < n - 1:
            return False
        set_count = 1
        for i in range(n):
            uf.add(i)
        for x, y in edges:
            res = uf.merge(x,y)
            if not res:
                return False
            
        if set_count > 1:
            return False
        
        return True
