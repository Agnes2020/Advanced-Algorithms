# algorithm to calculate the sum of first n given numbers

# assigning n to a given number
n = 10
# sum variable to store and add numbers in each iteration

sum = 0
# loop from 1 to n
for num in range(1, n + 1, 1):
    sum = sum + num
    # returning answer
print("Sum of first ", n, "numbers is: ", sum)
