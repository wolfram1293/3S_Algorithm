import sys

def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.
    N,M=[int(x.strip()) for x in lines[0].split()]
    inf=10**9
    dist=[[inf for i in range(N)] for j in range(N)]
    for i in range(N):
        dist[i][i]=0
    for i in range(M):
        a,b,d=[int(x.strip()) for x in lines[i+1].split()]
        dist[a][b]=d
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])
                           
    Q=int(lines[M+1])
    for i in range(Q):
        u,v=[int(x.strip()) for x in lines[i+M+2].split()]
        if dist[u][v]==inf:
            print('INF')
        else:
            print(dist[u][v])

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
