def binary(arr,target):
    l ,r = 0,len(arr) - 1
    while l <= r:
        mid = l  + (r - l)//2
        if arr[mid] ==  target:
            while mid < r and arr[mid] == arr[mid + 1]:               
                mid += 1 
            return mid + 1
        elif arr[mid] >  target:
            r = mid - 1
        else:
            l = mid + 1
    return l 

## O(n*n) 81%
def solution__binary(A):
    # write your code in Python 3.6
    border = []
    for i,n in enumerate(A):
        border.append([i - n,i + n])    
    border.sort()
    start = []
    end = []
    for s,e in border:
        start.append(s)
        end.append(e)


    count = 0
    n = len(A)
    for i in range(n - 1):
        s = start.pop(0)
        e = end.pop(0)
        count += binary(start,e)
    return count


def solution(A):
    discs_count = len(A)            # The total number of discs
    range_upper,range_lower = [],[]
    # Fill the limit_upper and limit_lower
    for index,n in enumerate(A):
        range_upper.append(index + n)
        range_lower.append(index - n)

    range_upper.sort()
    range_lower.sort()
    range_lower_index = 0
    intersect_count = 0
    for range_upper_index in range(discs_count):
        # Compute for each disc
        while range_lower_index < discs_count and range_upper[range_upper_index] >= range_lower[range_lower_index]:
            # Find all the discs that:
            #    disc_center - disc_radius <= current_center + current_radius
            range_lower_index += 1
        # We must exclude some discs such that:
        #    disc_center - disc_radius <= current_center + current_radius
        #    AND
        #    disc_center + disc_radius <(=) current_center + current_radius
        # These discs are not intersected with current disc, and below the
        #    current one completely.
        # After removing, the left discs are intersected with current disc,
        #    and above the current one.
        # Attention: the current disc is intersecting itself in this result
        #    set. But it should not be. So we need to minus one to fix it.
        intersect_count += range_lower_index - range_upper_index -1
        if intersect_count > 10000000:
            return -1
    return intersect_count

