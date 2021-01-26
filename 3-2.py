import sys

def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.

    N=int(lines[0])
    A=[int(x.strip()) for x in lines[1].split()]
    Q=int(lines[2])
    l=len(A)
    mi=A[0]
    ma=A[l-1]
    for i in range(Q):
        x=int(lines[i+3])
        if x<mi or x>ma:
            print("No")
        else:
            low=0
            high=l-1
            f=0
            while low<=high:
                mid=(low+high)//2
                if x==A[mid]:
                    f=1
                    break
                if x>A[mid]:
                    low=mid+1
                else:
                    high=mid-1
            if f==1:
                print("Yes")
            else:
                print("No")

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)