# Author: Thomas Vu
# Email: thomas.vu@ucalgary.ca
# Feel free to send any questions about this problem to the email above
# or ask in the CPC discord. (discord.gg/MEXwfze)
# ---------------------------------------------------------------------

# Using individual variables:

K, Q, R, B, N, P = [int(i) for i in input().split()]
print(1-K, 1-Q, 2-R, 2-B, 2-N, 8-P)



# Using a list:

# myList = [int(i) for i in input().split()]
# validChessSet = [1,1,2,2,2,8]
# answer = ""
# for index, element in enumerate(myList):
#     answer += str(validChessSet[index] - element) + " "
# print(answer)



# Using a list short version:

# myList = [int(i) for i in input().split()]
# validChessSet = [1,1,2,2,2,8]
# print(" ".join(str(validChessSet[i] - myList[i]) for i in range(6)))
