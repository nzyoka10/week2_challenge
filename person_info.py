# Write a program that uses a dictionary to store information about a person, such as their name, age, and favorite color. 
# Ask the user for input and store the information in the dictionary. 
# Then, print the dictionary to the console.

# title
print("\n Personal Information! ")

# Create an empty dictionary to store person's information
person_info = {}

# Ask the user for input and store the information in the dictionary
person_info['name'] = input("Enter your name: ")
person_info['age'] = input("Enter your age: ")
person_info['favorite_color'] = input("Enter your favorite color: ")

# Print the dictionary to the console
print("Person's information: ", person_info)
# print(person_info)
