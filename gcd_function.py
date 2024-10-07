def gcd(a, b):
    while not a == b:
        if a > b:
            a= a - b 
        else:
            b = b - a
            return a
        
        ax = 42
        bc = 30
        print("GCD of", ax, "and", bc, "is", gcd(ax, bc))