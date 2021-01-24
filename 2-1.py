import sys

def main(lines):
    Q=int(lines[0])
    class Queue:
        def __init__(self,size: int):
            self.queue=[None for i in range(size)]
            self.size=size
            self.head=0
            self.tail=0

        def enqueue(self,a: int):
            if self.head==(self.tail+1)%self.size:
                print("full")
                return False
            self.queue[self.tail]=a
            self.tail=(self.tail+1)%self.size

        def dequeue(self):
            if self.head==self.tail:
                print("empty")
                return False
            a=self.queue[self.head]
            self.head=(self.head+1)%self.size
            return a

    q=Queue(Q)
    for i in range(Q):
        l=[int(x.strip()) for x in lines[i+1].split()]
        if l[0]==1:
            q.enqueue(l[1])
        else:
            print(q.dequeue())
            
if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)