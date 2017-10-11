# Author: Thomas Vu
# Email: thomas.vu@ucalgary.ca
# Feel free to send any questions about this problem to the email above
# or ask in the CPC discord. (discord.gg/MEXwfze)
# ---------------------------------------------------------------------

asciiNums = ["**** ** ** ****",
             "  *  *  *  *  *",
             "***  *****  ***",
             "***  ****  ****",
             "* ** ****  *  *",
             "****  ***  ****",
             "****  **** ****",
             "***  *  *  *  *",
             "**** ***** ****",
             "**** ****  ****"]

line1 = input()
line2 = input()
line3 = input()
line4 = input()
line5 = input()

numDigits = (len(line1) + 1) // 4
numbers = []
for _ in range(numDigits):
    numbers.append("")

for i in range(numDigits):
    numbers[i] += line1[i*4:i*4+3]
    numbers[i] += line2[i*4:i*4+3]
    numbers[i] += line3[i*4:i*4+3]
    numbers[i] += line4[i*4:i*4+3]
    numbers[i] += line5[i*4:i*4+3]

theNumber = ""
boom = False
for n in numbers:
    if n in asciiNums:
        theNumber += str(asciiNums.index(n))
    else:
        boom = True

if boom == False and int(theNumber) % 6 == 0:
    print("BEER!!")
else:
    print("BOOM!!")
