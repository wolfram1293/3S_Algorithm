import sys

def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.

    #漸化式法での実装
    N,W=[int(x.strip()) for x in lines[0].split()]
    note=[[0 for j in range(W+1)] for i in range(N+1)] #表

    for i in range(1,N+1): #表の更新
        w,v=[int(x.strip()) for x in lines[i].split()]
        for j in range(W+1):
            if j<w:
                note[i][j]=note[i-1][j]
            else:
                if v+note[i-1][j-w]>note[i-1][j]:
                    note[i][j]=v+note[i-1][j-w]
                else:
                    note[i][j]=note[i-1][j]
    
    print(note[N][W]) #N,Wとしたときの値を出力
    
if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)