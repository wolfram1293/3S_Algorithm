import sys
import heapq

def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.

    N,M,S=[int(x.strip()) for x in lines[0].split()]
    done=[False]*N
    edges=[[]for i in range(N)]
    inf=10**9
    dist=[inf]*N
    dist[S]=0
    for i in range(M):
        a,b,d=[int(x.strip()) for x in lines[i+1].split()]
        edges[a].append([b,d])

    heap=[]
    heapq.heappush(heap,[dist[S],S])
    while heap:
        node=heapq.heappop(heap)[1]
        if not done[node]:
            for e in edges[node]:
                if dist[e[0]]>dist[node]+e[1]:
                    dist[e[0]]=dist[node]+e[1]
                    heapq.heappush(heap,[dist[e[0]],e[0]])
        done[node]=True

    for i in range(N):
        if dist[i]==inf:
            dist[i]='INF'
    
    print(' '.join(map(str, dist)))

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)


'''
import sys

def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.

    N,M,S=[int(x.strip()) for x in lines[0].split()]
    done = [False]*N
    edges=[[]for i in range(N)]
    inf = 10**9
    dist = [inf]*N
    dist[S]=0
    for i in range(M):
        a,b,d=[int(x.strip()) for x in lines[i+1].split()]
        edges[a].append([b,d])
    #print(edges)
    while 1:
        min_dist=inf
        node=-1
        for i in range(N):
            if (not done[i]) and (min_dist > dist[i]):
                node=i
                min_dist=dist[i]
        if node==-1: break

        for e in edges[node]:
            if dist[e[0]]>dist[node]+e[1]:
                dist[e[0]]=dist[node]+e[1]
        done[node]=True

    for i in range(N):
        if dist[i]==inf:
            dist[i]='INF'
    
    print(' '.join(map(str, dist)))



if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
'''

