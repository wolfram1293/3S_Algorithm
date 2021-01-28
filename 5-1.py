import sys

def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.

    #N=int(lines[0])
    A=[int(x.strip()) for x in lines[1].split()]
    def babblesort(a):
        l=len(a)
        for i in range(l):
            for j in range(l-1,i,-1):
                if a[j-1]>a[j]:
                    a[j],a[j-1]=a[j-1],a[j]
        return a
    A=babblesort(A)
    print(' '.join(map(str,A)))
    

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)