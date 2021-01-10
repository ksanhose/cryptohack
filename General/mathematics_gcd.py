def gcd_ab(a, b): 
    if(b == 0): 
        return a 
    else: 
        return gcd_ab(b, a % b) 

a = 66528
b = 52920

print(gcd_ab(66528, 52920))
