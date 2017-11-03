# Author: Thomas Vu
# Email: thomas.vu@ucalgary.ca
# Feel free to send any questions about this problem to the email above
# or ask in the CPC discord. (discord.gg/MEXwfze)
# ---------------------------------------------------------------------

input()
notes = [x for x in input().split()]

data = [ ["G", " ", "G: "],
         ["F", "-", "F: "],
         ["E", " ", "E: "],
         ["D", "-", "D: "],
         ["C", " ", "C: "],
         ["B", "-", "B: "],
         ["A", " ", "A: "],
         ["g", "-", "g: "],
         ["f", " ", "f: "],
         ["e", "-", "e: "],
         ["d", " ", "d: "],
         ["c", " ", "c: "],
         ["b", " ", "b: "],
         ["a", "-", "a: "], ]

for note in notes:
    duration = 1 if len(note) == 1 else int(note[1:])

    for d in data:
        if d[0] == note[0]:
            d[2] += ("*" * duration) + d[1]
        else:
            d[2] += d[1] * (duration + 1)

for d in data:
    print(d[2][:-1])
