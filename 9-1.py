import sys
from collections import deque
def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.
    
    N,M,S,T=[int(x.strip()) for x in lines[0].split()]
    edges=[[] for i in range(N)] #各頂点からつながる頂点のリスト

    for i in range(M):
        a,b=[int(x.strip()) for x in lines[i+1].split()]
        edges[a-1].append(b-1)
        edges[b-1].append(a-1)
    
    done = [0]*N #一度通った頂点を記録
    def dfs(edges, start, end):
        if len(edges[start])==0 or done[start]==1:
            return
        if start==end:
            print('Yes')
            sys.exit()
        done[start]=1
        for n in edges[start]:
            dfs(edges,n, end)

    dfs(edges,S-1,T-1)
    print('No')

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)