# 1. Countdown - Create a function that accepts a number as an input.
# Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
# Example: countdown(5) should return [5,4,3,2,1,0]
# value = int(input("Type a number:\n"))
# newlist = []
# for x in range(value, -1, -1):
#     newlist.append(x)

# print(f'{newlist}')
# 
# 
# 2. Print and Return - Create a function that will receive a list with two numbers.
# Print the first value and return the second.
# Example: print_and_return([1,2]) should print 1 and return 2
# def twonum(please):
#     print(please[0])
#     return please[1]

# print(twonum([1,2]))
# 
# 
# 3. First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
# Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)
# def first_plus_length(help):
#      return help[0] + len(help)

# print(first_plus_length([1,2,3,4,5]))
# 
# 
# 4. Values Greater than Second - 
# Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. 
# def values_greater_than_second(original):
# # Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
#     if len(original) < 2:
#         return False
#     newlist = []
#     for i in range(0,len(original)):
#         if original[i] > original[1]:
#             newlist.append(original[i])
#     print(len(newlist))
#     return newlist

# print(values_greater_than_second([5,2,3,2,1,4]))
# print(values_greater_than_second([3]))
        
# Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
# Example: values_greater_than_second([3]) should return False
# 
# 
# 5. This Length, That Value - Write a function that accepts two integers as parameters: size and value. 
def length_and_value(size, value):
    newlist = []
    newlist.append((value) * size)
# The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
    return length_and_value(4,7)
    return length_and_value(6,2)
# Example: length_and_value(4,7) should return [7,7,7,7]
# Example: length_and_value(6,2) should return [2,2,2,2,2,2]