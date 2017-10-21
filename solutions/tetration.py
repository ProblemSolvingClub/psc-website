# Author: Martin Tran
# Email: martin.tran@ucalgary.ca
# Feel free to send any questions about this problem to the email above
# or ask in the CPC discord. (discord.gg/MEXwfze)
# ---------------------------------------------------------------------
from math import pow as fpow  # Make sure you use the pow() from the math library
N = float(input())            # since the regular pow() is only accurate for ints!
print(fpow(N, 1/N))
