# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys

queries = int(sys.stdin.readline())

S = ""
S_previous = []
ops = []
for _ in range(queries):
    ops.append(sys.stdin.readline().strip().split(" "))
    
for commands in ops:
    if commands[0] == '1':
        S_previous.append(S)
        S += commands[1]
    elif commands[0] == '2':
        idx = int(commands[1]) * -1
        S_previous.append(S)
        S = S[:idx]
    elif commands[0] == '3':
        print(S[int(commands[1])-1])
    elif commands[0] == '4':
        S = S_previous.pop()
        
