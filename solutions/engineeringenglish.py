# Author: Thomas Vu
# Email: thomas.vu@ucalgary.ca
# Feel free to send any questions about this problem to the email above
# or ask in the CPC discord. (discord.gg/MEXwfze)
# ---------------------------------------------------------------------

used = set()
try:
    while True:
        line = input().split()
        efficientLine = ""
        for word in line:
            if word.lower() not in used:
                efficientLine += word + " "
                used.add(word.lower())
            else:
                efficientLine += ". "
        print(efficientLine)
except EOFError as e:
    pass
