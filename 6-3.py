import sys
#数列A中に各数字がどこに入っているか(インデックス)を記録したテーブルを作り、そのテーブルのインデックスがどれだけ連続して入っているかを考える
def main(lines):
    N=int(lines[0])
    A=[int(x.strip()) for x in lines[1].split()]
    table=[0 for i in range(max(A)+1)]
    for i in range(N): #Aを左から順に見て、各数字が最初に出てきたインデックスを入れたテーブルの作成、その数がAになければ0が値として入る
        if table[A[i]]==0:
            table[A[i]]=i+1
        elif table[A[i]-1]!=0: #その数の一つ前の数字が記録されており、その後もう一回出てきた場合はその後最初に出てきたインデックスに更新
            if table[A[i]]<table[A[i]-1]:
                table[A[i]]=i+1

    l=0 #Bの長さ
    index=[] #Bのインデックスを記録
    maxl=1
    for i in range(max(A)+1):
        if table[i]==0: #テーブルの値が0ならスキップ
            l=0
            index=[]
        else:
            if table[i]>table[i-1]: #テーブルの値が前の値より大きい→連続した数字が後ろにある→カウントを増やし、インデックスを記録
                l+=1
                index.append(table[i])
            else: #テーブルの値が前の値より小さい→カウントをリセットし、この数から再スタート
                l=1
                index=[table[i]]
        if l>=maxl: #最大値の更新
            maxl=l
            maxindex=index
        elif l==maxl: #最大値が同じ場合はインデックスの列が辞書順で最小になるものに更新
            if index[0]<=maxindex[0]:
                maxl=l
                maxindex=index

    print(maxl)
    print(' '.join(map(str,maxindex)))

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)