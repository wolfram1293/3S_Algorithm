import sys

def main(lines):
    #削除のパターンは先頭、中間、末尾の3パターン(0文字削除も含む)
    N=int(lines[0])
    S=lines[1]
    p,q=0,N-1 #文字列の前と後ろのポインター
    n=n1=n2=0 #nは出力する長さ

    while q-p>=1: #最初の時点で先頭と末尾の文字が同じなら中間を削除するパターン→違う文字になるまで先頭と末尾を一文字ずつ削除し、先頭か末尾を削除するパターンのどちらかにする
        if S[p]==S[q]:
            p+=1
            q-=1
            n+=2
        else:
            break
    
    #この時点で先頭か末尾を削除するパターンのどちらか→それぞれ先頭、末尾から回文になるまで取り除いていく
    pold=p
    S2=S[p:q+1] #先頭か末尾を削除するパターンのどちらかにしたS
    while q-p>=1: #先頭を削除するパターン
        if S[p]==S[q]: #先頭と末尾が同じ文字なら回文判定
            if S2==S2[::-1]: #回文ならbreak
                n1=len(S2)
                break
            else: #先頭と末尾が同じかつ回文でない→先頭、末尾に連続して並ぶ同じ文字の個数をみて、削除する文字数を判定
                f=S2[0]
                l=len(S2)
                l2=len(S2.lstrip(f))
                ll=l-l2 #先頭に連続して並ぶ同じ文字の個数

                l2=len(S2.rstrip(f))
                lr=l-l2 #末尾に連続して並ぶ同じ文字の個数

                if ll>lr: #先頭の方が多いならll-lrだけ削除、末尾の方が多いなら先頭に並ぶ同じ文字はすべて削除しても良い
                    p+=ll-lr
                else:
                    p+=ll
                S2=S[p:q+1]
        else: #先頭と末尾が違う文字なら先頭に連続して並んだ同じ文字はすべて削除して良い
            f=S2[0]
            l=len(S2)
            S2=S2.lstrip(f)
            l2=len(S2)
            p+=l-l2
    if p==q: #このとき最後に残った1文字は長さにカウントしていないのでカウント
        n1+=1

    p=pold
    S2=S[p:q+1]
    while q-p>=1: #末尾を削除するパターン(先頭を削除する場合の逆パターンで処理は同様)
        if S[p]==S[q]:
            if S2==S2[::-1]:
                n2=len(S2)
                break
            else:
                f=S2[-1]
                l=len(S2)
                l2=len(S2.lstrip(f))
                ll=l-l2

                l2=len(S2.rstrip(f))
                lr=l-l2

                if lr>ll:
                    q-=lr-ll
                else:
                    q-=lr
                S2=S[p:q+1]
        else:
            f=S2[-1]
            l=len(S2)
            S2=S2.rstrip(f)
            l2=len(S2)
            q-=l-l2
    if p==q:
        n2+=1        

    if n1>n2: #先頭と末尾を削除するパターンのどちらかが長い回文になるか判定→中間を取る場合と合計
        n=n+n1
    else:
        n=n+n2
    print(n)

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)