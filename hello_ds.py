#DS217 Assignment 1 Wenli Xie#

#Task 1#
print("Hello, Data Science!")

#Task 2#
total_sum = 0
for num in range(1000):
    if num % 3 == 0 or num % 5 == 0:
        total_sum += num

print("The sum of all multiples of 3 or 5 below 1000 is:", total_sum)
