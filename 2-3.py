import sys

def main(lines):
    #N,K=map(int,input().split())
    N,K=[int(x.strip()) for x in lines[0].split()]
    S=[int(x.strip()) for x in lines[1].split()]
    n=0
    count=0
    for i in range(len(S)):
        if S[i]=='(':
            count+=1
        else:
            count-=1
        if count==0:
            n+=1
    print(n//N)

    
if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)