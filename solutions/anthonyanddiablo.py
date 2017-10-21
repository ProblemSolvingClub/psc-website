# Author: Martin Tran
# Email: martin.tran@ucalgary.ca
# Feel free to send any questions about this problem to the email above
# or ask in the CPC discord. (discord.gg/MEXwfze)
# ---------------------------------------------------------------------
import math

A, N = [float(x) for x in input().split()]
if A <= math.pow(N, 2)/(4*math.pi):
    print('Diablo is happy!')
else:
    print('Need more materials!')
