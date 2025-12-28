def bin_pow(a, p, m):
    if p == 0:
        return 1

    if p % 2 == 1:
        return (bin_pow(a, p - 1, m) * a) % m
    
    else:
        t =  bin_pow(a, p // 2, m)
        return (t * t) % m
    

"""
regular ** operation is linear time complexity, while this algorithm works
in O(logn)
"""