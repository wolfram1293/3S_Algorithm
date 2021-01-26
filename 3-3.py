import sys

def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.
    T=int(lines[0])
    for i in range(T):
        X,Y,P,Q=[int(x.strip()) for x in lines[i+1].split()]
        l=Y//Q

        if P==Q or P==0:
            n=-1
        else:
            if X/Y==P/Q:
                n=0
            elif X>P*(l+1):
                n=Q*(1+X//P)-Y
            else:
                while True:
                    if Q*(l+1)-Y>=P*(l+1)-X:
                        n=Q*(l+1)-Y
                        break
                    else:
                        l+=1 
        print(n)

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)