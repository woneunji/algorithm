def solution(a, b, c, d):
    nums = [a, b, c, d]
    counts = [nums.count(i) for i in nums]
    if max(counts) == 4:
        return a * 1111
    elif max(counts) == 3:
        p = nums[counts.index(3)]
        q = nums[counts.index(1)]
        return (10 * p + q) ** 2
    elif max(counts) == 2:
        if min(counts) == 2:
            return (a + c) * abs(a - c) if a == b else (a + b) * abs(a - b)
        else:
            p = nums[counts.index(2)]
            return (a * b * c * d) / p**2
    else:
        return min(nums)

'''def solution(a, b, c, d):
    four = False
    three = False
    two = False
    p = q = r = 0
    
    if (a == b):
        two = True
        p = a
        if (a == c):
            two = False
            three = True
            if (a == d):
                three = False
                four = True
            else:
                q = d
        elif (a == d):
            two == False
            three = True
            q = c
        elif (c == d):
            q = c
        elif (c != d):
            q = c
            r = d
    elif (a == c):
        two = True
        p = a
        if (a == d):
            two = False
            three = True
            q = b
        elif (b == d):
            q = b
        elif (b != d):
            q = b
            r = d
    elif (a == d):
        two = True
        p = a
        if (b == c):
            q = b
        else:
            r = c
    elif (b == c):
        two = True
        p = b
        if (b == d):
            two = False
            three = True
            q = a
        elif (a == d):
            q = a
        else:
            q = a
            r = d
    elif (c == d):
        two = True
        q = a
        r = b
    else:
        l = [a, b, c, d]
        p = min(l)
    
    if (two):
        if r != 0:
            return (q * r)
        else:
            return ((p + q) * abs(p - q))
    elif (three):
        return (10 * p + q) ** 2
    elif (four):
        return (1111 * p)
    else:
        return p'''