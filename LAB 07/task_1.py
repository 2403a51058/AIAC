
# The error is that the function is called with a string argument ("5") instead of an integer.
# Also, the base case for n==0 should return 1 for a factorial-like function.
# Here is the corrected code:

def factr(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factr(n - 1)
print(factr(5))



