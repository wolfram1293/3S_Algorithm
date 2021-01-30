import sys

def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.

    Q=int(lines[0])
    r=[]
    for i in range(Q):
        li,ri=[int(x.strip()) for x in lines[i+1].split()]
        r.append(ri)

    n=max(r)
    prime=[2]
    lim=int(n**0.5)
    d=[i+1 for i in range(2,n,2)]
    while True:
        p=d[0]
        if lim<p:
            prime=prime+d
            break
        prime.append(p)
        d=[x for x in d if x%p!=0]
    
    prime2=[]
    for i in range(1,len(prime)):
        if (prime[i]+1)/2 in prime:
            prime2.append(prime[i])
    N=len(prime2)
    for i in range(Q):
        l,r=[int(x.strip()) for x in lines[i+1].split()]
        for j in range(N):
            if prime2[j]>=l:
                i1=j
                break
        for j in range(N):
            if prime2[N-1-j]<=r:
                i2=N-1-j
                break

        print(i2-i1+1)

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
