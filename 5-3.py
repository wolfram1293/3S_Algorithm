import sys

def main(lines): 
    #累乗の大きさを最小化したい→大きな底ほど小さい冪指数を選べばいい
    #i番目のb^aは合計(N-i)*(i+1)回かけられる→b^(a*(N-i)*(i+1))をかけあわせたものが答え
    #それの最小化のためにはa*(N-i)*(i+1)を小さい順に並べて、それとbを大きい順に並べたものをペアにすればいい
    N=int(lines[0])
    a=[int(x.strip()) for x in lines[1].split()]
    b=[int(x.strip()) for x in lines[2].split()]
    a2=[]
    for i in range(N): #a2にa[i]*(N-i)*(i+1)を入れる
        a2.append(a[i]*(N-i)*(i+1))

    a2.sort() #a2を昇順、bを降順にソートし、ペアにする
    b.sort(reverse=True)
    A=1
    for i in range(N): #b^a2をかけあわせ1000000007で割ったあまりをとる。(計算の効率化のためb^a2もあまりをとる)
        A*=pow(b[i],a2[i],1000000007)
        A%=1000000007

    print(A)

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
