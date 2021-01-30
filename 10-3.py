import sys
import heapq
#計算量を減らすためダイクストラ法で実装した。
#ある町へ行って、コンサートを見て帰って来るときのコストはその町までの往復分の交通費とその町でのコンサートのチケットの料金の合計である。
#これをダイクストラ法で実装するために、新たなノードを設定し、各町でのチケットの料金はそのノードから各町へのエッジのコストとする。
#よってまず、それぞれの町のノードに加え、スタート地点にするノードを設定し、そこから各町へコンサートのチケットの料金分のコストで移動する。
#その後、往復分の交通費をコストとしながらそれぞれの町へ移動し、最小値を更新し続ければ、各町のノードにはその町から出発したときのコストの最小値に相当するものが入っている。
#これにより単⼀始点最短経路問題に帰着でき、各テストケースについて1回ずつダイクストラ法を実行するだけで答えが求まり、計算量が削減できる。
def main(lines):
    T=int(lines[0])
    count=1 #入力の読み込みカウント
    for l in range(T):
        N,M=[int(x.strip()) for x in lines[count].split()]
        count+=1
        inf=10**9
        
        edges=[[]for i in range(N+1)] #スタート地点にするノードを含めて初期化
        for i in range(M): #それぞれの町のノードをつなげる
            a,b,c=[int(x.strip()) for x in lines[count+i].split()]
            edges[a-1].append([b-1,c])
            edges[b-1].append([a-1,c])
        count+=M
        A=[int(x.strip()) for x in lines[count].split()]
        count+=1
        for i in range(N): #スタート地点にするノードとそれぞれの町をその町でのコンサートのチケットの料金をコストに持つ有向エッジでつなげる
            edges[N].append([i,A[i]])
        cost=[inf]*(N+1)
        cost[N]=0
        done=[False]*(N+1)
        heap=[]
        heapq.heappush(heap,[cost[N],N]) #スタート地点にするノードからダイクストラ法を開始
        while heap:
            node=heapq.heappop(heap)[1]
            if not done[node]:
                for e in edges[node]:
                    if node==N: #スタート地点にするノードから移動する場合はエッジのコスト(コンサートのチケットの料金)分コストを足す
                        cost[e[0]]=cost[node]+e[1]
                        heapq.heappush(heap,[cost[e[0]],e[0]])
                    else: #それ以外は往復分より、2倍の交通費を足す
                        if cost[e[0]]>cost[node]+2*e[1]:
                            cost[e[0]]=cost[node]+2*e[1]
                            heapq.heappush(heap,[cost[e[0]],e[0]])
            done[node]=True
        
        min_cost=cost[:-1] #costからスタート地点にするノードを除いたものが各町から出発したときのコストの最小値

        print(' '.join(map(str,min_cost)))
    
if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
