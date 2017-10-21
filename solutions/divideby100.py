# Author: Martin Tran
# Email: martin.tran@ucalgary.ca
# Feel free to send any questions about this problem to the email above
# or ask in the CPC discord. (discord.gg/MEXwfze)
# ---------------------------------------------------------------------
N, M = input(), input()
num_zeroes = len(M) - 1

if num_zeroes == 0:
    print(N)
    
elif len(N) > num_zeroes:
    print((N[:-num_zeroes] + '.' + N[-num_zeroes:]).rstrip('0').rstrip('.'))

elif len(N) == num_zeroes:
    print(('0.' + N).rstrip('0'))

else:
    print(('0.' + M[1:num_zeroes-len(N)+1] + N).rstrip('0').rstrip('.'))
