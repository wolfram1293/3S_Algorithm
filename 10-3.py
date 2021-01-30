import sys

def main(lines):
    T=int(lines[0])
    count=1
    for l in range(T):
        N,M=[int(x.strip()) for x in lines[count].split()]
        count+=1
        inf=10**9
        cost=[[inf for i in range(N)] for j in range(N)]
        for i in range(N):
            cost[i][i]=0
        for j in range(M):
            a,b,c=[int(x.strip()) for x in lines[count+j].split()]
            cost[a-1][b-1]=c
            cost[b-1][a-1]=c
        count+=M
        A=[int(x.strip()) for x in lines[count].split()]
        count+=1
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    cost[i][j]=min(cost[i][j],cost[i][k]+cost[k][j])
        
        #print(cost)
        min_cost=[inf]*N
        for i in range(N):
            for j in range(N):
                if 2*cost[i][j]+A[j]<min_cost[i]:
                    min_cost[i]=2*cost[i][j]+A[j]

        print(' '.join(map(str,min_cost)))
    
if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)

################################################################

import sys
import heapq

def main(lines):
    T=int(lines[0])
    count=1
    for l in range(T):
        N,M=[int(x.strip()) for x in lines[count].split()]
        count+=1
        inf=10**9
        cost=[[inf for i in range(N)] for j in range(N)]
        for i in range(N):
            cost[i][i]=0

        edges=[[]for i in range(N)]
        for j in range(M):
            a,b,c=[int(x.strip()) for x in lines[count+j].split()]
            edges[a-1].append([b-1,c])
            edges[b-1].append([a-1,c])
        count+=M

        A=[int(x.strip()) for x in lines[count].split()]
        count+=1

        for i in range(N):
            done=[False]*N
            heap=[]
            heapq.heappush(heap,[cost[i][i],i])
            while heap:
                node=heapq.heappop(heap)[1]
                if not done[node]:
                    for e in edges[node]:
                        if cost[i][e[0]]>cost[i][node]+e[1]:
                            cost[i][e[0]]=cost[i][node]+e[1]
                            heapq.heappush(heap,[cost[i][e[0]],e[0]])
                done[node]=True
        
        min_cost=[inf]*N
        for i in range(N):
            for j in range(N):
                if 2*cost[i][j]+A[j]<min_cost[i]:
                    min_cost[i]=2*cost[i][j]+A[j]

        print(' '.join(map(str,min_cost)))
    
if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)

#############################################################

import sys
import heapq

def main(lines):
    T=int(lines[0])
    count=1
    for l in range(T):
        N,M=[int(x.strip()) for x in lines[count].split()]
        count+=1
        inf=10**9
        
        edges=[[]for i in range(N)]
        for j in range(M):
            a,b,c=[int(x.strip()) for x in lines[count+j].split()]
            edges[a-1].append([b-1,c])
            edges[b-1].append([a-1,c])
        count+=M

        A=[int(x.strip()) for x in lines[count].split()]
        count+=1

        min_cost=[inf]*N
        for i in range(N):
            cost=[inf]*N
            cost[i]=0
            done=[False]*N
            heap=[]
            heapq.heappush(heap,[cost[i],i])
            while heap:
                node=heapq.heappop(heap)[1]
                if not done[node]:
                    for e in edges[node]:
                        if cost[e[0]]>cost[node]+e[1]:
                            cost[e[0]]=cost[node]+e[1]
                            heapq.heappush(heap,[cost[e[0]],e[0]])
                done[node]=True

            for j in range(N):
                if 2*cost[j]+A[j]<min_cost[i]:
                    min_cost[i]=2*cost[j]+A[j]

        print(' '.join(map(str,min_cost)))

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
