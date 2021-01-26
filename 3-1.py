import sys

def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.

    Q=lines[0]
    Q=int(Q)
    N=1000000
    table=['']*N
    for i in range(Q):
        f,x=lines[i+1].split()
        f=int(f)
        x=int(x)
        if f==0:
            n=x%N
            if table[n]=='':
                table[n]=x
            else:
                table.append(x)
        else:
            n=x%N
            if table[n]==x:
                print('found')
            elif table[n]=='':
                print('not found')
            else:
                N2=len(table)
                if N2==N:
                    print('not found')
                else:
                    for j in range(N,N2):
                        if table[j]==x:
                            print('found')
                            break
                        elif j==N2-1:
                            print('not found')

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)