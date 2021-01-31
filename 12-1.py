import sys

def main(lines):

    class UnionFind: #UF木の実装
        def __init__(self, n):
            self.parent = [i for i in range(n)]
            self.height = [0 for i in range(n)]

        def get_root(self, i):
            if self.parent[i] == i:
                return i
            else:
                self.parent[i] = self.get_root(self.parent[i])
                return self.parent[i]
        
        def unite(self, i, j):
            ri = self.get_root(i)
            rj = self.get_root(j)
            if ri != rj:
                if self.height[ri] < self.height[rj]:
                    self.parent[ri] = rj
                else:
                    self.parent[rj] = ri
                    if self.height[ri] == self.height[rj]:
                        self.height[ri] += 1
        
        def is_in_group(self, i, j):
            if self.get_root(i) == self.get_root(j):
                return True
            else:
                return False
    
    def kruskal(V, edges): #クラスカル法の実装
        e_sorted = []
        for e in edges:
            e_sorted.append([e[2], e[0], e[1]])
        e_sorted.sort()
        uf_tree = UnionFind(V)
        mst = []
        ans=0
        for e in e_sorted:
            if uf_tree.is_in_group(e[1], e[2])==False:
                uf_tree.unite(e[1], e[2])
                mst.append([e[1], e[2]])
                ans+=e[0]
                
        #mst.sort()
        #print(mst)
        print(ans)

    N,M=[int(x.strip()) for x in lines[0].split()]
    edges=[]
    for i in range(M):
        a,b,d=[int(x.strip()) for x in lines[i+1].split()]
        edges.append([a,b,d])
        edges.append([b,a,d])

    kruskal(N, edges)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
