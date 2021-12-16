# algorithm to return the super digit of a given integer

def solve(x):
    s = 0

    while(x > 0 or s > 9):
      if x == 0:
             x = s
             s = 0
    
      s += x % 10
      x //= 10

    return s
    
x = 513682
print(solve(x))