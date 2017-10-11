# Author: Thomas Vu
# Email: thomas.vu@ucalgary.ca
# Feel free to send any questions about this problem to the email above
# or ask in the CPC discord. (discord.gg/MEXwfze)
# ---------------------------------------------------------------------

for _ in range(int(input())):
    r, e, c = [int(i) for i in input().split()]
    if e - c > r:
        print("advertise")
    elif e - c == r:
        print("does not matter")
    else:
        print("do not advertise")
