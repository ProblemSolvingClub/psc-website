# Author: Thomas Vu
# Email: thomas.vu@ucalgary.ca
# Feel free to send any questions about this problem to the email above
# or ask in the CPC discord. (discord.gg/MEXwfze)
# ---------------------------------------------------------------------

import string
for _ in range(int(input())):
    missingLetters = list(string.ascii_lowercase)
    for ch in input().lower():
        if ch in missingLetters:
            missingLetters.remove(ch)
    print("pangram" if len(missingLetters) == 0 else "missing", "".join(missingLetters))
