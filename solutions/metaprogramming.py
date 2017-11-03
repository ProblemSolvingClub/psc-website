# Author: Thomas Vu
# Email: thomas.vu@ucalgary.ca
# Feel free to send any questions about this problem to the email above
# or ask in the CPC discord. (discord.gg/MEXwfze)
# ---------------------------------------------------------------------

try:

    dic = {}
    while True:
        command, *args = input().split()

        if command == "define":
            dic[args[1]] = args[0]

        if command == "eval":
            if args[0] in dic and args[2] in dic:
                if args[1] == "=":
                    args[1] = "=="
                print(str(eval(dic[args[0]] + " " + args[1] + " " + dic[args[2]])).lower())
            else:
                print("undefined")

except EOFError as e:
    pass
