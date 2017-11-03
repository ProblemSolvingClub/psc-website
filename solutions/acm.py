# Author: Thomas Vu
# Email: thomas.vu@ucalgary.ca
# Feel free to send any questions about this problem to the email above
# or ask in the CPC discord. (discord.gg/MEXwfze)
# ---------------------------------------------------------------------

attempts = {}
correct = 0
penalty = 0

line = input()
while line != "-1":
    time, question, result = line.split()

    if question in attempts:
        attempts[question] += 1
    else:
        attempts[question] = 0

    if result == "right":
        correct += 1
        penalty += int(time) + attempts[question] * 20

    line = input()

print(correct, penalty)
