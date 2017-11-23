# Author: Thomas Vu
# Email: thomas.vu@ucalgary.ca
# Feel free to send any questions about this problem to the email above
# or ask in the CPC discord. (discord.gg/MEXwfze)
# ---------------------------------------------------------------------

quadkey = input()
inc = 2 ** len(quadkey) // 2
x = y = 0

for ch in quadkey:
    if ch == "1" or ch == "3":
        x += inc
    if ch == "2" or ch == "3":
        y += inc
    inc //= 2

print(len(quadkey), x, y)
