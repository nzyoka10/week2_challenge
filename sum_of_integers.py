
# program that accepts user input to create a list of integers. 
# Then, compute the sum of all the integers in the list.

print('\n')

# my_list = [1,2,3,4,5]
# sum = sum(my_list)
# print(len(my_list))
# print(sum)
# print(sum(my_list))

my_list = input("Enter your list of integers - separated by comma ( , ): ")

numbers = [
    int(x) for x in my_list.split(',')
]
print("My list contains: ", numbers)

sum_of_list = sum(numbers)
print("Sum of list (integers): ", sum_of_list)

