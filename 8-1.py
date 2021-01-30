import sys

def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.
    N=int(lines[0])
    K=int(lines[1])
    M=1000000007
    a=1
    for i in range(N-K):
        a*=i+1
        a%=M
    b=a
    for i in range(N-K,N):
        b*=i+1
        b%=M
    ans=pow(a,M-2,M)
    ans*=b
    ans%=M
    print(ans)

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
