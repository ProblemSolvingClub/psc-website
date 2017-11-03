# Author: Thomas Vu
# Email: thomas.vu@ucalgary.ca
# Feel free to send any questions about this problem to the email above
# or ask in the CPC discord. (discord.gg/MEXwfze)
# ---------------------------------------------------------------------

try:

    case = 0
    while True:
        a, b = [int(x) for x in input().split()]
        c, d = [int(x) for x in input().split()]
        input()

        determinant = a*d-b*c

        case += 1
        print("Case {}:".format(case))
        print(round( d/determinant), round(-b/determinant))
        print(round(-c/determinant), round( a/determinant))

except EOFError as e:
    pass
