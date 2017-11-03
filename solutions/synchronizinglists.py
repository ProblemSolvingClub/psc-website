# Author: Thomas Vu
# Email: thomas.vu@ucalgary.ca
# Feel free to send any questions about this problem to the email above
# or ask in the CPC discord. (discord.gg/MEXwfze)
# ---------------------------------------------------------------------

n = int(input())
while n != 0:
    list1, list2 = [], []

    for _ in range(n):
        list1.append(int(input()))
    for _ in range(n):
        list2.append(int(input()))

    sortedlist1, sortedlist2, = sorted(list1), sorted(list2)

    for x in list1:
        print(sortedlist2[sortedlist1.index(x)])
    print()

    n = int(input())
