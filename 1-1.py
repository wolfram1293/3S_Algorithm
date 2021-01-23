import sys

def main(lines):

    N,M=[int(x.strip()) for x in lines[0].split()]
    A=[int(x.strip()) for x in lines[1].split()]
    sumA=0
    for i in range(M):
        sumA+=A[i]
    maxA=sumA
    index=1
    for i in range(N-M):
        sumA=sumA+A[M+i]-A[i]
        if maxA<sumA:
            maxA=sumA
            index=i+2

    print(maxA, index)

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)