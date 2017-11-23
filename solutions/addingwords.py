# Author: Thomas Vu
# Email: thomas.vu@ucalgary.ca
# Feel free to send any questions about this problem to the email above
# or ask in the CPC discord. (discord.gg/MEXwfze)
# ---------------------------------------------------------------------

try:
    memo = {}
    while True:
        command, *line = [i for i in input().split()]

        if command == "def":
            if line[0] in memo:
                del memo[memo[line[0]]]

            memo[line[0]] = line[1]
            memo[line[1]] = line[0]

        if command == "calc":
            unknown = False
            tokens = []
            for token in line[:-1]:
                if token in ("+", "-"):
                    tokens.append(token)
                elif token in memo:
                    tokens.append(memo[token])
                else:
                    unknown = True

            if unknown:
                print(" ".join(line), "unknown")
            else:
                expression = " ".join(tokens)
                if str(eval(expression)) in memo:
                    print(" ".join(line), memo[str(eval(expression))])
                else:
                    print(" ".join(line), "unknown")

        if command == "clear":
            memo.clear()

except EOFError as e:
    pass
