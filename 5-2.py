import sys

def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.

    #N=int(lines[0])
    A=[int(x.strip()) for x in lines[1].split()]

    def quicksort(a):
        if len(a)<=1:
            return a

        left=[]
        right=[]
        pivot=a[len(a)//2]
        count=0
        for i in range(len(a)):
            e=a[i]
            if e==pivot:
                count+=1
            elif e<pivot:
                left.append(e)
            else:
                right.append(e)
                
        left=quicksort(left)
        right=quicksort(right)
        return left+[pivot]*count+right

    print(' '.join(map(str,quicksort(A))))
    
if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)