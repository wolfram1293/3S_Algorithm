import sys

def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.
    S=lines[0]
    T=lines[1]
    
    table=[0]*(len(T)+1)
    table[0]=-1
    i,j=0,1
    while j<len(T):
        if T[i]!=T[j] and i>0:
            i=table[i]
        else:
            if T[i]==T[j]:
                i+=1
            j+=1
            table[j]=i

    k=l=0
    while k<len(S) and l<len(T):
        if S[k]==T[l]:
            k+=1
            l+=1
        elif l==0:
            k+=1
        else:
            l=table[l]

    if l==len(T):
        print(k-l)
    else:
        print(-1)

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)

