# Author: Thomas Vu
# Email: thomas.vu@ucalgary.ca
# Feel free to send any questions about this problem to the email above
# or ask in the CPC discord. (discord.gg/MEXwfze)

n = int(input())
temperatures = [int(i) for i in input().split()]
tempsBelowZero = 0
for temp in temperatures:
    if temp < 0:
        tempsBelowZero += 1
print(tempsBelowZero)


# Short version:

# input()
# print(input().count("-"))
