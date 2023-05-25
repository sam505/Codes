# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

q = int(sys.stdin.readline())

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self,item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def front(self):
        return self.items[0]

    def size(self):
        return len(self.items)


def main():
    queue = Queue()
    for _ in range(q):
        action = sys.stdin.readline().split(" ")
        if int(action[0]) == 1:
            queue.enqueue(int(action[1]))
            
        elif int(action[0]) == 2:
            queue.dequeue()
            
        elif int(action[0]) == 3:
            print(queue.front())


if __name__ == "__main__":
    main()
