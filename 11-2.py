import sys
#スタートから各文字列に流量a、コストiのエッジ、各文字列から各アルファベットに流量(各文字列中の各アルファベットの数)、コスト0のエッジ、
#各アルファベットからゴールに流量(各アルファベットの必要数)、コスト0のエッジを引き、プライマルデュアル法により最小費用流を求める
def main(lines):

    def add_edge(f,t,cap,cost): #グラフのエッジを追加する関数
        G[f].append([t,cap,cost,len(G[t])])
        G[t].append([f,0,-cost,len(G[f])-1])

    def min_cost_flow(s,t,f): #最小費用流を求める関数
        res = 0
        while f > 0:
            #ベルマンフォード法で最短路を求める
            dist=[INF]*V; #最短距離
            dist[s] = 0
            update = True
            while update:
                update = False
                for v in range(V):
                    if dist[v] == INF: continue
                    for i in range(len(G[v])):
                        if G[v][i][1] > 0 and dist[G[v][i][0]] > dist[v] + G[v][i][2]: #最短距離を更新
                            dist[G[v][i][0]] = dist[v] + G[v][i][2]
                            prev_v[G[v][i][0]] = v #直前の頂点、辺も記録
                            prev_e[G[v][i][0]] = i
                            update = True

            if dist[t] == INF: #これ以上流せないなら-1
                return -1

            d = f #流量
            v = t
            #最短路に沿ってできる限り流すというのを繰り返す
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

    T=lines[0]
    N=int(lines[1])
    INF=10**9
    V=1+N+26+1 #頂点数
    G=[[] for i in range(V)] #グラフ
    prev_v=[0 for i in range(V)] #直前の頂点
    prev_e=[0 for i in range(V)] #直前の辺
    for i in range(N):
        s,a=[x.strip() for x in lines[i+2].split()]
        add_edge(0,i+1, int(a), i+1) #スタートから各文字列に流量a、コストiのエッジを引く
        for j in range(26):
            if s.count(chr(ord('a')+j))!=0:
                add_edge(i+1,N+1+j, s.count(chr(ord('a')+j)), 0) #各文字列から各アルファベットに流量(各文字列中の各アルファベットの数)、コスト0のエッジを引く

    for i in range(26):
        if T.count(chr(ord('a')+i))!=0:
            add_edge(N+1+i,V-1, T.count(chr(ord('a')+i)), 0) #各アルファベットからゴールに流量(各アルファベットの必要数)、コスト0のエッジを引く

    print(min_cost_flow(0,V-1,len(T))) #プライマルデュアル法を実行

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
    