import sys
from collections import deque
#まず既存の道路で行ける範囲を調べ、そこから行ける範囲をすべての町に広げてゆく
def main(lines):
    N,M,S=[int(x.strip()) for x in lines[0].split()]

    edges=[[] for i in range(N)] #ある町から行ける町のリスト
    for i in range(M):
        a,b=[int(x.strip()) for x in lines[i+1].split()]
        edges[a-1].append(b-1)
    
    edges_r=[[] for i in range(N)] #ある町に来ることができる町のリスト
    for i in range(M):
        a,b=[int(x.strip()) for x in lines[i+1].split()]
        edges_r[b-1].append(a-1)

    def bfs(edges,start): #スタートから行ける範囲すべてを調べる関数
        q=deque()
        done=[0]*N
        done[start]=2
        for n in edges[start]:
            done[n]=1
            q.append(n)
        while len(q):
            node=q.popleft()
            if done[node]!=2:
                done[node]=2
                for n in edges[node]:
                    if done[n]!=2:
                        done[n]=1
                        q.append(n)
        return done

    done=bfs(edges,S-1) #既存の道路で行ける範囲を調べる
    edges2=edges
    m=0 #建設する道路の数
    for i in range(N):
        if done[i]==0:
            if len(edges_r[i])==0: #ある町に現時点でスタートから行くことができず、かつその町に来る道路がない場合はスタートからその町への道路を引く(この町への道路は最低1本は引かなければならない)
                m+=1
                edges[S-1].append(i)

    done=bfs(edges2,S-1) #2回目の行ける範囲の調査
    #ここで残っている町はすべてどこかの町からその町に来る道路を持ち、かつスタートからは行けない
    #→スタートから行ける範囲とは独立したループとそこから枝分かれした町が残っている→そのループを行けない町がなくなるまで1つずつ減らしてゆく
    while 0 in done:
        min0=done.count(0) #doneに含まれる0の最小値→残っている町の最小値
        min_i=0 #そのときのi
        for i in range(N): #行けない町があるならとりあえずそこにスタートから道路を引いてみて、新たにどれだけ多くの町に行けるようになるかを記録、それが最大となるとき(残っている町が最小となるとき)の操作を行う
            if done[i]==0:
                edges2[S-1].append(i)
                done=bfs(edges2,S-1)
                if not 0 in done: #行けない町がなくなったらbreak
                    break
                if done.count(0)<min0: #新たに行けるようになった町の数が最大となるときを更新
                    min0=done.count(0)
                    min_i=i
                edges2[S-1].pop()
        m+=1 #新たに行けるようになる町の数が最大となるように道路を1本引く
        edges2[S-1].append(min_i)
        done=bfs(edges2,S-1)
        
    print(m)

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
