# Author: Thomas Vu
# Email: thomas.vu@ucalgary.ca
# Feel free to send any questions about this problem to the email above
# or ask in the CPC discord. (discord.gg/MEXwfze)
# ---------------------------------------------------------------------

line = input()
T = line.count("T")
C = line.count("C")
G = line.count("G")
print(T**2 + C**2 + G**2 + min(T,C,G)*7)
