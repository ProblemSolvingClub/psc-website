n = int(input())    # number of test cases (how many lines will follow)
for i in range(n):  # do something 'n' times
    r, e, c = [int(i) for i in input().split()]  # stores 3 numbers from a line
    print("Expected revenue (No ads):", r)
    print("Expected revenue (With ads):", e)
    print("Cost of ads:", c)
    print()
