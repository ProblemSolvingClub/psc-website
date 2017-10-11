# Author: Thomas Vu
# Email: thomas.vu@ucalgary.ca
# Feel free to send any questions about this problem to the email above
# or ask in the CPC discord. (discord.gg/MEXwfze)
# ---------------------------------------------------------------------

history = {}
for _ in range(int(input())):
    word = input()

    for i in range(1, len(word)+1):   # Progressively slice the word.
        if word[:i] in history:       # We've seen this prefix before.
            history[word[:i]] += 1    # Note that we've seen it again: += 1
        else:
            history[word[:i]] = 0     # First time seeing this prefix.

    print(history[word])
