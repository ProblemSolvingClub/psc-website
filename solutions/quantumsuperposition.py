# Author: Martin Tran
# Email: martin.tran@ucalgary.ca
# Feel free to send any questions about this problem to the email above
# or ask in the CPC discord. (discord.gg/MEXwfze)
# ---------------------------------------------------------------------
import sys

sys.setrecursionlimit(2000)  # PYTHON WILL CRASH WITHOUT THIS LINE!!!!


n1, n2, m1, m2 = [int(x) for x in input().split()]

u1, u2 = {i:set() for i in range(1, n1+1)}, {i:set() for i in range(1, n2+2)}

memo1, memo2 = {}, {}

for _ in range(m1):  # Make the DAG for universe 1
    u, v = [int(x) for x in input().split()]
    u1[u].add(v)

for _ in range(m2):  # Make the DAG for universe 2
    u, v = [int(x) for x in input().split()]
    u2[u].add(v)

def solve1(node):  # Solve the DAG for universe 1
    if node in memo1:
        return memo1[node]
    if node == n1:
        return set([0])
    aset = set()
    for child in u1[node]:
        aset |= set(map(lambda x: x+1, solve1(child)))
    memo1[node] = aset
    return aset


def solve2(node):  # Solve the DAG for universe 2
    if node in memo2:
        return memo2[node]
    if node == n2:
        return set([0])
    aset = set()
    for child in u2[node]:
        aset |= set(map(lambda x: x+1, solve2(child)))
    memo2[node] = aset
    return aset


paths1 = solve1(1)
paths2 = solve2(1)


for _ in range(int(input())):
    q = int(input())
    for possib in paths1:
        if q-possib in paths2:
            print('Yes')
            break
    else:
        print('No')    
    
