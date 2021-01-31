import sys
import heapq

def main(lines):

    def prim(V, edges): #プリム法の実装
        edges2 = [[] for i in range(V)]
        for e in edges:
            edges2[e[0]].append([e[2], e[0], e[1]])
        heap = []
        mst = []
        done = [False]*V
        start=0
        done[start] = True
        for i in range(len(edges2[start])):
            heapq.heappush(heap,edges2[start][i])
        ans=0
        while heap:
            e=heapq.heappop(heap)
            if done[e[2]]==False:
                done[e[2]]=True
                mst.append([e[1], e[2]])
                for i in range(len(edges2[e[2]])):
                    heapq.heappush(heap,edges2[e[2]][i])
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

    prim(N,edges)

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
