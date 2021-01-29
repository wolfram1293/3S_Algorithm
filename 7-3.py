import sys
#ある区間[i,j]における操作の回数の最小値を表dp[i][j]に入れる。区間をすべての範囲にしたときが答え
def main(lines):
    N=int(lines[0])
    c=[int(x.strip()) for x in lines[1].split()]
    dp=[[-1 for j in range(N)] for i in range(N)] #表

    for j in range(N): #表の更新
        for i in range(N-1,-1,-1):
            if j-i==0: #ブロックが1つなら0回
                dp[i][j]=0
            
            elif j-i==1: #ブロックが2つ
                if c[i]==c[i+1]: #[i,j]を[i+1,j]とiで分けたとき、操作回数はiとi+1が同じ色ならdp[i+1][j]と同じ、違う色ならdp[i+1][j]+1回
                    x=dp[i+1][j]
                else:
                    x=dp[i+1][j]+1

                if c[j-1]==c[j]: #[i,j]を[i,j-1]とjで分けたときも同様
                    y=dp[i][j-1]
                else:
                    y=dp[i][j-1]+1
                
                dp[i][j]=min(x,y) #最小のものを表に代入

            elif j-i>=2: #ブロックが2つ以上
                if c[i]==c[i+1]: #[i+1,j]とiで分けたとき
                    x=dp[i+1][j]
                else:
                    x=dp[i+1][j]+1

                if c[j-1]==c[j]: #[i,j-1]とjで分けたとき
                    y=dp[i][j-1]
                else:
                    y=dp[i][j-1]+1
                
                if c[i]==c[j]: #[i,j]をi、[i+1,j-1]、jと分けたとき、iとjが同じ色ならdp[i+1][j-1]+1回の操作で同じ色になる。違う色ならdp[i+1][j-1]+2回
                    z=dp[i+1][j-1]+1
                else:
                    z=dp[i+1][j-1]+2
                dp[i][j]=min(x,y,z) #最小のものを表に代入

    print(dp[0][N-1])

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
