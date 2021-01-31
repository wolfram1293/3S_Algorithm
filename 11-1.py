import sys

def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.

    # 隣接リストでの実装
    N,M=[int(x.strip()) for x in lines[0].split()]
    edges=[[[i,0]for i in range(N)]for j in range(N)]
    for i in range(M):
        u,v,c=[int(x.strip()) for x in lines[i+1].split()]
        edges[u-1][v-1][1]=c
    
    max_flow = 0
    start=0
    end=N-1

    def dfs(s, e, flow):
        if (s == e): return flow
        visited[s] = True
        for i in range(len(edges[s])):
            if edges[s][i][1]>0 and not visited[edges[s][i][0]]:
                f = dfs(i, e, min(flow, edges[s][i][1]))
                if f > 0:
                    edges[s][i][1] -= f
                    edges[i][s][1] += f
                    return f
        return 0

    while True:
        visited = [False]*N
        f = dfs(start,end,10**9)
        if f==0: break
        max_flow += f

    print(max_flow)

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

    N,M=[int(x.strip()) for x in lines[0].split()]
    capacity=[[0 for i in range(N)] for j in range(N)]
    for i in range(M):
        u,v,c=[int(x.strip()) for x in lines[i+1].split()]
        capacity[u-1][v-1]=c
    
    max_flow = 0
    start=0
    end=N-1

    def dfs(s, e, flow):
        if (s == e): return flow
        visited[s] = True
        for i in range(len(capacity[s])):
            if not visited[i] and capacity[s][i]>0:
                f = dfs(i, e, min(flow, capacity[s][i]))
                if f > 0:
                    capacity[s][i] -= f
                    capacity[i][s] += f
                    return f
        return 0

    while True:
        visited = [False]*N
        f = dfs(start,end,10**9)
        if f==0: break
        max_flow += f

    print(max_flow)
if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)

'''
'''
import sys

def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.

    N,M=[int(x.strip()) for x in lines[0].split()]
    edges=[[]for i in range(N)]
    for i in range(M):
        u,v,c=[int(x.strip()) for x in lines[i+1].split()]
        edges[u-1].append([v-1,c])
    
    max_flow = 0
    start=0
    end=N-1
    #print(edges)

    def dfs(s, e, flow):
        if (s == e): return flow
        visited[s] = True
        for i in range(len(edges[s])):
            if edges[s][i][1]>0 and not visited[edges[s][i][0]]:
                f = dfs(i, e, min(flow, edges[s][i][1]))
                if f > 0:
                    edges[s][i][1] -= f
                    for j in range(len(edges[edges[s][i][0]])):
                        if edges[edges[s][i][0]][j][0]==s:
                            edges[edges[s][i][0]][j][1] += f
                            break
                    return f
        return 0

    while True:
        visited = [False]*N
        f = dfs(start,end,10**9)
        if f==0: break
        max_flow += f

    print(max_flow)

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
'''