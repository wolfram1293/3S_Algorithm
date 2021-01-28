import sys

def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.
    N=int(lines[0])
    S=lines[1]
    p,q=0,N-1
    n=n1=n2=0
    while q-p>=1:
        if S[p]==S[q]:
            p+=1
            q-=1
            n+=2
        else:
            break

    pold=p
    qold=q
    f=0
    while q-p>=1:
        if f==0:
            if S[p]!=S[q]:
                p+=1
            else:
                f=1
                n1=2
        else:
            p2=p+1
            q2=q-1
            while q2-p2>=1:
                if S[p2]==S[q2]:
                    p2+=1
                    q2-=1
                    n1+=2
                else:
                    n1=0
                    f=0
                    p+=1
                    break
            if q2-p2==0:
                n1+=1
                break
            if q2-p2==-1:
                break
    if p==q:
        n1+=1

    p=pold
    q=qold
    f=0
    while q-p>=1:
        if f==0:
            if S[p]!=S[q]:
                q-=1
            else:
                f=1
                n2=2
        else:
            p2=p+1
            q2=q-1
            while q2-p2>=1:
                if S[p2]==S[q2]:
                    p2+=1
                    q2-=1
                    n2+=2
                else:
                    n2=0
                    f=0
                    q-=1
                    break
            if q2-p2==0:
                n2+=1
                break
            if q2-p2==-1:
                break
    if p==q:
        n2+=1

    if n1>n2:
        n=n+n1
    else:
        n=n+n2
    print(n)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)