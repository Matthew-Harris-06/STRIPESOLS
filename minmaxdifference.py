def min_max_difference(num):
    
    digits = [int(digit) for digit in str(num)]
    smallest = digits.copy()
    smallest.sort()
    digits.sort(reverse=True)
    
    return(int("".join([str(x) for x in digits]))-int("".join([str(x) for x in smallest])))
    



