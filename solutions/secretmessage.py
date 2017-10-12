# Author: Thomas Vu
# Email: thomas.vu@ucalgary.ca
# Feel free to send any questions about this problem to the email above
# or ask in the CPC discord. (discord.gg/MEXwfze)
# ---------------------------------------------------------------------

import math

for _ in range(int(input())):
    message = input()
    L = len(message)

    for x in range(1, 101):
        if x ** 2 >= L:
            M = x ** 2
            break

    numAsterisks = M - L
    message += "*" * numAsterisks
    K = int(math.sqrt(M))

    decoded = ""
    for x in range(K):
        for ch in reversed(range(K)):
            sliced = message[K*ch:K*(ch+1)]
            if sliced[x] != "*":
                decoded += sliced[x]

    print(decoded)
