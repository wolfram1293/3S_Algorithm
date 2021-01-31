V=100

def BellmanFord(V, e_list):
    inf = 10**9
    dist = [inf]*V
    dist[0] = 0
    for j in range(V):
        for e in e_list:
            if dist[e[1]] > e[2] + dist[e[0]]:
                dist[e[1]] = e[2] + dist[e[0]]
                # 負の閉路の検知
                if j==V-1: return -1
    print(dist)

edges_list2 = [[0, 1, 5], [0, 2, 4], [1, 0, 5], [1, 3, 9], [1, 5, 9],
[2, 0, 4], [2, 3, 2], [2, 4, 3], [3, 1, 9], [3, 2, 2], [3, 5, 1], [3, 6, 7],
[4, 2, 3], [4, 6, 8], [5, 1, 9], [5, 3, 1], [5, 6, 2], [5, 7, 5], [6, 3, 7],
[6, 4, 8], [6, 5, 2], [6, 7, 2], [7, 5, 5], [7, 6, 2]]

def min_cost_flow(s,t,f):
    res = 0
    while f > 0:
        # ベルマンフォード法により、s-t間最短路を求める
        dist=[INF]*V; # 最短距離
        dist[s] = 0
        update = True
        while update:
            update = False
            for v in range(V):
                if dist[v] == INF: continue
                for i in range(len(G[v])):
                    if G[v][i][1] > 0 and dist[G[v][i][0]] > dist[v] + G[v][i][2]:
                        dist[G[v][i][0]] = dist[v] + G[v][i][2]
                        prev_v[G[v][i][0]] = v
                        prev_e[G[v][i][0]] = i
                        update = True

        if dist[t] == INF:
            # これ以上流せない
            return -1

        # s-t間最短路に沿って目一杯流す
        d = f
        v = t
        while  v != s:
            d = min(d, G[prev_v[v]][prev_e[v]][1])
            v = prev_v[v]
        
        f -= d
        res += d*dist[t]
        v = t
        while  v != s:
            G[prev_v[v]][prev_e[v]][1] -= d
            G[v][G[prev_v[v]][prev_e[v]][3]][1] += d
            v = prev_v[v]
            
    return res



def add_edge(f,t,cap,cost):
    G[f].append([t,cap,cost,len(G[t])])
    G[t].append([f,0,-cost,len(G[f])-1])

INF=10**9
V=4 # 頂点数
G=[[] for i in range(V)] # グラフの隣接リスト表現

prev_v=[0 for i in range(V)]
prev_e=[0 for i in range(V)] # 直前の頂点と辺

add_edge(0,1, 3, 6)
add_edge(0,2, 5, 2)
add_edge(1,3, 4, 3)
add_edge(2,1, 7, 3)
add_edge(2,3, 6, 9)



# 辺を表す構造体 (行き先、容量、コスト、逆辺)

#G = [[[1, 3, 6], [2, 5, 2]], [[3, 4, 3]],[[1, 7, 3], [3, 6, 9]],[]]
# sからtへの流量fの最小費用流を求める
# 流せない場合は-1を返す
min_cost_flow(0,3,7)