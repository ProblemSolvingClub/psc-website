# Author: Martin Tran
# Email: martin.tran@ucalgary.ca
# Feel free to send any questions about this problem to the email above
# or ask in the CPC discord. (discord.gg/MEXwfze)
# ---------------------------------------------------------------------
notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
scales = {}
num_notes = len(notes)
for i in range(len(notes)//2):  # Make a dictionary mapping scales to their notes
    scales[notes[i]] = set([notes[i % (num_notes)],
                            notes[(i+2) % num_notes],
                            notes[(i+4) % num_notes],
                            notes[(i+5) % num_notes],
                            notes[(i+7) % num_notes],
                            notes[(i+9) % num_notes],
                            notes[(i+11) % num_notes]])
input()  # Skip the first line of input
input_notes = set(input().split())
possible_scales = []
for major_name, major_notes in scales.items():
    if len(input_notes - major_notes) == 0:  
        possible_scales.append(major_name)

print(sorted(possible_scales))
