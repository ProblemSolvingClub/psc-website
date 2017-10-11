# Author: Thomas Vu
# Email: thomas.vu@ucalgary.ca
# Feel free to send any questions about this problem to the email above
# or ask in the CPC discord. (discord.gg/MEXwfze)
# ---------------------------------------------------------------------

def solve(page):
    if page in memo:
        return memo[page]
    if book[page] == "favourably":
        return 1
    if book[page] == "catastrophically":
        return 0
    memo[page] = solve(book[page][0]) + solve(book[page][1]) + solve(book[page][2])
    return memo[page]

for _ in range(int(input())):
    memo = {}
    book = {}
    for _ in range(int(input())):
        line = input().split()
        if len(line) == 2:
            book[line[0]] = line[1]
        else:
            book[line[0]] = (line[1], line[2], line[3])
    print(solve("1"))
