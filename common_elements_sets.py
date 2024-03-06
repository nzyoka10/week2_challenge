# Common Elements in Sets:
# Write a program that accepts user input to create two sets of integers. 
# Then, create a new set that contains only the elements that are common to both sets.
print('\n')

# Function to get a set of integers from user input
def get_integer_set_from_input():
    
    # Prompt the user to enter integers separated by commas
    input_str = input("Enter integers separated by commas: ")
    
    # Split the input string by commas to get a list of strings
    integer_list = input_str.split(',')
    
    # Create an empty set to store integers
    integer_set = set()
    
    # Iterate through each string in the list
    for num_str in integer_list:
        
        try:
            # Convert the string to an integer
            num = int(num_str)
            
            # Add the integer to the set
            integer_set.add(num)
            
        except ValueError:
            # If the string cannot be converted to an integer, ignore it
            print(f"Ignoring '{num_str}'. Please enter only integers.")
            
    # Return the set of integers
    return integer_set

def main():
    print("\t Welcome to the Common Elements Finder!")
    print("This program finds common elements between two sets of integers.")
    print()

    print("Let's create the first set:")
    # Call the function to get the first set of integers from the user
    set1 = get_integer_set_from_input()

    print("\nGreat! Now let's create the second set:")
    # Call the function to get the second set of integers from the user
    set2 = get_integer_set_from_input()

    # Find the common elements between the two sets
    common_elements = set1.intersection(set2)

    if common_elements:
        # If there are common elements, print them
        print("\n Common elements in the sets:", common_elements)
    else:
        # If there are no common elements, inform the user
        print("\n There are no common elements in the sets.")

if __name__ == "__main__":
    # Call the main function when the script is executed
    main()

