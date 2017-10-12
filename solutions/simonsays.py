# Author: Thomas Vu
# Email: thomas.vu@ucalgary.ca
# Feel free to send any questions about this problem to the email above
# or ask in the CPC discord. (discord.gg/MEXwfze)
# ---------------------------------------------------------------------

for _ in range(int(input())):
    line = input()
    if line[:10] == "Simon says":
        print(line[11:])
