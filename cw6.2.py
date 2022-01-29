def bounded_min(first, *args, lo=float('-inf'), hi = float('inf')):
    min_value = hi
    for value in (first, ) +args:
        if value < min_value and lo<value<hi:
            min_value=value
    return max(min_value, lo)

print(bounded_min(-5,12,13,lo=0, hi=255))