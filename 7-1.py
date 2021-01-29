import sys

def main(lines):
    #漸化式法での実装
    N,W=[int(x.strip()) for x in lines[0].split()]
    V=0 #全部入れたときの価値の和
    for i in range(1,N+1):
        wi,vi=[int(x.strip()) for x in lines[i].split()]
        V+=vi

    note=[[-1 for j in range(V+1)] for i in range(N+1)] #表
    note[0][0]=0
    Vmax=0 #求める価値の和
    for i in range(1,N+1): #表の更新
        w,v=[int(x.strip()) for x in lines[i].split()]
        for j in range(V+1):
            if j<v:
                note[i][j]=note[i-1][j]
            else:
                if note[i-1][j-v]!=-1:
                    if note[i-1][j]!=-1:
                        note[i][j]=min(note[i-1][j],note[i-1][j-v]+w)
                    else:
                        note[i][j]=note[i-1][j-v]+w
                else:
                    if note[i-1][j]!=-1:
                        note[i][j]=note[i-1][j]
    
    for j in range(V+1): #表のi=Nのとき、要素がWを超えない最大のjが答え
        if note[N][j]<=W and note[N][j]!=-1:
            Vmax=j

    print(Vmax)
if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
