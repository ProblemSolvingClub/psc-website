# Author: Thomas Vu
# Email: thomas.vu@ucalgary.ca
# Feel free to send any questions about this problem to the email above
# or ask in the CPC discord. (discord.gg/MEXwfze)
# ---------------------------------------------------------------------

for _ in range(int(input())):
    people = {}
    classes = {}

    for _ in range(int(input())):
        line = input().split()
        people[line[0][:-1]] = line[1].split("-")

    for person in people:

        classNumber = ""
        for distinction in reversed(people[person]):
            if distinction == "upper":  classNumber += "1"
            if distinction == "middle": classNumber += "2"
            if distinction == "lower":  classNumber += "3"
        classNumber += "2" * (10-len(classNumber))

        if classNumber in classes:
            classes[classNumber].append(person)
        else:
            classes[classNumber] = [person]

    for key in sorted(classes.keys()):
        for person in sorted(classes[key]):
            print(person)

    print("==============================")