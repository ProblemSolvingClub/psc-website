# Author: Thomas Vu
# Email: thomas.vu@ucalgary.ca
# Feel free to send any questions about this problem to the email above
# or ask in the CPC discord. (discord.gg/MEXwfze)
# ---------------------------------------------------------------------

alphabet = "abcdefghijklmnopqrstuvwxyz"
unpaired = [0 for _ in range(26)]  # creating a list with 26 0's in it

string = input()

for ch in string:
    i = alphabet.find(ch)  # finding the index of the character in the alphabet
    if unpaired[i] == 0:   # flips unpaired[i] from 0 to 1
        unpaired[i] = 1
    else:                  # flips unpaired[i] from 1 to 0
        unpaired[i] = 0

print(max(0, sum(unpaired)-1))  # prints 0 or the sum of the unpaired list
                                # minus one, whichever is larger
