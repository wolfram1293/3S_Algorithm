import sys

def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.
    S=lines[0]
    T=lines[1]
    a=1007
    h=10**9+7
    Slen=len(S)
    Tlen=len(T)
    Shash=0
    Thash=0
    num=lambda c:ord(c)-ord('a')
    am=1
    for i in range(Tlen):
        Shash+=num(S[Tlen-i-1])*am
        Thash+=num(T[Tlen-i-1])*am
        am*=a
        am=am%h
    Shash=Shash%h
    Thash=Thash%h

    for i in range(Slen-Tlen+1):
        if i!=0:
            Shash=(a*Shash+num(S[Tlen+i-1])-am*num(S[i-1]))%h
        if Shash==Thash:
            print(i)

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)

