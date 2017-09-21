"""
 Author: Thomas Vu
 Discord: Thomas
 Email: thomas.vu@ucalgary.ca

 Feel free to send any questions about this problem
 to the email above or ask in the CPC discord.
"""
def starsForRank():
    global rank
    if 25 >= rank >= 21: return 2
    if 20 >= rank >= 16: return 3
    if 15 >= rank >= 11: return 4
    if 10 >= rank >= 1:  return 5
    else:                return 0

def addStar():
    global rank, stars, reachedLegend
    if stars == starsForRank():
        rank -= 1
        stars = 1
        if rank == 0: reachedLegend = True
    else:
        stars += 1

def loseStar():
    global rank, stars
    if stars == 0:
        rank += 1
        stars = starsForRank() - 1
    else:
        stars -= 1

#######################################################

matchHistory = input()
winStreak = 0
rank = 25
stars = 0
reachedLegend = False

for game in matchHistory:
    if game == "W":
        winStreak += 1
        if winStreak >= 3 and 25 >= rank >= 6:
            addStar()
        addStar()
    else:
        winStreak = 0
        if rank <= 19 or (rank == 20 and stars > 0):
            loseStar()

print("Legend" if reachedLegend else rank)
