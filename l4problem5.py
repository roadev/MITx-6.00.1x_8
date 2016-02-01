lo = int(raw_input("Low"))
hi = int(raw_input("High"))
x = int(raw_input("x"))
def clip(lo, x, hi):
    '''
    Takes in three numbers and returns a value based on the value of x.
    Returns:
     - lo, when x < lo
     - hi, when x > hi
     - x, otherwise
    '''
    while (min(x, lo) < lo):
        return lo
    while (max(x, hi) > hi):
        return hi
    return x
z = clip(lo, x, hi)
print z
