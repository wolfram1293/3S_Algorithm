import sys
#整数Nの約数全てをかけた値の中に各素因数が何回かけられているかを考える
def main(lines):
    M=int(lines[0])
    p=[int(x.strip()) for x in lines[1].split()]
    h=1000000007
    a=list(set(p)) #素因数を重複なく取り出したリスト
    b=[] #aの各素因数をNはそれぞれ何個持つかを入れたリスト
    for i in range(len(a)):
        b.append(p.count(a[i]))
    b1=1 #約数の個数は各素因数の組み合わせの数より、(各素因数の数+1)をかけ合わせたもの
    for i in range(len(a)):
        b1*=b[i]+1

    ans=1
    for i in range(len(a)):
        b2=0 #素因数a[i]のかけられる総数
        for j in range(b[i]): #素因数a[i]自身の個数としてありえる組み合わせは1,2,...,b[i]よりその和を出す
            b2+=j+1
        
        b2*=b1//(b[i]+1) #さらにそれ以外の素因数の組み合わせの数をかければ素因数a[i]がかけられる回数となる
        ans*=pow(a[i],b2,h)
        ans%=h
    #これを各素因数について行えば答え
    print(ans)

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
