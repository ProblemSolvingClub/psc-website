# Author: Thomas Vu
# Email: thomas.vu@ucalgary.ca
# Feel free to send any questions about this problem to the email above
# or ask in the CPC discord. (discord.gg/MEXwfze)
# ---------------------------------------------------------------------

grades = []
for _ in range(5):
    grades.append(sum([int(i) for i in input().split()]))
print(grades.index(max(grades))+1, max(grades))
