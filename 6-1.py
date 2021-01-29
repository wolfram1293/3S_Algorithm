import sys

def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.

    N=int(lines[0])
    h=[int(x.strip()) for x in lines[1].split()]
    S=[0,abs(h[1]-h[0])] # コストの総和

    for i in range(2,N):
        S1=S[i-1]+abs(h[i]-h[i-1])
        S2=S[i-2]+abs(h[i]-h[i-2])
        if S1<S2:
            S.append(S1)
        else:
            S.append(S2)
    
    print(S[N-1])

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
