#1
# write a function that returns the sum of integers from 1 to n
def sum_to(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    print(sum)

sum_to(10)

#2
# write a function named largest that takes a list of numbers as argument and returns the largest number in the list
def largest(numbers):
    largest = numbers[0]
    for i in numbers:
        if i > largest:
            largest = i
    print(largest)

largest([1,2,3,4,5,6,7,8,400,10])

#3
# Write a function named occurences that takes two string arguments as input and counts the number of occurences of the second string in the first string
def occurences(string, substring):
    count = 0
    for i in range(len(string)):
        if string[i:i+len(substring)] == substring:
            count += 1
    print(count)

occurences("hello world", "o")

#4
# Write a function named product that takes an arbitrary number of numbers, multiplies them all together, and returns the product. HINT: Review your notes on args.
def product(*numbers):
    product = 1
    for i in numbers:
        product *= i
    print(product)

product(1,2,3,4,5,6,7,8,9,10)