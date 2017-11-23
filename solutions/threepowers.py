# Author: Thomas Vu
# Email: thomas.vu@ucalgary.ca
# Feel free to send any questions about this problem to the email above
# or ask in the CPC discord. (discord.gg/MEXwfze)
# ---------------------------------------------------------------------

n = int(input())
while n != 0:
    subset = []
    for i, bit in enumerate(reversed(bin(n-1)[2:])):
        if bit == "1":
            subset.append(str(3**i))
    print("{ }" if n == 1 else "{ " + ", ".join(subset) + " }")
    n = int(input())
