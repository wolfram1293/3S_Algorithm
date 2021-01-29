import sys

def main(lines):
    N,K=[int(x.strip()) for x in lines[0].split()]
    A=[int(x.strip()) for x in lines[1].split()]
    note=[[0 for j in range(K+1)] for i in range(N+1)] #表
    note[0][0]=1
    for i in range(1,N+1): #表の更新
        f=0
        note[i][0]=1
        for j in range(1,K+1):
            if j-A[i-1]<0:
                note[i][j]=note[i][j-1]+note[i-1][j]
                note[i][j]%=10**9+7
            else:
                if f==0:
                    for k in range(j-A[i-1],j+1):
                        note[i][j]+=note[i-1][k]
                    note[i][j]%=10**9+7
                    f=1
                else:
                    note[i][j]=note[i][j-1]+note[i-1][j]-note[i-1][j-A[i-1]-1]
                    note[i][j]%=10**9+7

    print(note[N][K])

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
