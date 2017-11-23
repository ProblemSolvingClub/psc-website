# Author: Thomas Vu
# Email: thomas.vu@ucalgary.ca
# Feel free to send any questions about this problem to the email above
# or ask in the CPC discord. (discord.gg/MEXwfze)
# ---------------------------------------------------------------------

old1, old2 = input(), input()

old1 = "0" * max(len(old2) - len(old1), 0) + old1
old2 = "0" * max(len(old1) - len(old2), 0) + old2

new1 = new2 = ""

for i in range(len(old1)):
    
    if int(old1[i]) > int(old2[i]):
        new1 += old1[i]

    if int(old1[i]) == int(old2[i]):
        new1 += old1[i]
        new2 += old2[i]

    if int(old1[i]) < int(old2[i]):
        new2 += old2[i]

print("YODA" if len(new1) == 0 else int(new1))
print("YODA" if len(new2) == 0 else int(new2))
