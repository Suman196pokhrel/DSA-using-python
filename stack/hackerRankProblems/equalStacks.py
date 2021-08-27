# BruteForce Approach 

def equalStacks(h1, h2, h3):
    sum1, sum2, sum3 = map(sum, (h1, h2, h3))
    while h1 and h2 and h3:
        min_all = min(sum1,sum2,sum3)
        while sum1 > min_all: sum1=sum1- h1.pop(0) # poping the top of stack
        while sum2 > min_all: sum2 = sum2-h2.pop(0)
        while sum3 > min_all: sum3 = sum3-h3.pop(0)
        
        if sum1==sum2==sum3:
            return sum1
    
    return 0
                  